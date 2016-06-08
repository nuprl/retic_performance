from retic.runtime import *
from retic.transient import *
from retic.typing import *
from compat import xrange
import util
from math import sin, cos, sqrt
import optparse
import time


@fields({'x': float, 'y': float, 'z': float, })
class Point(retic_actual(object)):
    retic_class_type = Class('Point', {'__init__': Function(NamedParameters([('self', Dyn), ('i', Float)]), Dyn), 'maximize': Function(NamedParameters([('self', TypeVariable('Point')), ('other', TypeVariable('Point'))]), TypeVariable('Point')), 'normalize': Function(NamedParameters([('self', TypeVariable('Point'))]), Dyn), '__repr__': Function(NamedParameters([('self', TypeVariable('Point'))]), String), }, {'y': Float, 'x': Float, 'z': Float, })

    def __init__(self, i):
        check_type_float(i)
        self.x = x = check_type_function(sin)(i)
        self.y = (check_type_function(cos)(i) * 3)
        self.z = ((x * x) / 2)
    __init__ = check_type_function(__init__)

    def __repr__(self):
        check_type_object(self, ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
        return ('<Point: x=%s, y=%s, z=%s>' % (check_type_float(self.x), check_type_float(self.y), check_type_float(self.z)))
    __repr__ = check_type_function(__repr__)

    def normalize(self):
        check_type_object(self, ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
        x = check_type_float(self.x)
        y = check_type_float(self.y)
        z = check_type_float(self.z)
        norm = check_type_function(sqrt)((((x * x) + (y * y)) + (z * z)))
        self.x = check_type_float((check_type_float(self.x) / norm))
        self.y = check_type_float((check_type_float(self.y) / norm))
        self.z = check_type_float((check_type_float(self.z) / norm))
    normalize = check_type_function(normalize)

    def maximize(self, other):
        check_type_object(self, ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
        check_type_object(other, ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
        self.x = (check_type_float(self.x) if (check_type_float(self.x) > check_type_float(other.x)) else check_type_float(other.x))
        self.y = (check_type_float(self.y) if (check_type_float(self.y) > check_type_float(other.y)) else check_type_float(other.y))
        self.z = (check_type_float(self.z) if (check_type_float(self.z) > check_type_float(other.z)) else check_type_float(other.z))
        return self
    maximize = check_type_function(maximize)
Point = check_type_class(Point, ['__init__', 'maximize', 'normalize', '__repr__'])

def maximize(points):
    check_type_list(points)
    next = check_type_object(points[0], ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
    for p in check_type_list(points[1:]):
        check_type_object(p, ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
        next = check_type_function(check_type_object(next, ['maximize']).maximize)(p)
    return check_type_object(next, ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
maximize = check_type_function(maximize)

def benchmark(n):
    check_type_int(n)
    points = check_type_list([check_type_object(Point(check_type_float(i)), ['maximize', 'x', 'z', 'y', 'normalize', '__repr__']) for i in check_type_function(xrange)(n)])
    for p in check_type_list(points):
        check_type_function(check_type_object(p, ['normalize']).normalize)()
    return check_type_object(maximize(points), ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
benchmark = check_type_function(benchmark)
POINTS = 100000

def main(arg, timer):
    check_type_int(arg)
    times = []
    for i in check_type_function(xrange)(arg):
        t0 = check_type_function(timer)()
        o = check_type_object(benchmark(POINTS), ['maximize', 'x', 'z', 'y', 'normalize', '__repr__'])
        tk = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((tk - t0)))
    return times
main = check_type_function(main)
if (__name__ == '__main__'):
    parser = check_type_function(check_type_object(optparse, ['OptionParser']).OptionParser)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check_type_object(parser, ['parse_args']).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check_type_object(options, ['num_runs']).num_runs, main)
