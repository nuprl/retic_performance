import os

data = {}

for fn in os.listdir('out'):
    ex, kind = fn.split('_')
    if ex == 'pystone' or ex == 'hexiom':
        continue
    if ex not in data:
        data[ex] = {}
    with open('out/'+fn) as file:
        vals = [float(s) for s in file.read().split()]
        if len(vals) == 0:
            data[ex][kind] = 1
            continue
        s = sum(vals)
        avg = s/len(vals)
        data[ex][kind] = avg

print('Test case\tRatio\t\tTyped\t\tUntyped\tBlame ratio\tBlame')
for ex in data:
    ratio = data[ex]['typed']/data[ex]['untyped']
    bratio = data[ex]['blame']/data[ex]['untyped']
    print('%s\t\t%fx\t%f\t%f\t%fx\t%f' % \
          (ex, ratio, data[ex]['typed'], data[ex]['untyped'], bratio, data[ex]['blame']))
        
