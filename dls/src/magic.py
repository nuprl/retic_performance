
def tail(xs:List(String))->List(String):
  return xs[1:]

def magic(xs)->List(String):
  return tail(xs)

strings = magic([1,2,3])
print(strings)
# [2, 3]
