#!/N/u/zmahmoud/Karst/Python-3.4.3/python

# Main script for running jobs on the cluster.
#
# Every day just do:
#   $ ./brun.py
# Until it says "All benchmarks finished!"

## -----------------------------------------------------------------------------
## import

import glob
import math
import os
import random
import re
import subprocess
import sys

## -----------------------------------------------------------------------------
## constants

USER    = "zmahmoud"
RP      = "/N/u/zmahmoud/Karst/retic_performance"

TEST    = "Test"

NODE_AI = "%s/karst/bnode.py" % RP
QSTAT   = "qstat -u %s" % USER
QSUB    = "qsub -k o -l nodes=1:ppn=16,walltime=24:00:00 %s" % NODE_AI
# warning: output goes in YOUR current directory. Please check those for errors!

KARST_INPUT = "karst_input.txt"
# List of configurations that need to be run. Each benchmark has one of these.

KARST_OUTPUT = "karst_output.txt"
# This script collects results for each benchmark in a `KARST_OUTPUT` file

NUM_NODES  = 99
# Max number of nodes to schedule at once (limit is like 700)

NODE_INPUT = "node_input.txt"
NODE_OUTPUT = "node_output.txt"
# Local list of TODO/DONE, for nodes to update

## -----------------------------------------------------------------------------
## typedef

# ConfigId
config_id_rx = r'([0-9]+-)+'
def is_config_id(string):
  return bool(re.match(config_id_rx, string))

## -----------------------------------------------------------------------------
## util

def is_finished(output):
  """
    A 'complete' line of output ends with a well-formed Python list.
    Just check for the last character of the list.
    @returns Boolean
  """
  return output.endswith("]")

def parse_config_id(output):
  """
    The `config_id` should be the first whitespace-separated component
     in a string of output.
    @returns ConfigId
  """
  cfg = output.split(" ", 1)
  if is_config_id(cfg):
    return cfg
  else:
    raise ValueError("parse_config_id: failed to parse '%s'" % output)

def parse_elapsed_times(qstat_output):
  """
    Read the "%H:%M:%S" strings from the last column of a `qstat` table.
    Return a list of parsed times, as 3-element lists.
    @returns Listof(List(Hour, Min, Sec))
             Hour = Min = Sec = Natural number
  """
  elaps = []
  for ln in qstat_output:
    m = re.search(r'([0-9]{2}):([0-9]{2}):([0-9]{2})$', ln)
    if m:
      elaps.append([int(m.group(i)) for i in range(1, 4)])
  return elaps

def warning(msg):
  print("WARNING: " + msg)

## -----------------------------------------------------------------------------
## main

def any_nodes_in_progress():
  """
    Check if all jobs are finished by checking the output of `qstat`
    @return Boolean
  """
  # Don't bother catching `CalledProcessError`, just die
  output = [x for x in str(subprocess.check_output(QSTAT, shell=True, stderr=subprocess.STDOUT), encoding="utf-8").split("\n") if x]
  if bool(output):
    elap_times = parse_elapsed_times(output)
    jobs_left  = len(output)
    hours_left = 24 - math.floor(max((t[0] for t in elap_times))) if bool(elap_times) else "??"
    print("Cannot start `./brun`, %s jobs still running (%s hours left). Use '%s' to check job status." % (jobs_left, hours_left, QSTAT))
    return True
  else:
    return False

def cleanup_nodes():
  """
    Cluster nodes save their (partial) results in temporary directories.
    - find tmp directories
    - save results for finished configs
    - put unfinished configs back on the global worklist
    @return Void
  """
  for bm_dir in glob.iglob(RP + "/*/"): # trailing / means 'directories only'
    karst_output = bm_dir + KARST_OUTPUT
    karst_inputs = glob.glob("%s/%s*" % (bm_dir, KARST_INPUT)) # may be []
    if not os.path.exists(karst_output):
      warning("Missing output file '%s', skipping benchmark." % karst_output)
      continue
    for node_dir in glob.iglob("%s/%s/*/" % (bm_dir, TEST)):
      # -- read the node's results file,
      #    collect a list of truly finished configs
      node_output = node_dir + NODE_OUTPUT
      node_input  = node_dir + NODE_INPUT
      if not os.path.exists(node_output):
        warning("Missing node output file '%s' skipping node." % node_output)
        continue
      if not os.path.exists(node_intput):
        warning("Missing node input file '%s' skipping node." % node_input)
        continue
      totally_finished_cfgs = set([])
      with open(node_output, "r") as in_lines:
        with open(karst_output, "a") as out_lines:
          for output in in_lines:
            if is_finished(output):
              # -- save result to global output file, save config.#
              print(output, file=out_lines)
              totally_finished_cfgs.add(parse_config_id(output))
      # -- read the node's list of claimed configs,
      #    write the unfinished ones back to the local `KARST_INPUT` file
      with open(node_input, "r") as in_lines:
        karst_input = random.choice(karst_inputs) if bool(karst_inputs) else "%s/%s0" % (bm_dir, KARST_INPUT)
        with open(karst_input, "a") as out_lines:
          for cfg in in_lines:
            if cfg not in totally_finished_cfgs:
              print(cfg, file=out_lines)
      # -- delete the node's directory, to save space
      os.rmdir(node_dir)
  return

def all_benchmarks_finished():
  """
    Return True if there are no configurations left to run for any benchmark.
    @return Boolean
  """
  for karst_input in glob.iglob("%s/*/%s*" % (RP, KARST_INPUT)):
    # http://stackoverflow.com/a/15924160/5237018
    if os.path.getsize(karst_input) > 0:
      return False
    else:
      os.remove(karst_input)
  return True

def run():
  if any_nodes_in_progress():
    return
  cleanup_nodes()
  if all_benchmarks_finished():
    print("All benchmarks finished! See results at:")
    for karst_output in glob.iglob("%s/*/%s" % (RP, KARST_OUTPUT)):
      print("* " + karst_output)
    return
  else:
    print("Starting %s nodes" % NUM_NODES)
    for i in range(NUM_NODES):
      os.system(QSUB)
    return

## -----------------------------------------------------------------------------

if __name__ == "__main__":
  if len(sys.argv) != 1:
    print("Usage: ./brun")
  else:
    run()
