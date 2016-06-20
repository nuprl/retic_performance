import random

with open("us-places-large.txt", "r") as f:
  for line in random.sample(list(f), 7000):
    print(line)
