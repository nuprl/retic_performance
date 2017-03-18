from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def cast1(val, src, b, trg):
    try:
        val.islice
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast4(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast0(val, src, b, trg):
    try:
        val.count
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym11 = Function(AnonymousParameters([]), Dyn)
gensym4 = Dyn
gensym56 = Dyn
gensym33 = Function(AnonymousParameters([Function(NamedParameters([('k', Dyn)]), Tuple(Dyn, Dyn, Int, Dyn)), Dyn]), Dyn)
gensym65 = Function(AnonymousParameters([]), Dyn)
gensym38 = Dyn
gensym58 = Dyn
gensym45 = Tuple(Int, Int, Int, Int)
gensym83 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym39 = Function(NamedParameters([]), Dyn)
gensym25 = Object('', {'islice': Dyn, })
gensym41 = Tuple(Int, Int, Int, Int)
gensym66 = Dyn
gensym35 = Function(NamedParameters([('a', Tuple(Int, Int, Int, Int)), ('b', Tuple(Int, Int, Int, Int))]), Tuple(Int, Int, Int, Int))
gensym16 = Dyn
gensym51 = Tuple(Int, Int, Int, Int)
gensym42 = Dyn
gensym60 = Dyn
gensym22 = Dyn
gensym5 = Object('', {'islice': Dyn, })
gensym6 = Dyn
gensym26 = Dyn
gensym81 = Dyn
gensym2 = Dyn
gensym73 = Dyn
gensym80 = Tuple(Dyn, Dyn)
gensym55 = Tuple(Int, Int, Int, Int)
gensym62 = Dyn
gensym64 = Dyn
gensym43 = Tuple(Int, Int, Int, Int)
gensym47 = Tuple(Int, Int, Int, Int)
gensym34 = Dyn
gensym44 = Dyn
gensym0 = Dyn
gensym9 = Function(AnonymousParameters([]), Dyn)
gensym28 = Dyn
gensym78 = Function(AnonymousParameters([]), Dyn)
gensym3 = Object('', {'count': Dyn, })
gensym36 = Dyn
gensym29 = Function(NamedParameters([]), Dyn)
gensym69 = List(Dyn)
gensym72 = Object('', {'OptionParser': Dyn, })
gensym23 = Object('', {'count': Dyn, })
gensym54 = Dyn
gensym8 = Dyn
gensym76 = Object('', {'parse_args': Dyn, })
gensym71 = Dyn
gensym49 = Tuple(Int, Int, Int, Int)
gensym7 = Function(AnonymousParameters([Int]), Dyn)
gensym59 = Function(AnonymousParameters([Dyn]), Dyn)
gensym82 = Object('', {'num_runs': Dyn, })
gensym1 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym32 = Dyn
gensym14 = Dyn
gensym20 = Dyn
gensym84 = Dyn
gensym74 = Function(DynParameters, Dyn)
gensym48 = Tuple(Int, Dyn, Int, Int)
gensym40 = Dyn
gensym63 = Function(AnonymousParameters([Int]), Dyn)
gensym70 = Dyn
gensym77 = Dyn
gensym79 = Dyn
gensym53 = Tuple(Int, Int, Int, Int)
gensym12 = Dyn
gensym50 = Dyn
gensym37 = Function(NamedParameters([('z', Tuple(Int, Int, Int, Int)), ('j', Int)]), Int)
gensym18 = Dyn
gensym17 = Function(AnonymousParameters([Int]), Dyn)
gensym61 = List(Int)
gensym57 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym19 = Function(AnonymousParameters([]), Dyn)
gensym10 = Dyn
gensym75 = Dyn
gensym13 = Object('', {'count': Dyn, })
gensym27 = Function(NamedParameters([('n', Int)]), List(Int))
gensym31 = Function(AnonymousParameters([Int]), Dyn)
gensym46 = Dyn
gensym21 = Function(AnonymousParameters([]), Dyn)
gensym67 = Function(AnonymousParameters([]), Dyn)
gensym30 = Dyn
gensym52 = Dyn
gensym15 = Object('', {'islice': Dyn, })
gensym24 = Dyn
import optparse
import time
import itertools
import util
from compat import xrange, imap, next
NDIGITS = 2000

def test_pidgits(iterations, timer):
    mgd_check_type_int(iterations, test_pidgits, (1, 0))
    _map = imap
    _count = cast0(itertools, gensym22, '21', gensym23).count
    _islice = cast1(itertools, gensym24, '22', gensym25).islice

    def calc_ndigits(n):
        mgd_check_type_int(n, calc_ndigits, (1, 0))

        def gen_x():
            return mgd_cast_type_function(_map, gensym32, '27', gensym33)((lambda k: (k, ((4 * k) + 2), 0, ((2 * k) + 1))), mgd_cast_type_function(_count, gensym30, '27', gensym31)(1))

        def compose(a, b):
            mgd_check_type_tuple(a, compose, (1, 0), 4)
            mgd_check_type_tuple(b, compose, (1, 1), 4)
            (aq, ar, as_, at) = a
            (bq, br, bs, bt) = b
            return ((aq * bq), ((aq * br) + (ar * bt)), ((as_ * bq) + (at * bs)), ((as_ * br) + (at * bt)))

        def extract(z, j):
            mgd_check_type_tuple(z, extract, (1, 0), 4)
            mgd_check_type_int(j, extract, (1, 1))
            (q, r, s, t) = z
            return (((q * j) + r) // ((s * j) + t))

        def pi_digits():
            z = (1, 0, 0, 1)
            x = gen_x()
            while 1:
                y = mgd_check_type_int(extract(z, 3), extract, 2)
                while (y != mgd_check_type_int(extract(z, 4), extract, 2)):
                    z = mgd_check_type_tuple(compose(z, mgd_cast_type_tuple(next(x), gensym54, '47', gensym55, 4)), compose, 2, 4)
                    y = mgd_check_type_int(extract(z, 3), extract, 2)
                z = mgd_check_type_tuple(compose((10, ((- 10) * y), 0, 1), z), compose, 2, 4)
                yield y
        return mgd_cast_type_list(mgd_cast_type_function(list, gensym58, '52', gensym59)(mgd_cast_type_function(_islice, gensym56, '52', gensym57)(pi_digits(), n)), gensym60, '52', gensym61)
    mgd_check_type_list(calc_ndigits(NDIGITS), calc_ndigits, 2)
    mgd_check_type_list(calc_ndigits(NDIGITS), calc_ndigits, 2)
    times = []
    gensym68 = mgd_cast_type_function(xrange, gensym62, '59', gensym63)(iterations)
    for _ in gensym68:
        t0 = mgd_cast_type_function(timer, gensym64, '60', gensym65)()
        mgd_check_type_list(calc_ndigits(NDIGITS), calc_ndigits, 2)
        t1 = mgd_cast_type_function(timer, gensym66, '62', gensym67)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t1 - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym69, '64', gensym70)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast2(optparse, gensym71, '68', gensym72).OptionParser, gensym73, '68', gensym74)(usage='%prog [options]', description='Test the performance of pi calculation.')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast3(parser, gensym75, '72', gensym76).parse_args, gensym77, '72', gensym78)(), gensym79, '72', gensym80, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast4(options, gensym81, '74', gensym82).num_runs, mgd_cast_type_dyn(test_pidgits, gensym83, '74', gensym84))
