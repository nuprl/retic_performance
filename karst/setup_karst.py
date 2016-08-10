#!/N/u/zmahmoud/Karst/Python-3.4.3/python

# Sets up a list of benchmarks (or all benchmarks) for `brun`
#
# Usage:
#    ./setup_karst.py
# or:
#    ./setup_karst.py <dir> ...
# where each `<dir>` is a benchmark directory (tho, we'll double check for you)
#
# This script:
# - makes all the configurations
# - sets up directories that `brun` expects
# - makes a worklist of configurations to run

## -----------------------------------------------------------------------------
## imports

import glob
import itertools
import os
import shutil
import sys

## -----------------------------------------------------------------------------
## constants

USER      = "zmahmoud"
BASEPATH  = "/N/u/%s/Karst" % USER
PYTHON    = "%s/Python-3.4.3/python" % BASEPATH
RP        = "%s/retic_performance" % BASEPATH
TOOLS     = "%s/benchmark_tools/benchmark_tools" % BASEPATH
READER    = "%s/Reader.py" % TOOLS
TIMER     = "%s/Timer.py"  % TOOLS

BENCHMARK = "Benchmark"
BOTH      = "both"
TEST      = "Test"
TYPED     = "typed"

KARST_INPUT = "karst_input.txt"

LINES_PER_KARST_FILE = 100000
# Keep it small enough to 'quickly' read/write files of this length

## -----------------------------------------------------------------------------
## main

def ensure_dir(d):
  if not os.path.exists(d):
    os.mkdir(d)
  return

def is_benchmark(d):
  return os.path.isdir(d) and os.path.exists("%s/%s" % (d, TYPED))

def is_clean_benchmark(d):
  """
    Check if benchmark directory `d` has anything leftover from a past setup
    @returns Boolean
  """
  aliens = []
  for should_not_exist in [BENCHMARK, TEST, "karst*"]:
    aliens.extend(glob.glob("%s/%s" % (d, should_not_exist)))
  if bool(aliens):
    print("Benchmark directory %s has folders leftover from a previous setup:" % d)
    for alien in aliens:
      print("* %s" % alien)
    print("Remove these, then call './setup_karst.py %s'" % d)
    return False
  else:
    return True

def file_name(path):
  return os.path.splitext(os.path.basename(path))[0]

def run(dirs):
  for d in dirs:
    if not is_benchmark(d):
      continue
    if not is_clean_benchmark(d):
      continue
    print("Setting up '%s'" % d)
    # -- ok, really setup the benchmark
    both_dir = "%s/%s" % (d, BOTH)
    ensure_dir(both_dir)
    shutil.copyfile(TIMER, "%s/Timer.py" % both_dir)
    ensure_dir("%s/%s" % (d, TEST))
    os.system("%s %s %s/%s %s/%s" % (PYTHON, READER, d, TYPED, d, BENCHMARK))
    all_config_files = [glob.iglob("%s/*" % d) for d in glob.glob("%s/%s/*/" % (d, BENCHMARK))]
    output_index = 1
    output_file  = open("%s/%s%s" % (d, KARST_INPUT, output_index), "w")
    lines_left   = LINES_PER_KARST_FILE
    for files in itertools.product(*all_config_files):
      print("-".join((file_name(x) for x in files)), file=output_file)
      lines_left -= 1
      if lines_left == 0:
        output_file.close()
        output_index += 1
        output_file  = open("%s/%s/%s" % (d, KARST_INPUT, output_index), "w")
        lines_left   = LINES_PER_KARST_FILE

## -----------------------------------------------------------------------------

if __name__ == "__main__":
  # By default, run on all benchmark directories.
  # If directories are given, 
  if len(sys.argv) > 1:
    run([d for d in sys.argv[1::]
         if os.path.exists("%s/" % d)])
  else:
    run(glob.glob("%s/*/" % RP))
