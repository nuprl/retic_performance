from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def cast4(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast0(val, src, b, trg):
    try:
        val.insert
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

def cast2(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast1(val, src, b, trg):
    try:
        val.pop
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym13 = Function(AnonymousParameters([Dyn]), Dyn)
gensym34 = Dyn
gensym20 = Dyn
gensym50 = Dyn
gensym33 = Object('', {'pop': Dyn, })
gensym88 = Object('', {'OptionParser': Dyn, })
gensym18 = Dyn
gensym96 = Tuple(Dyn, Dyn)
gensym60 = Dyn
gensym91 = Dyn
gensym92 = Object('', {'parse_args': Dyn, })
gensym40 = Int
gensym37 = Function(AnonymousParameters([Dyn]), Dyn)
gensym63 = Int
gensym85 = List(Dyn)
gensym62 = Dyn
gensym98 = Object('', {'num_runs': Dyn, })
gensym25 = Function(AnonymousParameters([Dyn]), Dyn)
gensym78 = Dyn
gensym19 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym52 = Dyn
gensym10 = Dyn
gensym35 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym30 = Dyn
gensym69 = Function(AnonymousParameters([]), Dyn)
gensym49 = Function(AnonymousParameters([Int]), Dyn)
gensym64 = Dyn
gensym2 = Dyn
gensym26 = Dyn
gensym43 = Dyn
gensym76 = Dyn
gensym11 = Function(AnonymousParameters([Int]), Dyn)
gensym61 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym83 = Function(AnonymousParameters([]), Dyn)
gensym54 = Dyn
gensym67 = Function(AnonymousParameters([Dyn]), Dyn)
gensym55 = Object('', {'pop': Dyn, })
gensym31 = Object('', {'insert': Dyn, })
gensym74 = Dyn
gensym58 = Dyn
gensym12 = Dyn
gensym46 = Dyn
gensym17 = Object('', {'pop': Dyn, })
gensym21 = Function(AnonymousParameters([Dyn]), Dyn)
gensym16 = Dyn
gensym93 = Dyn
gensym39 = Dyn
gensym73 = Function(AnonymousParameters([Dyn]), Dyn)
gensym27 = Function(AnonymousParameters([Int]), Dyn)
gensym45 = Function(AnonymousParameters([Int]), Dyn)
gensym22 = Dyn
gensym44 = Dyn
gensym53 = Object('', {'insert': Dyn, })
gensym15 = Object('', {'insert': Dyn, })
gensym86 = Dyn
gensym8 = Dyn
gensym66 = Dyn
gensym32 = Dyn
gensym29 = Function(AnonymousParameters([Dyn]), Dyn)
gensym48 = Dyn
gensym36 = Dyn
gensym77 = Function(AnonymousParameters([]), Dyn)
gensym70 = Dyn
gensym89 = Dyn
gensym23 = Function(AnonymousParameters([Int]), Dyn)
gensym14 = Dyn
gensym82 = Dyn
gensym97 = Dyn
gensym9 = Function(AnonymousParameters([Dyn]), Dyn)
gensym87 = Dyn
gensym28 = Dyn
gensym56 = Int
gensym72 = Dyn
gensym24 = Dyn
gensym65 = Function(NamedParameters([('n', Dyn), ('timer', Dyn)]), Dyn)
gensym47 = Function(AnonymousParameters([Dyn]), Dyn)
gensym100 = Dyn
gensym3 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym7 = Function(AnonymousParameters([Int]), Dyn)
gensym80 = Dyn
gensym41 = Dyn
gensym90 = Function(DynParameters, Dyn)
gensym51 = Function(AnonymousParameters([Dyn]), Dyn)
gensym75 = Function(AnonymousParameters([]), Dyn)
gensym6 = Dyn
gensym59 = Function(AnonymousParameters([Int]), Dyn)
gensym38 = Int
gensym57 = Dyn
gensym71 = Function(AnonymousParameters([]), Dyn)
gensym0 = Dyn
gensym68 = Dyn
gensym81 = Function(AnonymousParameters([]), Dyn)
gensym1 = Function(NamedParameters([('n', Int)]), Int)
gensym42 = Int
gensym5 = Function(AnonymousParameters([Dyn]), Dyn)
gensym79 = Function(AnonymousParameters([Dyn]), Dyn)
gensym95 = Dyn
gensym4 = Dyn
gensym99 = Function(NamedParameters([('n', Dyn), ('timer', Dyn)]), Dyn)
gensym94 = Function(AnonymousParameters([]), Dyn)
import optparse
import time
import util
from compat import xrange

def fannkuch(n):
    mgd_check_type_int(n, fannkuch, (1, 0))
    count = mgd_cast_type_function(list, gensym36, '15', gensym37)(mgd_cast_type_function(range, gensym34, '15', gensym35)(1, (n + 1)))
    max_flips = mgd_cast_type_dyn(0, gensym38, '16', gensym39)
    m = (n - 1)
    r = mgd_cast_type_dyn(n, gensym40, '18', gensym41)
    check = mgd_cast_type_dyn(0, gensym42, '19', gensym43)
    perm1 = mgd_cast_type_function(list, gensym46, '20', gensym47)(mgd_cast_type_function(range, gensym44, '20', gensym45)(n))
    perm = mgd_cast_type_function(list, gensym50, '21', gensym51)(mgd_cast_type_function(range, gensym48, '21', gensym49)(n))
    perm1_ins = cast0(perm1, gensym52, '22', gensym53).insert
    perm1_pop = cast1(perm1, gensym54, '23', gensym55).pop
    while 1:
        if (check < 30):
            check = (check + 1)
        while (r != 1):
            count[(r - 1)] = r
            r = (r - 1)
        if ((perm1[0] != 0) and (perm1[m] != m)):
            perm = perm1[:]
            flips_count = mgd_cast_type_dyn(0, gensym56, '36', gensym57)
            k = perm[0]
            while k:
                perm[:(k + 1)] = perm[k::(- 1)]
                flips_count = (flips_count + 1)
                k = perm[0]
            if (flips_count > max_flips):
                max_flips = flips_count
        while (r != n):
            mgd_cast_type_function(perm1_ins, gensym60, '47', gensym61)(r, mgd_cast_type_function(perm1_pop, gensym58, '47', gensym59)(0))
            count[r] = (count[r] - 1)
            if (count[r] > 0):
                break
            r = (r + 1)
        else:
            return mgd_cast_type_int(max_flips, gensym62, '53', gensym63)
    return (- 1)
DEFAULT_ARG = 9

def main(n, timer):
    times = []
    gensym84 = mgd_cast_type_function(xrange, gensym78, '60', gensym79)(n)
    for i in gensym84:
        t0 = mgd_cast_type_function(timer, gensym80, '61', gensym81)()
        mgd_check_type_int(fannkuch(DEFAULT_ARG), fannkuch, 2)
        tk = mgd_cast_type_function(timer, gensym82, '63', gensym83)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((tk - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym85, '65', gensym86)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast2(optparse, gensym87, '68', gensym88).OptionParser, gensym89, '68', gensym90)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast3(parser, gensym91, '72', gensym92).parse_args, gensym93, '72', gensym94)(), gensym95, '72', gensym96, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast4(options, gensym97, '74', gensym98).num_runs, mgd_cast_type_dyn(main, gensym99, '74', gensym100))
