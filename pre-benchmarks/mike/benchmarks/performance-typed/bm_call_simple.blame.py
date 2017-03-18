from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def cast0(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.time
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast1(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym12 = Dyn
gensym16 = Dyn
gensym59 = Dyn
gensym3 = Function(NamedParameters([('a', Dyn), ('b', Int), ('c', Int)]), Dyn)
gensym11 = Function(NamedParameters([('iterations', Dyn), ('timer', Dyn)]), Dyn)
gensym22 = Dyn
gensym58 = Int
gensym86 = Dyn
gensym87 = Dyn
gensym41 = Dyn
gensym0 = Dyn
gensym35 = Dyn
gensym20 = Dyn
gensym26 = Dyn
gensym69 = Function(AnonymousParameters([]), Dyn)
gensym1 = Function(NamedParameters([('a', Dyn), ('b', Int), ('c', Int), ('d', Int)]), Dyn)
gensym28 = Int
gensym39 = Dyn
gensym54 = Int
gensym53 = Dyn
gensym5 = Function(NamedParameters([('a', Dyn), ('b', Int)]), Dyn)
gensym52 = Int
gensym47 = Dyn
gensym18 = Dyn
gensym88 = Object('', {'num_runs': Dyn, })
gensym23 = Function(AnonymousParameters([]), Dyn)
gensym80 = Function(AnonymousParameters([]), Dyn)
gensym6 = Dyn
gensym37 = Dyn
gensym48 = Int
gensym8 = Dyn
gensym45 = Dyn
gensym66 = Int
gensym64 = Int
gensym50 = Int
gensym83 = Dyn
gensym17 = Function(AnonymousParameters([]), Dyn)
gensym24 = Dyn
gensym56 = Int
gensym38 = Int
gensym25 = Function(AnonymousParameters([Dyn]), Dyn)
gensym90 = Dyn
gensym63 = Dyn
gensym51 = Dyn
gensym9 = Function(NamedParameters([]), Dyn)
gensym75 = Dyn
gensym21 = Function(AnonymousParameters([]), Dyn)
gensym31 = Dyn
gensym49 = Dyn
gensym60 = Int
gensym73 = Dyn
gensym29 = Dyn
gensym2 = Dyn
gensym79 = Dyn
gensym55 = Dyn
gensym77 = Dyn
gensym78 = Object('', {'parse_args': Dyn, })
gensym72 = Dyn
gensym82 = Tuple(Dyn, Dyn)
gensym13 = Function(AnonymousParameters([Dyn]), Dyn)
gensym57 = Dyn
gensym62 = Int
gensym7 = Function(NamedParameters([('a', Dyn)]), Dyn)
gensym10 = Dyn
gensym43 = Dyn
gensym33 = Dyn
gensym34 = Int
gensym32 = Int
gensym4 = Dyn
gensym40 = Int
gensym46 = Int
gensym67 = Dyn
gensym68 = Dyn
gensym27 = Function(AnonymousParameters([]), Dyn)
gensym89 = Function(NamedParameters([('iterations', Dyn), ('timer', Dyn)]), Dyn)
gensym81 = Dyn
gensym42 = Int
gensym30 = Int
gensym84 = Object('', {'time': Dyn, })
gensym85 = Int
gensym14 = Dyn
gensym44 = Int
gensym36 = Int
gensym74 = Object('', {'OptionParser': Dyn, })
gensym76 = Function(DynParameters, Dyn)
gensym19 = Function(AnonymousParameters([Dyn]), Dyn)
gensym71 = List(Dyn)
gensym65 = Dyn
gensym61 = Dyn
gensym15 = Function(AnonymousParameters([]), Dyn)
import optparse
import time
import util
from compat import xrange

def foo(a, b, c, d):
    mgd_check_type_int(b, foo, (1, 1))
    mgd_check_type_int(c, foo, (1, 2))
    mgd_check_type_int(d, foo, (1, 3))
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)

def bar(a, b, c):
    mgd_check_type_int(b, bar, (1, 1))
    mgd_check_type_int(c, bar, (1, 2))
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)

def baz(a, b):
    mgd_check_type_int(b, baz, (1, 1))
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)

def quux(a):
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()

def qux():
    pass

def test_calls(iterations, timer):
    times = []
    gensym70 = mgd_cast_type_function(xrange, gensym24, '120', gensym25)(iterations)
    for _ in gensym70:
        t0 = mgd_cast_type_function(timer, gensym26, '121', gensym27)()
        foo(mgd_cast_type_dyn(1, gensym28, '123', gensym29), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym30, '124', gensym31), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym32, '125', gensym33), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym34, '126', gensym35), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym36, '127', gensym37), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym38, '128', gensym39), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym40, '129', gensym41), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym42, '130', gensym43), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym44, '131', gensym45), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym46, '132', gensym47), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym48, '133', gensym49), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym50, '134', gensym51), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym52, '135', gensym53), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym54, '136', gensym55), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym56, '137', gensym57), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym58, '138', gensym59), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym60, '139', gensym61), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym62, '140', gensym63), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym64, '141', gensym65), 2, 3, 4)
        foo(mgd_cast_type_dyn(1, gensym66, '142', gensym67), 2, 3, 4)
        t1 = mgd_cast_type_function(timer, gensym68, '143', gensym69)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t1 - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym71, '145', gensym72)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast0(optparse, gensym73, '149', gensym74).OptionParser, gensym75, '149', gensym76)(usage='%prog [options] [test]', description='Test the performance of simple Python-to-Python function calls.')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, _) = mgd_cast_type_tuple(mgd_cast_type_function(cast1(parser, gensym77, '154', gensym78).parse_args, gensym79, '154', gensym80)(), gensym81, '154', gensym82, 2)
    test_calls(mgd_cast_type_dyn(1, gensym85, '157', gensym86), cast2(time, gensym83, '157', gensym84).time)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast3(options, gensym87, '159', gensym88).num_runs, mgd_cast_type_dyn(test_calls, gensym89, '159', gensym90))
