"""
  usage: ValidateResults.py <file.txt> ...

  For each cluster output file <file.txt> given on the command line:
  - Searches for duplicate and repeated configs.
  - Creates a new file "<file.txt>.fix" with duplicates removed, if the
    duplicated rows have overlapping 95% confidence intervals.

  Be sure to double-check the ".fix" file against the original after this
  script finishes.
"""


import code
import itertools
import glob
import sys
import os
import statistics
import math

THIS_FILE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
GIT_ROOT = os.path.dirname(THIS_FILE_DIRECTORY)

BENCHMARK = "Benchmark"
DUP = "duplicate"
MIS = "missing"
DNE = "does_not_exist"

def directory_of_benchmark_name(name):
  return os.path.join(GIT_ROOT, name)

def parse_benchmark_name(filename):
  return filename.split(".", 1)[0]

def all_configs_of_filenames(benchmark_files):
  """
    [(str, int)] -> setstr
  """
  return set(("-".join([str(x) for x in ids])
              for ids in itertools.product(*[range(fc[1]) for fc in benchmark_files])))

def confidence95_ivl(vals):
  m = statistics.mean(vals)
  s = statistics.stdev(vals)
  n = len(vals)
  offset = (2 * s) / (math.sqrt(n))
  return [m - offset, m + offset]

def ivl_overlap(c0, c1):
  return ((c0[0] <= c1[0]) and (c1[0] <= c0[1])) or ((c1[0] <= c0[0]) and (c0[0] <= c1[1]))

def close_enough(valss):
  val0 = valss[0]
  m0 = statistics.mean(val0)
  s0 = statistics.stdev(val0)
  c0 = confidence95_ivl(val0)
  for vals in valss[1::]:
    c = confidence95_ivl(vals)
    if not ivl_overlap(c0, c):
      print("Confidence intervals for series do not overlap:")
      print("- (mean: %s, std %s) %s" % (m0, s0, val0))
      print("- (mean: %s, std %s) %s" % (statistics.mean(vals), statistics.stdev(vals), vals))
      if "n" == input("Accept anyway? [y/n]: "):
        return False
  return True

def valid_output(s):
  try:
    vals = eval(s)
    return isinstance(vals, list)
  except:
    return False

def fix_duplicates(data_file, dup, dne):
  data_for_dups = {}
  line_for_dups = {}
  for d in dup:
    if d not in dne:
      data_for_dups[d] = []
  fix_file = "%s.fix" % data_file
  with open(fix_file, 'w') as g:
    with open(data_file, 'r') as f:
      lineno = -1
      for line in f:
        lineno += 1
        xs = line.strip().split("    ")
        config = xs[0]
        if config in dne:
          continue
        if config in dup:
          if not valid_output(xs[-1]):
            print("Malformed output list on line %s: %s" % (lineno, xs[-1]))
          else:
            data_for_dups[config].append(eval(xs[-1]))
            line_for_dups[config] = xs[0:-1]
        elif valid_output(xs[-1]):
          print(line.strip(), file=g)
        else:
          print("Invalid %s" % config)
    for cfg,valss in data_for_dups.items():
      if not bool(valss):
        print("No data for %s" % cfg)
      elif close_enough(valss):
        print("    ".join((str(y) for y in line_for_dups[cfg] + [valss[0]])), file=g)
      else:
        print("Trouble with %s:\n    %s" % (cfg, valss))
  print("Saved de-duplicated outputs to '%s'" % fix_file)
  return

def print_configs(out_file, cfgs, descr):
  with open(out_file, 'w') as g:
    for cfg in cfgs:
      print(cfg, file=g)
  print("Saved %s configs to '%s'" % (descr, out_file))

def validate_file(data_file, benchmark_files):
  seen = set([])
  dne = set([])
  need = all_configs_of_filenames(benchmark_files)
  dup = set([])
  with open(data_file, "r") as f:
    for line in f:
      config = line.split(None, 1)[0]
      if config in seen:
        dup.add(config)
      else:
        seen.add(config)
        if config in need:
          need.remove(config)
        else:
          dne.add(config)
  return {DUP : dup
         ,MIS : need
         ,DNE : dne}

def main(argv):
  for data_file in argv:
    benchmark_name = parse_benchmark_name(os.path.basename(data_file))
    benchmark_dir = directory_of_benchmark_name(benchmark_name)
    benchmark_bm_dir = os.path.join(benchmark_dir, BENCHMARK)
    if not os.path.exists(benchmark_bm_dir):
      print("Missing '%s/' directory for '%s', setup the benchmark and try again" % (BENCHMARK, benchmark_name))
      continue
    print("Validating output file '%s' against directory '%s'" % (data_file, benchmark_dir))
    benchmark_files = [(os.path.basename(d), len(glob.glob(os.path.join(d, "*"))))
                       for d in glob.iglob(os.path.join(benchmark_bm_dir, "*")) ]
    print("Benchmark '%s' has %s files:" % (benchmark_name, len(benchmark_files)))
    for fc in benchmark_files:
      print("- %s.py : %s configs" % (fc[0], fc[1]))
    results = validate_file(data_file, benchmark_files)
    print("Results now:")
    print("- missing %s configs" % len(results[MIS]))
    print("- %s duplicate configs" % len(results[DUP]))
    print("- %s invalid configs" % len(results[DNE]))
    if 0 < len(results[DUP]):
      fix_duplicates(data_file, results[DUP], results[DNE])
    if 0 < len(results[MIS]):
      print_configs("%s.mis" % data_file, results[MIS], "missing")
    if 0 < len(results[DNE]):
      print_configs("%s.dne" % data_file, results[DNE], "non-existant")
    #print("Opening a REPL in current scope (results bound to local variable 'results') ...")
    #code.interact(local=locals())

def check_args(argv):
  if len(argv) < 2:
    # empty list of arguments
    return False
  for arg in argv[1:]:
    if not os.path.exists(arg):
      # invalid path
      return False
  return True

if __name__ == "__main__":
  if (check_args(sys.argv)):
    main(sys.argv[1:])
  else:
    print("usage: python ValidateResults.py <filename.txt> ...")



