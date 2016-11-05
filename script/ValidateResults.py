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

SEP = "    " # sorry world

def directory_of_benchmark_name(name):
  return os.path.join(GIT_ROOT, name)

def parse_benchmark_name(filename):
  before_dot = filename.split(".", 1)[0]
  maybe_dir = directory_of_benchmark_name(before_dot)
  if os.path.exists(maybe_dir):
    return [before_dot, maybe_dir]
  else:
    raise ValueError("Failed to infer benchmark name from filename '%s'." % filename)

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
        xs = line.strip().split(SEP)
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

def data_file_map(fn, data_file, suffix="mapped"):
  out_file = "%s.%s" % (data_file, suffix)
  with open(out_file, 'w') as g:
    with open(data_file, 'r') as f:
      for line in f:
        xs = line.strip().split(SEP)
        ys = fn(*xs)
        print(SEP.join(ys), file=g)
  return out_file

def fix_types(data_file, config_types_map):
  print("%s configs have incorrect type counts" % len(config_types_map))
  def check_and_fix_types(cfg, old_types, times):
    new_types = str(config_types_map.get(cfg, old_types))
    return [cfg, new_types, times]
  ty_file = data_file_map(check_and_fix_types, data_file, suffix="typed")
  print("Saved re-typed outputs to '%s'" % ty_file)
  return

def print_configs(out_file, cfgs, descr):
  with open(out_file, 'w') as g:
    for cfg in cfgs:
      print(cfg, file=g)
  print("Saved %s configs to '%s'" % (descr, out_file))

# TODO abstract me
def validate_file_duplicates(data_file, benchmark_files):
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

def count_types(nums, lengths):
    total = 0
    for num, length in zip(nums, lengths):
        b = bin(int(num))[2:]
        l = int(math.log2(length))
        c = ("0" * (l - len(b))) + b
        total += sum([1 for bit in c if bit == '0'])
    return total

# TODO abstract me
def validate_file_types(data_file, file_numconfigs_assoc):
  config_types_map = {}
  # 2016-11-05: assumes files & config ids use the same order
  numconfigs = [xs[1] for xs in file_numconfigs_assoc]
  with open(data_file, 'r') as f:
    for line in f:
      xs = line.strip().split(SEP)
      config = xs[0]
      actual_types = int(xs[1])
      expect_types = count_types(config.split("-"), numconfigs)
      if actual_types != expect_types:
        config_types_map[config] = expect_types
  return config_types_map

def main(argv):
  for data_file in argv:
    [benchmark_name, benchmark_dir] = parse_benchmark_name(os.path.basename(data_file))
    benchmark_bm_dir = os.path.join(benchmark_dir, BENCHMARK)
    if not os.path.exists(benchmark_bm_dir):
      print("Missing '%s/' directory for '%s', setup the benchmark and try again" % (BENCHMARK, benchmark_name))
      continue
    print("Validating output file '%s' against directory '%s'" % (data_file, benchmark_dir))
    benchmark_files = sorted([(os.path.basename(d), len(glob.glob(os.path.join(d, "*"))))
                       for d in glob.iglob(os.path.join(benchmark_bm_dir, "*")) ])
    print("Benchmark '%s' has %s files:" % (benchmark_name, len(benchmark_files)))
    for fc in benchmark_files:
      print("- %s.py : %s configs" % (fc[0], fc[1]))
    results = validate_file_duplicates(data_file, benchmark_files)
    print("Results now:")
    print("- %s missing configs" % len(results[MIS]))
    print("- %s duplicate configs" % len(results[DUP]))
    print("- %s invalid configs" % len(results[DNE]))
    perfect = True
    if 0 < len(results[DUP]):
      perfect = False
      fix_duplicates(data_file, results[DUP], results[DNE])
    if 0 < len(results[MIS]):
      perfect = False
      print_configs("%s.mis" % data_file, results[MIS], "missing")
    if 0 < len(results[DNE]):
      perfect = False
      print_configs("%s.dne" % data_file, results[DNE], "non-existant")
    if not perfect:
      return
    print("All '%s' configurations present in file '%s', checking type counts..." % (benchmark_name, data_file))
    config_types_map = validate_file_types(data_file, benchmark_files)
    if 0 < len(config_types_map):
      fix_types(data_file, config_types_map)
    else:
      print("Type counts in '%s' are OK." % data_file)
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



