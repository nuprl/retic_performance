
def tail(xs:List(Int))->List(Int):
  return xs[1:]

def magic(xs)->List(Int):
  return tail(xs)

ints = magic(["5", 6, 7, "8"])
print(ints[0] * ints[1])
# 42
print(ints)
# [6, 7, "8"]
