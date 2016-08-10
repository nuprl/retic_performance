#!/N/u/zmahmoud/Karst/Python-3.4.3/python

# Script for cluster nodes to follow.
#
# Basically,
# - each benchmark directory has a list of things to do
# - nodes grab a few configs off the list & run them many times
# - nodes save results to their own temp. directory
#
# There's just a few complications to make filesystem operations faster &
#  hopefully avoid filesystem data races.

# TODO may want to copy rectic & python-3.4.3 files to node-private space

## -----------------------------------------------------------------------------
## import

import glob
import os
import random
import re
import shutil
import subprocess
import time

## -----------------------------------------------------------------------------
## constants

USER         = "zmahmoud"
RP           = "/N/u/%s/Karst/retic_performance" % USER
RETIC        = "/N/u/%s/Karst/reticulated/retic.py" % USER

BOTH         = "both"
BENCHMARK    = "Benchmark"
TEST         = "Test"

MUTEX        = ".lock"
# Suffix for lockfiles

ITERS        = 40
# Number of iterations to run for each configuration

CHUNK        = 10
# Number of configurations to grab at once

KARST_INPUT  = "karst_input.txt"
# List of configurations that need to be run. Each benchmark has one of these.

KARST_OUTPUT = "karst_output.txt"
# This script collects results for each benchmark in a `KARST_OUTPUT` file

NODE_INPUT   = "node_input.txt"
NODE_OUTPUT  = "node_output.txt"
# Local list of TODO/DONE, so we can clean up after killed nodes

PBS_JOBID    = os.environ["PBS_JOBID"]
# Unique ID for node

NODE_QSTAT   = "qstat %s" % PBS_JOBID
# To check my status

## -----------------------------------------------------------------------------
## util

def file_pop(path, num_to_read):
  """
    Return the first `num_lines` lines from the file `path`,
     or the rest of `path`, if it has fewer lines.
    Delete the same lines from `path`.

    @param num_lines Positive-Integer
    @return Listof(String)
  """
  ln = []
  num_to_remove = 0
  with open(path, "r") as f:
    for line in f:
      ln.append(line)
      num_to_read -= 1
      num_to_remove += 1
      if num_to_read == 0:
        break # if we never hit this, we've emptied the file
  os.system("sed -i bak '%sd' %s" % (num_to_remove, path)) # fast way to delete lines from a file
  return ln

def get_benchmark_worklists(bm):
  return [wl for wl in glob.glob("%s/%s*" % (bm, KARST_INPUT))
          if os.path.getsize(wl) > 0]

def get_random_benchmark():
  """
    Pick a random benchmark with work left to do
    @return Path-String
  """
  all_bm = [bm for bm in glob.glob("%s/*/" % RP)
            if bool(glob.glob("%s/%s*" % (bm, KARST_INPUT)))]
  if bool(all_bm):
    return random.choice(all_bm)
  else:
    return None

def lock_worklist(wl):
  """
    Try to claim a worklist by writing a MUTEX file next to it.
    Hopefully Karst's filesystem makes this safe. But IDK.
    @return Boolean
  """
  m = "%s%s" % (wl, MUTEX)
  if not os.path.exists(m):
    with open(m, "a") as f:
      print(PBS_JOBID, file=f)
    # -- check that we wrote successfully
    with open(m, "r") as f:
      return f.read() == PBS_JOBID
  else:
    return False

def parse_elapsed_time_for_node(qstat_output):
  """
    Read the "%H:%M:%S" strings from a 1-line qstat output
    @returns List(Hour, Min, Sec)
             Hour = Min = Sec = Natural number
  """
  for ln in str(qstat_output, encoding="utf-8").split("\n"):
    m = re.search(r'([0-9]{2}):([0-9]{2}):([0-9]{2})', ln)
    if m:
      return [int(m.group(i)) for i in range(1, 4)]
  return None

def remaining_time():
  """
    Count the number of hours before Karst shuts this node down
    @return Natural
  """
  try:
    output = subprocess.check_output(NODE_QSTAT, shell=True, stderr=subprocess.STDOUT)
    if not output:
      raise ValueError("Node '%s' should be running, but got no result from qstat" % PBS_JOBID)
    elap_time = parse_elapsed_time_for_node(output)
    if not elap_time:
      raise ValueError("Could not parse the result of '%s'" % NODE_QSTAT)
    return 24 - elap_time[0]
  except (subprocess.CalledProcessError, ValueError):
    return 0

def unlock_worklist(wl):
  m = "%s%s" % (wl, MUTEX)
  if os.path.exists(m):
    os.remove(m)
    return
  else:
    raise ValueError("Missing lockfile for '%s'. Goodbye!" % wl)

## -----------------------------------------------------------------------------
## main

if __name__ == "__main__":
  while (remaining_time() > 1): #hours
    my_worklist = None
    my_configs  = None
    my_dir      = None
    # -- get all benchmarks with work left to do
    bm = get_random_benchmark()
    if not bm:
      break # all jobs finished!
    worklists = get_benchmark_worklists(bm)
    if not bool(worklists):
      # may have work left, and we just picked a bad benchmark
      for wl in glob.glob("%s/%s*" % (bm, KARST_INPUT)):
        try:
          os.remove(wl)
        except FileNotFoundError:
          pass
      continue
    random.shuffle(worklists)
    # -- pick a random worklist that's not being concurrently accessed
    for wl in worklists:
      if lock_worklist(wl):
        my_worklist = wl
    if my_worklist is None:
      time.sleep(1)
      continue
    ## -- read a few lines from the worklist
    my_configs = file_pop(my_worklist, CHUNK)
    unlock_worklist(my_worklist)
    ## -- setup node to run configs
    my_dir     = "%s/Test/%s" % (bm, PBS_JOBID)
    if not os.path.exists(my_dir):
      os.mkdir(my_dir)
      shutil.copytree("%s/%s" % (bm, BOTH)
                     ,my_dir)
    ## -- save my claimed configs to file, so `brun` can clean later
    with open("%s/%s" % (my_dir, NODE_INPUT), "w") as f:
      for cfg in my_configs:
        print(cfg, file=f)
    ## -- step through configs & run each
    for cfg in my_configs:
      my_results = []
      my_output  = "%s/%s" % (my_dir, NODE_OUTPUT)
      ## -- copy config files into test folder
      for file_dir, file_id in zip(glob.iglob("%s/%s/*/" % (bm, BENCHMARK)), cfg.split("-")):
        filename = os.path.basename(os.path.dirname(file_dir)) # messy, sorry. But dirname strips the last '/' and basename gets the string before the last '/'
        shutil.copyfile("%s/%s.py" % (file_dir, file_id)
                       ,"%s/%s.py" % (my_dir  , filename))
      ## -- finally run the config
      for i in range(ITERS):
        # Don't bother catching `CalledProcessError`, just die
        output  = subprocess.check_output("%s %s/main.py" % (RETIC, my_dir), shell=True)
        runtime = str(output, encoding="utf-8").split("\n")[-2]
        my_results.append(runtime)
      with open(my_output, "a") as f:
        # Don't care about num_types, just put 0
        print("%s    0    %s" % (cfg, my_results), file=f)
