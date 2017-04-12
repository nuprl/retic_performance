from benchmark_tools.Timer import Timer
import os, sys

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '..'))
data = (list(map(int, [line.strip() for line in open(
    "numbers.txt")])))
rand_num = (element for element in data)

def main():
  total = 0
  for n in rand_num:
    total += n
  return total

t = Timer()
with t:
  for i in range(100):
    main()
