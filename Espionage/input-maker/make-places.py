import math
import random

DEGREE = 100
NUM_KEEP = 3

def name(loc):
  return loc[2]

def weight(loc1, loc2):
  [x1,y1,n1] = loc1
  [x2,y2,n2] = loc2
  return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def edges(G):
  edges = []
  for loc1 in G:
    for loc2 in random.sample(G, DEGREE):
      if loc2 != loc1:
        edges.append([name(loc1), name(loc2), weight(loc1, loc2)])
  return edges

def main():
  G = set([])
  with open("us-places-small.txt", "r") as f:
    for i, line in enumerate(f):
      [xy,loc] = line.split("\t")
      [x,y] = xy.split()
      # Goodbye loc
      G.add((float(x),float(y),i))
  E = edges(G)
  L = len(E)
  print("%s %s %s" % (L, L - NUM_KEEP, NUM_KEEP))
  for e in E[:L-NUM_KEEP]:
    print("%s %s %s" % (e[0], e[1], e[2]))
  for e in E[L-NUM_KEEP:]:
    print("%s %s" % (e[0], e[1]))

if __name__ == "__main__":
  main()
