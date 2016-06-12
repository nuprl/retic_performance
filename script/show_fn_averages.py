"""
  Print the average runtime of configurations where a function is typed
   vs. configurations where the same function is untyped.

  Usage:
    python show_fn_averages.py <DATA.csv>

  For each function name (aka column) in the .csv file
   counts the average of all rows where the function is typed
   and the averate of all rows where the function is untyped.
  Prints all averages for all functions to STDOUT.
"""

import sys
import statistics


def run(fname):
  with open(fname, "r") as f:
    row0 = next(f).split(",")
    # -- collect matrix with rows [NAME, UNTYPED-TIME, TYPED-TIME]
    name_and_times_list = [(name.strip(), [], [])
                           for name in row0[1:]]
    all_times = []
    num_rows = 0
    for line in f:
      num_rows += 1
      row = line.strip().split(",")
      time = float(row[0])
      all_times.append(time)
      for (bit, name_and_times) in zip(row[1:], name_and_times_list):
        if bit == "1":
          name_and_times[1].append(time)
        else:
          name_and_times[2].append(time)
    # -- 
    half_rows = num_rows / 2
    print("\tTotal Avg: %s\n" % mean(all_times))
    print("\t%30s\t%s\t%s\t%s" % ("Function Name", "Untyped Avg", "Typed Avg", "Difference"))
    for [name, untyped, typed] in name_and_times_list:
      # -- print a warning if the number of points doesn't match what we expect
      #    (means we're missing some configurations for a function)
      if len(untyped) != half_rows:
        print("ERROR: only %s data points for %s untyped (expected %s)" % (len(untyped), name, half_rows))
      if len(typed) != half_rows:
        print("ERROR: only %s data points for %s typed" % (len(typed), name))
      um = mean(untyped)
      tm = mean(typed)
      diff = abs(um - tm)
      print("\t%30s\t%6s\t%6s\t%6s" % (name, um, tm, diff))

def rnd(n):
  return round(n, 4)

def mean(xs):
  if xs:
    return rnd(statistics.mean(xs))
  else:
    return "NaN"

def get_num_configurations(row):
  return 2 ** len(row[1:])


if __name__ == "__main__":
  run(sys.argv[1])
