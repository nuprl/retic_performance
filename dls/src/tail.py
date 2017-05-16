def tail(xs:List(String))->List(String):
  return xs[1:]

def caller(xs):
  return tail(xs)

ys = caller([4,5,6,7])
ys[0] = tail
print(ys[1] * ys[2])
