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

def cast2(val, src, b, trg):
    try:
        val.num_runs
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
gensym65 = Function(AnonymousParameters([Int]), Dyn)
gensym47 = Dyn
gensym108 = Dyn
gensym81 = List(Float)
gensym89 = Function(AnonymousParameters([]), Dyn)
gensym113 = Dyn
gensym72 = Dyn
gensym110 = Object('', {'OptionParser': Dyn, })
gensym93 = Function(AnonymousParameters([Int]), Dyn)
gensym17 = Function(NamedParameters([('i_u', Tuple(Float, List(Float)))]), Float)
gensym14 = Dyn
gensym102 = Function(AnonymousParameters([List(Dyn), List(Float)]), Dyn)
gensym97 = List(Dyn)
gensym9 = Function(AnonymousParameters([Dyn]), Dyn)
gensym112 = Function(DynParameters, Dyn)
gensym10 = Tuple(Dyn, List(Float))
gensym18 = Dyn
gensym38 = Function(NamedParameters([('i_u', Tuple(Float, List(Float)))]), Float)
gensym69 = List(Float)
gensym114 = Object('', {'parse_args': Dyn, })
gensym2 = Dyn
gensym6 = Dyn
gensym107 = List(Dyn)
gensym62 = Dyn
gensym76 = Dyn
gensym118 = Tuple(Dyn, Dyn)
gensym11 = Tuple(Float, List(Float))
gensym43 = Dyn
gensym79 = Function(AnonymousParameters([Int]), Dyn)
gensym45 = Dyn
gensym13 = List(Float)
gensym57 = Float
gensym96 = List(Float)
gensym48 = Float
gensym7 = Function(AnonymousParameters([Dyn]), Dyn)
gensym42 = Float
gensym92 = Dyn
gensym90 = List(Int)
gensym39 = Dyn
gensym59 = Function(NamedParameters([('n', Int), ('timer', Dyn)]), Dyn)
gensym122 = Dyn
gensym87 = Function(AnonymousParameters([Int]), Dyn)
gensym1 = Function(NamedParameters([('i', Float), ('j', Float)]), Float)
gensym54 = Float
gensym120 = Object('', {'num_runs': Dyn, })
gensym22 = Dyn
gensym29 = Dyn
gensym88 = Dyn
gensym66 = Dyn
gensym77 = Function(AnonymousParameters([]), Dyn)
gensym44 = Float
gensym83 = Function(AnonymousParameters([List(Dyn), List(Float)]), Dyn)
gensym33 = Float
gensym116 = Function(AnonymousParameters([]), Dyn)
gensym53 = Dyn
gensym26 = Dyn
gensym3 = Function(NamedParameters([('func', Function(AnonymousParameters([Tuple(Float, List(Float))]), Float)), ('u', List(Float))]), List(Float))
gensym24 = Dyn
gensym68 = Dyn
gensym52 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym12 = Dyn
gensym71 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym67 = List(Float)
gensym5 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym63 = Function(AnonymousParameters([]), Dyn)
gensym84 = Dyn
gensym56 = Dyn
gensym115 = Dyn
gensym37 = Dyn
gensym86 = Dyn
gensym21 = Float
gensym117 = Dyn
gensym32 = Dyn
gensym60 = Dyn
gensym46 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym40 = Function(AnonymousParameters([Dyn]), Dyn)
gensym36 = Float
gensym74 = Dyn
gensym91 = List(Dyn)
gensym15 = Function(NamedParameters([('u', List(Float))]), List(Float))
gensym101 = Dyn
gensym104 = Dyn
gensym119 = Dyn
gensym19 = Function(AnonymousParameters([Dyn]), Dyn)
gensym20 = Dyn
gensym35 = Dyn
gensym61 = Function(AnonymousParameters([Int]), Dyn)
gensym30 = Dyn
gensym31 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym28 = Int
gensym27 = Float
gensym4 = Dyn
gensym70 = Dyn
gensym82 = Dyn
gensym8 = Dyn
gensym121 = Function(NamedParameters([('n', Int), ('timer', Dyn)]), Dyn)
gensym23 = Float
gensym64 = Dyn
gensym78 = Dyn
gensym41 = Dyn
gensym95 = List(Float)
gensym75 = Function(AnonymousParameters([Int]), Dyn)
gensym58 = Dyn
gensym99 = Int
gensym111 = Dyn
gensym49 = Int
gensym51 = Dyn
gensym73 = Function(AnonymousParameters([]), Dyn)
gensym25 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym85 = Function(AnonymousParameters([]), Dyn)
gensym105 = Function(AnonymousParameters([]), Dyn)
gensym16 = Dyn
gensym100 = Dyn
gensym50 = Dyn
gensym109 = Dyn
gensym0 = Dyn
gensym80 = List(Dyn)
gensym94 = List(Dyn)
from math import sqrt
import time
import itertools
import optparse
from compat import izip, xrange
import util

