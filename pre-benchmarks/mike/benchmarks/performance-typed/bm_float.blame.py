from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def check0(val, elim, act):
    try:
        val.__repr__
        val.y
        val.normalize
        val.z
        val.maximize
        val.x
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def cast4(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.__repr__
        val.y
        val.normalize
        val.z
        val.maximize
        val.x
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast6(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast1(val, src, b, trg):
    try:
        val.maximize
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast5(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.normalize
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym18 = Dyn
gensym109 = Dyn
gensym92 = Dyn
gensym35 = Function(NamedParameters([('points', List(Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, })))]), Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym89 = Function(AnonymousParameters([Int]), Dyn)
gensym62 = Function(AnonymousParameters([Int]), Dyn)
gensym104 = Object('', {'OptionParser': Dyn, })
gensym84 = Dyn
gensym39 = Function(AnonymousParameters([Dyn]), Dyn)
gensym44 = Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, })
gensym53 = Dyn
gensym46 = Dyn
gensym15 = Function(NamedParameters([('self', Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))]), String)
gensym56 = Function(AnonymousParameters([Int]), Dyn)
gensym73 = Dyn
gensym27 = Float
gensym36 = Dyn
gensym114 = Object('', {'num_runs': Dyn, })
gensym11 = Function(AnonymousParameters([Float]), Dyn)
gensym111 = Dyn
gensym17 = Function(NamedParameters([('self', Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))]), Dyn)
gensym76 = Function(AnonymousParameters([]), Dyn)
gensym94 = Dyn
gensym107 = Dyn
gensym49 = Function(AnonymousParameters([Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, })]), Dyn)
gensym31 = Function(NamedParameters([('self', Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, })), ('other', Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))]), Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym30 = Dyn
gensym6 = Dyn
gensym57 = Dyn
gensym37 = Object('', {'maximize': Dyn, })
gensym71 = Dyn
gensym54 = Function(NamedParameters([('n', Int)]), Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym19 = Function(AnonymousParameters([Dyn]), Dyn)
gensym64 = Float
gensym26 = Dyn
gensym43 = Function(AnonymousParameters([Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, })]), Dyn)
gensym25 = Float
gensym91 = Function(AnonymousParameters([]), Dyn)
gensym5 = Function(AnonymousParameters([Float]), Dyn)
gensym60 = List(Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym87 = Function(AnonymousParameters([]), Dyn)
gensym41 = Object('', {'maximize': Dyn, })
gensym9 = Function(AnonymousParameters([Float]), Dyn)
gensym58 = Float
gensym45 = Dyn
gensym82 = Dyn
gensym80 = Dyn
gensym40 = Dyn
gensym75 = Dyn
gensym24 = Dyn
gensym83 = Function(AnonymousParameters([Int]), Dyn)
gensym105 = Dyn
gensym47 = Object('', {'maximize': Dyn, })
gensym97 = Function(AnonymousParameters([]), Dyn)
gensym106 = Function(DynParameters, Dyn)
gensym95 = Function(AnonymousParameters([Int]), Dyn)
gensym116 = Dyn
gensym20 = Dyn
gensym8 = Dyn
gensym112 = Tuple(Dyn, Dyn)
gensym108 = Object('', {'parse_args': Dyn, })
gensym68 = Function(AnonymousParameters([Int]), Dyn)
gensym103 = Dyn
gensym63 = Dyn
gensym7 = Function(AnonymousParameters([Float]), Dyn)
gensym66 = List(Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym69 = Dyn
gensym93 = Function(AnonymousParameters([]), Dyn)
gensym51 = Dyn
gensym101 = List(Dyn)
gensym16 = Dyn
gensym2 = Dyn
gensym88 = Dyn
gensym74 = Object('', {'normalize': Dyn, })
gensym14 = Dyn
gensym102 = Dyn
gensym85 = Function(AnonymousParameters([]), Dyn)
gensym38 = Dyn
gensym52 = Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, })
gensym99 = Function(AnonymousParameters([]), Dyn)
gensym23 = Function(AnonymousParameters([Float]), Dyn)
gensym32 = Dyn
gensym96 = Dyn
gensym42 = Dyn
gensym110 = Function(AnonymousParameters([]), Dyn)
gensym115 = Function(NamedParameters([('arg', Int), ('timer', Dyn)]), Dyn)
gensym90 = Dyn
gensym48 = Dyn
gensym33 = Class('Point', {'normalize': Function(NamedParameters([('self', TypeVariable('Point'))]), Dyn), '__repr__': Function(NamedParameters([('self', TypeVariable('Point'))]), String), 'maximize': Function(NamedParameters([('self', TypeVariable('Point')), ('other', TypeVariable('Point'))]), TypeVariable('Point')), '__init__': Function(NamedParameters([('self', Dyn), ('i', Float)]), Dyn), }, {'z': Float, 'y': Float, 'x': Float, })
gensym86 = Dyn
gensym0 = Dyn
gensym10 = Dyn
gensym22 = Dyn
gensym29 = Float
gensym4 = Dyn
gensym67 = Dyn
gensym34 = Dyn
gensym59 = Dyn
gensym13 = Function(AnonymousParameters([Float]), Dyn)
gensym81 = Function(NamedParameters([('arg', Int), ('timer', Dyn)]), Dyn)
gensym98 = Dyn
gensym79 = List(Dyn)
gensym65 = Dyn
gensym28 = Dyn
gensym21 = Function(AnonymousParameters([Float]), Dyn)
gensym1 = Function(NamedParameters([('self', Dyn), ('i', Float)]), Dyn)
gensym55 = Dyn
gensym78 = List(Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym70 = Float
gensym72 = List(Object('Point', {'__repr__': Function(NamedParameters([]), String), 'y': Float, 'normalize': Function(NamedParameters([]), Dyn), 'z': Float, 'maximize': Function(NamedParameters([('other', TypeVariable('Point'))]), TypeVariable('Point')), 'x': Float, }))
gensym113 = Dyn
gensym61 = Dyn
gensym3 = Function(AnonymousParameters([Float]), Dyn)
gensym12 = Dyn
from compat import xrange
import util
from math import sin, cos, sqrt
import optparse
import time


class Point(retic_actual(object)):

    def __init__(self, i):
        mgd_check_type_float(i, self.__init__, (1, 1))
        self.x = x = mgd_cast_type_function(sin, gensym10, '12', gensym11)(i)
        self.y = (mgd_cast_type_function(cos, gensym12, '13', gensym13)(i) * 3)
        self.z = ((x * x) / 2)

    def __repr__(self):
        check0(self, self.__repr__, (1, 0))
        return ('<Point: x=%s, y=%s, z=%s>' % (mgd_check_type_float(self.x, self, (0, 'x')), mgd_check_type_float(self.y, self, (0, 'y')), mgd_check_type_float(self.z, self, (0, 'z'))))

    def normalize(self):
        check0(self, self.normalize, (1, 0))
        x = mgd_check_type_float(self.x, self, (0, 'x'))
        y = mgd_check_type_float(self.y, self, (0, 'y'))
        z = mgd_check_type_float(self.z, self, (0, 'z'))
        norm = mgd_cast_type_function(sqrt, gensym22, '23', gensym23)((((x * x) + (y * y)) + (z * z)))
        self.x = mgd_cast_type_float((mgd_check_type_float(self.x, self, (0, 'x')) / norm), gensym24, '24', gensym25)
        self.y = mgd_cast_type_float((mgd_check_type_float(self.y, self, (0, 'y')) / norm), gensym26, '25', gensym27)
        self.z = mgd_cast_type_float((mgd_check_type_float(self.z, self, (0, 'z')) / norm), gensym28, '26', gensym29)

    def maximize(self, other):
        check0(self, self.maximize, (1, 0))
        check0(other, self.maximize, (1, 1))
        self.x = (mgd_check_type_float(self.x, self, (0, 'x')) if (mgd_check_type_float(self.x, self, (0, 'x')) > mgd_check_type_float(other.x, other, (0, 'x'))) else mgd_check_type_float(other.x, other, (0, 'x')))
        self.y = (mgd_check_type_float(self.y, self, (0, 'y')) if (mgd_check_type_float(self.y, self, (0, 'y')) > mgd_check_type_float(other.y, other, (0, 'y'))) else mgd_check_type_float(other.y, other, (0, 'y')))
        self.z = (mgd_check_type_float(self.z, self, (0, 'z')) if (mgd_check_type_float(self.z, self, (0, 'z')) > mgd_check_type_float(other.z, other, (0, 'z'))) else mgd_check_type_float(other.z, other, (0, 'z')))
        return self
Point = mgd_cast_type_class(Point, gensym32, '8', gensym33, ['normalize', '__repr__', 'maximize', '__init__'])

def maximize(points):
    mgd_check_type_list(points, maximize, (1, 0))
    next = mgd_cast_type_dyn(check0(points[0], points, 3), gensym44, '36', gensym45)
    gensym50 = mgd_check_type_list(points[1:], points, 3)
    for p in gensym50:
        check0(p, gensym50, 3)
        next = mgd_cast_type_function(cast1(next, gensym46, '38', gensym47).maximize, gensym48, '38', gensym49)(p)
    return cast2(next, gensym51, '39', gensym52)

def benchmark(n):
    mgd_check_type_int(n, benchmark, (1, 0))
    points = mgd_cast_type_list([check0(Point(mgd_cast_type_float(i, gensym69, '42', gensym70)), Point, 2) for i in mgd_cast_type_function(xrange, gensym67, '42', gensym68)(n)], gensym71, '42', gensym72)
    gensym77 = mgd_cast_type_list(points, gensym78, '43', gensym79)
    for p in gensym77:
        mgd_cast_type_function(cast3(p, gensym73, '44', gensym74).normalize, gensym75, '44', gensym76)()
    return check0(maximize(points), maximize, 2)
POINTS = 100000

def main(arg, timer):
    mgd_check_type_int(arg, main, (1, 0))
    times = []
    gensym100 = mgd_cast_type_function(xrange, gensym94, '53', gensym95)(arg)
    for i in gensym100:
        t0 = mgd_cast_type_function(timer, gensym96, '54', gensym97)()
        o = check0(benchmark(POINTS), benchmark, 2)
        tk = mgd_cast_type_function(timer, gensym98, '56', gensym99)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((tk - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym101, '58', gensym102)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast4(optparse, gensym103, '61', gensym104).OptionParser, gensym105, '61', gensym106)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast5(parser, gensym107, '65', gensym108).parse_args, gensym109, '65', gensym110)(), gensym111, '65', gensym112, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast6(options, gensym113, '67', gensym114).num_runs, mgd_cast_type_dyn(main, gensym115, '67', gensym116))
