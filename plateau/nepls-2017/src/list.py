def f(n:Int)->Int:
  return (n * (n+1)) // 2

def get_numbers(how_many:Int)->List(Int):
  nums = []
  for i in range(1, 1 + how_many):
    nums.append(f)
  return nums

print(get_numbers(4))

def apply_first(funs, n):
  return funs[0](n)

print(apply_first(get_numbers(4), 10))
