from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def cast1(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast0(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym10 = Dyn
gensym66 = Function(AnonymousParameters([Dyn]), Dyn)
gensym32 = Dyn
gensym43 = Function(AnonymousParameters([Dyn]), Dyn)
gensym108 = Object('', {'parse_args': Dyn, })
gensym57 = Dyn
gensym35 = Function(AnonymousParameters([Dyn]), Dyn)
gensym0 = Dyn
gensym80 = Dyn
gensym23 = Function(AnonymousParameters([Dyn]), Dyn)
gensym95 = Function(AnonymousParameters([]), Dyn)
gensym4 = Dyn
gensym5 = Function(AnonymousParameters([Dyn]), Dyn)
gensym51 = Function(AnonymousParameters([Dyn]), Dyn)
gensym115 = Function(NamedParameters([('iterations', Dyn), ('timer', Dyn)]), Dyn)
gensym40 = Dyn
gensym14 = Dyn
gensym97 = Function(AnonymousParameters([Dyn]), Dyn)
gensym22 = Dyn
gensym106 = Function(DynParameters, Dyn)
gensym63 = Dyn
gensym15 = Function(AnonymousParameters([Dyn]), Dyn)
gensym52 = Dyn
gensym25 = Function(AnonymousParameters([Dyn]), Dyn)
gensym30 = Dyn
gensym90 = Dyn
gensym18 = Dyn
gensym49 = Function(AnonymousParameters([Dyn]), Dyn)
gensym9 = Function(AnonymousParameters([Dyn]), Dyn)
gensym89 = Function(AnonymousParameters([Dyn]), Dyn)
gensym87 = Function(AnonymousParameters([]), Dyn)
gensym59 = Dyn
gensym61 = Dyn
gensym55 = Function(AnonymousParameters([Dyn]), Dyn)
gensym64 = Function(AnonymousParameters([Int]), Dyn)
gensym29 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym46 = Dyn
gensym68 = Function(AnonymousParameters([Dyn]), Dyn)
gensym72 = Function(AnonymousParameters([Dyn]), Dyn)
gensym110 = Function(AnonymousParameters([]), Dyn)
gensym39 = Function(AnonymousParameters([Dyn]), Dyn)
gensym12 = Dyn
gensym58 = Function(NamedParameters([('queen_count', Int)]), Dyn)
gensym16 = Dyn
gensym6 = Dyn
gensym19 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1 = Function(DynParameters, Dyn)
gensym34 = Dyn
gensym60 = Function(AnonymousParameters([Int]), Dyn)
gensym105 = Dyn
gensym102 = Dyn
gensym82 = Dyn
gensym53 = Function(AnonymousParameters([Dyn]), Dyn)
gensym91 = Function(AnonymousParameters([Dyn]), Dyn)
gensym27 = Function(AnonymousParameters([Dyn]), Dyn)
gensym77 = Function(AnonymousParameters([Dyn]), Dyn)
gensym71 = Dyn
gensym84 = Dyn
gensym36 = Dyn
gensym112 = Tuple(Dyn, Dyn)
gensym3 = Dyn
gensym99 = Function(AnonymousParameters([]), Dyn)
gensym92 = Dyn
gensym111 = Dyn
gensym69 = Dyn
gensym74 = Dyn
gensym47 = Function(AnonymousParameters([Dyn]), Dyn)
gensym20 = Dyn
gensym26 = Dyn
gensym107 = Dyn
gensym28 = Dyn
gensym113 = Dyn
gensym83 = Function(AnonymousParameters([Dyn]), Dyn)
gensym11 = Function(AnonymousParameters([Dyn]), Dyn)
gensym96 = Dyn
gensym81 = Function(AnonymousParameters([]), Dyn)
gensym98 = Dyn
gensym41 = Function(AnonymousParameters([Dyn]), Dyn)
gensym13 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym24 = Dyn
gensym79 = Function(AnonymousParameters([]), Dyn)
gensym76 = Dyn
gensym17 = Function(AnonymousParameters([Dyn]), Dyn)
gensym50 = Dyn
gensym44 = Dyn
gensym86 = Dyn
gensym109 = Dyn
gensym62 = Function(AnonymousParameters([Int]), Dyn)
gensym67 = Dyn
gensym2 = Void
gensym31 = Function(AnonymousParameters([Dyn]), Dyn)
gensym93 = Function(AnonymousParameters([Dyn]), Dyn)
gensym78 = Dyn
gensym94 = Dyn
gensym103 = Dyn
gensym21 = Function(AnonymousParameters([Dyn]), Dyn)
gensym65 = Dyn
gensym88 = Dyn
gensym8 = Dyn
gensym114 = Object('', {'num_runs': Dyn, })
gensym75 = Function(NamedParameters([('iterations', Dyn), ('timer', Dyn)]), Dyn)
gensym37 = Function(AnonymousParameters([Dyn]), Dyn)
gensym45 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym33 = Function(AnonymousParameters([Dyn]), Dyn)
gensym116 = Dyn
gensym7 = Function(AnonymousParameters([Dyn]), Dyn)
gensym38 = Dyn
gensym54 = Dyn
gensym104 = Object('', {'OptionParser': Dyn, })
gensym48 = Dyn
gensym42 = Dyn
gensym70 = Function(AnonymousParameters([Dyn]), Dyn)
gensym101 = List(Dyn)
gensym85 = Function(AnonymousParameters([]), Dyn)
__author__ = 'collinwinter@google.com (Collin Winter)'
import optparse
import re
import string
import time
import util
from compat import xrange

def permutations(iterable, r=mgd_cast_type_dyn(None, gensym2, '19', gensym3)):
    pool = mgd_cast_type_function(tuple, gensym36, '21', gensym37)(iterable)
    n = mgd_cast_type_function(len, gensym38, '22', gensym39)(pool)
    if (r is None):
        r = n
    indices = mgd_cast_type_function(list, gensym42, '25', gensym43)(mgd_cast_type_function(range, gensym40, '25', gensym41)(n))
    cycles = mgd_cast_type_function(list, gensym46, '26', gensym47)(mgd_cast_type_function(range, gensym44, '26', gensym45)(((n - r) + 1), (n + 1)))[::(- 1)]
    yield mgd_cast_type_function(tuple, gensym48, '27', gensym49)((pool[i] for i in indices[:r]))
    while n:
        gensym56 = mgd_cast_type_function(reversed, gensym52, '29', gensym53)(mgd_cast_type_function(range, gensym50, '29', gensym51)(r))
        for i in gensym56:
            cycles[i] = (cycles[i] - 1)
            if (cycles[i] == 0):
                indices[i:] = (indices[(i + 1):] + indices[i:(i + 1)])
                cycles[i] = (n - i)
            else:
                j = cycles[i]
                (indices[i], indices[(- j)]) = (indices[(- j)], indices[i])
                yield mgd_cast_type_function(tuple, gensym54, '37', gensym55)((pool[i] for i in indices[:r]))
                break
        else:
            return

def n_queens(queen_count):
    mgd_check_type_int(queen_count, n_queens, (1, 0))
    cols = mgd_cast_type_function(range, gensym63, '56', gensym64)(queen_count)
    gensym73 = permutations(cols)
    for vec in gensym73:
        if (queen_count == mgd_cast_type_function(len, gensym67, '58', gensym68)(mgd_cast_type_function(set, gensym65, '58', gensym66)(((vec[i] + i) for i in cols))) == mgd_cast_type_function(len, gensym71, '59', gensym72)(mgd_cast_type_function(set, gensym69, '59', gensym70)(((vec[i] - i) for i in cols)))):
            yield vec

def test_n_queens(iterations, timer):
    mgd_cast_type_function(list, gensym88, '65', gensym89)(n_queens(8))
    mgd_cast_type_function(list, gensym90, '66', gensym91)(n_queens(8))
    times = []
    gensym100 = mgd_cast_type_function(xrange, gensym92, '69', gensym93)(iterations)
    for _ in gensym100:
        t0 = mgd_cast_type_function(timer, gensym94, '70', gensym95)()
        mgd_cast_type_function(list, gensym96, '71', gensym97)(n_queens(8))
        t1 = mgd_cast_type_function(timer, gensym98, '72', gensym99)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t1 - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym101, '74', gensym102)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast0(optparse, gensym103, '78', gensym104).OptionParser, gensym105, '78', gensym106)(usage='%prog [options]', description='Test the performance of an N-Queens solvers.')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast1(parser, gensym107, '82', gensym108).parse_args, gensym109, '82', gensym110)(), gensym111, '82', gensym112, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast2(options, gensym113, '84', gensym114).num_runs, mgd_cast_type_dyn(test_n_queens, gensym115, '84', gensym116))