def eval_A(i, j):
    mgd_check_type_float(i, eval_A, (1, 0))
    mgd_check_type_float(j, eval_A, (1, 1))
    return (1.0 / (((((i + j) * ((i + j) + 1)) // 2) + i) + 1))

def eval_times_u(func, u):
    mgd_check_type_function(func, eval_times_u, (1, 0))
    mgd_check_type_list(u, eval_times_u, (1, 1))
    return mgd_cast_type_list([mgd_check_type_float(func(mgd_cast_type_tuple((i, u), gensym10, '21', gensym11, 2)), func, 2) for i in mgd_cast_type_function(xrange, gensym8, '21', gensym9)(mgd_cast_type_function(len, gensym6, '21', gensym7)(mgd_cast_type_function(list, gensym4, '21', gensym5)(u)))], gensym12, '21', gensym13)

def eval_AtA_times_u(u):
    mgd_check_type_list(u, eval_AtA_times_u, (1, 0))
    return mgd_check_type_list(eval_times_u(part_At_times_u, mgd_check_type_list(eval_times_u(part_A_times_u, u), eval_times_u, 2)), eval_times_u, 2)

def part_A_times_u(i_u):
    mgd_check_type_tuple(i_u, part_A_times_u, (1, 0), 2)
    (i, u) = i_u
    partial_sum = mgd_cast_type_dyn(0, gensym28, '29', gensym29)
    gensym34 = mgd_cast_type_function(enumerate, gensym30, '30', gensym31)(u)
    for (j, u_j) in gensym34:
        mgd_check_type_tuple((j, u_j), gensym34, 3, 2)
        partial_sum = (partial_sum + (mgd_check_type_float(eval_A(i, mgd_cast_type_float(j, gensym32, '31', gensym33)), eval_A, 2) * u_j))
    return mgd_cast_type_float(partial_sum, gensym35, '32', gensym36)

def part_At_times_u(i_u):
    mgd_check_type_tuple(i_u, part_At_times_u, (1, 0), 2)
    (i, u) = i_u
    partial_sum = mgd_cast_type_dyn(0, gensym49, '36', gensym50)
    gensym55 = mgd_cast_type_function(enumerate, gensym51, '37', gensym52)(u)
    for (j, u_j) in gensym55:
        mgd_check_type_tuple((j, u_j), gensym55, 3, 2)
        partial_sum = (partial_sum + (mgd_check_type_float(eval_A(mgd_cast_type_float(j, gensym53, '38', gensym54), i), eval_A, 2) * u_j))
    return mgd_cast_type_float(partial_sum, gensym56, '39', gensym57)
DEFAULT_N = 130

def main(n, timer):
    mgd_check_type_int(n, main, (1, 0))
    times = []
    gensym106 = mgd_cast_type_function(xrange, gensym86, '45', gensym87)(n)
    for i in gensym106:
        t0 = mgd_cast_type_function(timer, gensym88, '46', gensym89)()
        u = mgd_cast_type_list(([1] * DEFAULT_N), gensym90, '47', gensym91)
        gensym98 = mgd_cast_type_function(xrange, gensym92, '49', gensym93)(10)
        for dummy in gensym98:
            v = mgd_check_type_list(eval_AtA_times_u(mgd_cast_type_list(u, gensym94, '50', gensym95)), eval_AtA_times_u, 2)
            u = mgd_cast_type_list(mgd_check_type_list(eval_AtA_times_u(v), eval_AtA_times_u, 2), gensym96, '51', gensym97)
        vBv = vv = mgd_cast_type_dyn(0, gensym99, '53', gensym100)
        gensym103 = mgd_cast_type_function(izip, gensym101, '55', gensym102)(u, v)
        for (ue, ve) in gensym103:
            mgd_check_type_tuple((ue, ve), gensym103, 3, 2)
            vBv = (vBv + (ue * ve))
            vv = (vv + (ve * ve))
        tk = mgd_cast_type_function(timer, gensym104, '58', gensym105)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((tk - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym107, '60', gensym108)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast0(optparse, gensym109, '63', gensym110).OptionParser, gensym111, '63', gensym112)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast1(parser, gensym113, '67', gensym114).parse_args, gensym115, '67', gensym116)(), gensym117, '67', gensym118, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast2(options, gensym119, '69', gensym120).num_runs, mgd_cast_type_dyn(main, gensym121, '69', gensym122))
