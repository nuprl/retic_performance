def f(n:Int)->Int:
  return (n * (n+1)) // 2

def get_numbers(how_many:Int)->List(Int):
  nums = []
  for i in range(1, 1 + how_many):
    nums.append(f)
  return nums

def apply_first(funs, n):
  return funs[0](n)

nums = get_numbers(4)
print(apply_first(nums, 10))
