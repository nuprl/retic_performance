from retic import List, Float, Int
import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '..'))
data = list(map(float, [line.strip() for line in open(
    'utill-random-numbers.txt')]))
rand_num = (element for element in data)

def accumulated_s(probabilities):
    total = sum(probabilities)
    payoffs = probabilities
    result = []
    next = 0
    for element in payoffs:
        next += element
        result = result + [next / total]
    return result

def choose_randomly(probabilities, speed):
    s = accumulated_s(probabilities)
    res = []
    for n in range(speed):
        r = next(rand_num)
        for i in range(len(s)):
            if r < s[i]:
                res = res + [i]
                break
    return res

def relative_average(l: List(Float), w: Float) ->Float:
    return sum(l) / w / len(l)

