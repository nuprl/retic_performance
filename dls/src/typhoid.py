def make_strings()->List(String):
  xs = []
  for i in range(3):
    if i == 0:
      xs.append(i)
    elif i == 1:
      xs.append(True)
    else:
      xs.append(make_strings)
  return xs

make_strings()
