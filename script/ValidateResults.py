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

def fix_duplicates(data_file, dup):
  data_for_dups = {}
  line_for_dups = {}
  for d in dup:
    data_for_dups[d] = []
  with open("%s.fix" % data_file, 'w') as g:
    with open(data_file, 'r') as f:
      for line in f:
        xs = line.strip().split("    ")
        config = xs[0]
        if config in dup:
          vals = eval(xs[-1])
          if not isinstance(vals, list):
            print("yo no %s %s" % (xs[-1], vals))
            raise ValueError()
          data_for_dups[config].append(vals)
          line_for_dups[config] = xs[0:-1]
        else:
          print(line.strip(), file=g)
    for cfg,valss in data_for_dups.items():
      if close_enough(valss):
        print("    ".join((str(y) for y in line_for_dups[cfg] + valss[0])), file=g)
      else:
        print("Trouble with %s:\n    %s" % (cfg, valss))

def validate_file(data_file, benchmark_files):
  seen = set([])
  need = all_configs_of_filenames(benchmark_files)
  dup = set([])
  with open(data_file, "r") as f:
    for line in f:
      config = line.split(None, 1)[0]
      if config in seen:
        dup.add(config)
      else:
        seen.add(config)
        need.remove(config)
  return {DUP : dup
         ,MIS : need}

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
    if 0 < len(results[DUP]):
      fix_duplicates(data_file, results[DUP])
    #print("Opening a REPL in current scope (results bound to local variable 'results') ...")
    #code.interact(local=locals())

def check_args(argv):
  if not bool(argv):
    # empty list of arguments
    return False
  for arg in argv:
    if not os.path.exists(arg):
      # invalid path
      return False
  return True

if __name__ == "__main__":
  if (check_args(sys.argv)):
    main(sys.argv)
  else:
    print("usage: python ValidateResults.py <filename.txt> ...")



