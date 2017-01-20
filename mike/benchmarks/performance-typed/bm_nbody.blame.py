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
gensym110 = Function(AnonymousParameters([]), Dyn)
gensym84 = Dyn
gensym92 = Dyn
gensym46 = Dyn
gensym117 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym93 = Function(AnonymousParameters([]), Dyn)
gensym21 = Int
gensym99 = Function(AnonymousParameters([]), Dyn)
gensym5 = Function(AnonymousParameters([Dyn]), Dyn)
gensym85 = Function(AnonymousParameters([]), Dyn)
gensym77 = Function(AnonymousParameters([]), Dyn)
gensym118 = Dyn
gensym87 = Dyn
gensym98 = Dyn
gensym15 = Function(AnonymousParameters([List(Tuple(List(Float), List(Float), Float))]), Dyn)
gensym106 = Function(DynParameters, Dyn)
gensym60 = Float
gensym10 = Dyn
gensym30 = Float
gensym37 = List(Tuple(List(Float), List(Float), Float))
gensym79 = Function(AnonymousParameters([]), Dyn)
gensym96 = Int
gensym94 = Float
gensym66 = Dyn
gensym59 = Dyn
gensym45 = Function(AnonymousParameters([Dyn]), Dyn)
gensym33 = Dict(String, Tuple(List(Float), List(Dyn), Dyn))
gensym114 = Dyn
gensym73 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym34 = Dyn
gensym80 = Dyn
gensym101 = List(Dyn)
gensym55 = Float
gensym35 = Function(AnonymousParameters([Dyn]), Dyn)
gensym6 = Dyn
gensym11 = Function(AnonymousParameters([Dyn]), Dyn)
gensym16 = Dyn
gensym82 = Dyn
gensym88 = Int
gensym3 = Function(AnonymousParameters([List(Tuple(List(Float), List(Float), Float))]), Dyn)
gensym8 = Dyn
gensym64 = Dyn
gensym20 = Dyn
gensym86 = Float
gensym32 = Dict(String, Tuple(List(Float), List(Float), Dyn))
gensym61 = Dyn
gensym89 = Dyn
gensym70 = Dyn
gensym52 = Function(DynParameters, Float)
gensym81 = Function(AnonymousParameters([Int]), Dyn)
gensym44 = Dyn
gensym12 = Dyn
gensym95 = Dyn
gensym2 = Dyn
gensym28 = List(Dyn)
gensym29 = List(Tuple(List(Tuple(List(Float), List(Float), Float)), Tuple(List(Float), List(Float), Float)))
gensym74 = Dyn
gensym47 = Function(AnonymousParameters([Dyn]), Dyn)
gensym39 = Function(DynParameters, Dyn)
gensym42 = Dyn
gensym23 = Dyn
gensym38 = Dyn
gensym109 = Dyn
gensym65 = Float
gensym90 = Dyn
gensym108 = Object('', {'parse_args': Dyn, })
gensym115 = Dyn
gensym1 = Function(NamedParameters([('l', List(Tuple(List(Float), List(Float), Float)))]), List(Tuple(List(Tuple(List(Float), List(Float), Float)), Tuple(List(Float), List(Float), Float))))
gensym102 = Dyn
gensym53 = List(Tuple(List(Tuple(List(Float), List(Float), Float)), Tuple(List(Float), List(Float), Float)))
gensym14 = Dyn
gensym36 = Dyn
gensym83 = Function(AnonymousParameters([]), Dyn)
gensym31 = Dyn
gensym112 = Tuple(Dyn, Dyn)
gensym41 = Dyn
gensym40 = List(Tuple(List(Tuple(List(Float), List(Float), Float)), Tuple(List(Float), List(Float), Float)))
gensym75 = Function(AnonymousParameters([Int]), Dyn)
gensym25 = List(Tuple(List(Float), List(Float), Float))
gensym76 = Dyn
gensym104 = Object('', {'OptionParser': Dyn, })
gensym22 = Tuple(Tuple(List(Float), List(Float), Float), Dyn)
gensym67 = Float
gensym72 = Dyn
gensym116 = Object('', {'num_runs': Dyn, })
gensym13 = Int
gensym17 = Function(AnonymousParameters([Dyn]), Dyn)
gensym91 = Function(AnonymousParameters([Int]), Dyn)
gensym9 = Function(AnonymousParameters([List(Tuple(List(Float), List(Float), Float))]), Dyn)
gensym4 = Dyn
gensym51 = Dyn
gensym56 = Dyn
gensym62 = Function(DynParameters, Dyn)
gensym43 = Function(AnonymousParameters([Dyn]), Dyn)
gensym111 = Dyn
gensym26 = List(Dyn)
gensym107 = Dyn
gensym0 = Dyn
gensym113 = Tuple(List(Float), List(Dyn), Dyn)
gensym7 = Int
gensym19 = Int
gensym78 = Dyn
gensym63 = Float
gensym68 = Dyn
gensym71 = Tuple(Dyn, Dyn, Dyn)
gensym18 = Dyn
gensym97 = Dyn
gensym105 = Dyn
gensym103 = Dyn
gensym54 = Dyn
__contact__ = 'collinwinter@google.com (Collin Winter)'
import optparse
import sys
import time
import util
from compat import xrange

def combinations(l):
    mgd_check_type_list(l, combinations, (1, 0))
    result = []
    gensym27 = mgd_cast_type_function(xrange, gensym16, '31', gensym17)((mgd_cast_type_function(len, gensym14, '31', gensym15)(l) - 1))
    for x in gensym27:
        ls = mgd_check_type_list(l[mgd_cast_type_int((x + 1), gensym18, '32', gensym19):], l, 3)
        gensym24 = mgd_cast_type_list(ls, gensym25, '33', gensym26)
        for y in gensym24:
            mgd_check_type_void(mgd_check_type_function(result.append, result, (0, 'append'))(mgd_cast_type_dyn((mgd_check_type_tuple(l[mgd_cast_type_int(x, gensym20, '34', gensym21)], l, 3, 3), y), gensym22, '34', gensym23)), mgd_check_type_function(result.append, result, (0, 'append')), 2)
    return mgd_cast_type_list(result, gensym28, '35', gensym29)
PI = 3.141592653589793
SOLAR_MASS = mgd_cast_type_dyn(((4 * PI) * PI), gensym30, '39', gensym31)
DAYS_PER_YEAR = 365.24
BODIES = mgd_cast_type_dict({'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS), 'jupiter': ([4.841431442464721, (- 1.1603200440274284), (- 0.10362204447112311)], [(0.001660076642744037 * DAYS_PER_YEAR), (0.007699011184197404 * DAYS_PER_YEAR), ((- 6.90460016972063e-05) * DAYS_PER_YEAR)], (0.0009547919384243266 * SOLAR_MASS)), 'saturn': ([8.34336671824458, 4.124798564124305, (- 0.4035234171143214)], [((- 0.002767425107268624) * DAYS_PER_YEAR), (0.004998528012349172 * DAYS_PER_YEAR), (2.3041729757376393e-05 * DAYS_PER_YEAR)], (0.0002858859806661308 * SOLAR_MASS)), 'uranus': ([12.894369562139131, (- 15.111151401698631), (- 0.22330757889265573)], [(0.002964601375647616 * DAYS_PER_YEAR), (0.0023784717395948095 * DAYS_PER_YEAR), ((- 2.9658956854023756e-05) * DAYS_PER_YEAR)], (4.366244043351563e-05 * SOLAR_MASS)), 'neptune': ([15.379697114850917, (- 25.919314609987964), 0.17925877295037118], [(0.0026806777249038932 * DAYS_PER_YEAR), (0.001628241700382423 * DAYS_PER_YEAR), ((- 9.515922545197159e-05) * DAYS_PER_YEAR)], (5.1513890204661145e-05 * SOLAR_MASS)), }, gensym32, '42', gensym33)
SYSTEM = mgd_cast_type_function(list, gensym34, '78', gensym35)(mgd_check_type_function(BODIES.values, BODIES, (0, 'values'))())
PAIRS = mgd_check_type_list(combinations(mgd_cast_type_list(SYSTEM, gensym36, '79', gensym37)), combinations, 2)

def advance(dt, n, bodies=SYSTEM, pairs=mgd_cast_type_dyn(PAIRS, gensym40, '82', gensym41)):
    gensym50 = mgd_cast_type_function(xrange, gensym46, '83', gensym47)(n)
    for i in gensym50:
        gensym48 = pairs
        for (([x1, y1, z1], v1, m1), ([x2, y2, z2], v2, m2)) in gensym48:
            mgd_check_type_tuple((([x1, y1, z1], v1, m1), ([x2, y2, z2], v2, m2)), gensym48, 3, 2)
            dx = (x1 - x2)
            dy = (y1 - y2)
            dz = (z1 - z2)
            mag = (dt * ((((dx * dx) + (dy * dy)) + (dz * dz)) ** (- 1.5)))
            b1m = (m1 * mag)
            b2m = (m2 * mag)
            v1[0] = (v1[0] - (dx * b2m))
            v1[1] = (v1[1] - (dy * b2m))
            v1[2] = (v1[2] - (dz * b2m))
            v2[0] = (v2[0] + (dx * b1m))
            v2[1] = (v2[1] + (dy * b1m))
            v2[2] = (v2[2] + (dz * b1m))
        gensym49 = bodies
        for (r, [vx, vy, vz], m) in gensym49:
            mgd_check_type_tuple((r, [vx, vy, vz], m), gensym49, 3, 3)
            r[0] = (r[0] + (dt * vx))
            r[1] = (r[1] + (dt * vy))
            r[2] = (r[2] + (dt * vz))

def report_energy(bodies=SYSTEM, pairs=mgd_cast_type_dyn(PAIRS, gensym53, '104', gensym54), e=mgd_cast_type_dyn(0.0, gensym55, '104', gensym56)):
    gensym57 = pairs
    for (((x1, y1, z1), v1, m1), ((x2, y2, z2), v2, m2)) in gensym57:
        mgd_check_type_tuple((((x1, y1, z1), v1, m1), ((x2, y2, z2), v2, m2)), gensym57, 3, 2)
        dx = (x1 - x2)
        dy = (y1 - y2)
        dz = (z1 - z2)
        e = (e - ((m1 * m2) / ((((dx * dx) + (dy * dy)) + (dz * dz)) ** 0.5)))
    gensym58 = bodies
    for (r, [vx, vy, vz], m) in gensym58:
        mgd_check_type_tuple((r, [vx, vy, vz], m), gensym58, 3, 3)
        e = (e + ((m * (((vx * vx) + (vy * vy)) + (vz * vz))) / 2.0))
    return mgd_cast_type_float(e, gensym59, '113', gensym60)

def offset_momentum(ref, bodies=SYSTEM, px=mgd_cast_type_dyn(0.0, gensym63, '116', gensym64), py=mgd_cast_type_dyn(0.0, gensym65, '116', gensym66), pz=mgd_cast_type_dyn(0.0, gensym67, '116', gensym68)):
    gensym69 = bodies
    for (r, [vx, vy, vz], m) in gensym69:
        mgd_check_type_tuple((r, [vx, vy, vz], m), gensym69, 3, 3)
        px = (px - (vx * m))
        py = (py - (vy * m))
        pz = (pz - (vz * m))
    (r, v, m) = mgd_cast_type_tuple(ref, gensym70, '121', gensym71, 3)
    v[0] = (px / m)
    v[1] = (py / m)
    v[2] = (pz / m)

def test_nbody(iterations, timer):
    mgd_check_type_int(iterations, test_nbody, (1, 0))
    mgd_check_type_float(report_energy(), report_energy, 2)
    advance(mgd_cast_type_dyn(0.01, gensym86, '130', gensym87), mgd_cast_type_dyn(20000, gensym88, '130', gensym89))
    mgd_check_type_float(report_energy(), report_energy, 2)
    times = []
    gensym100 = mgd_cast_type_function(xrange, gensym90, '134', gensym91)(iterations)
    for _ in gensym100:
        t0 = mgd_cast_type_function(timer, gensym92, '135', gensym93)()
        mgd_check_type_float(report_energy(), report_energy, 2)
        advance(mgd_cast_type_dyn(0.01, gensym94, '137', gensym95), mgd_cast_type_dyn(20000, gensym96, '137', gensym97))
        mgd_check_type_float(report_energy(), report_energy, 2)
        t1 = mgd_cast_type_function(timer, gensym98, '139', gensym99)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t1 - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym101, '141', gensym102)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast0(optparse, gensym103, '145', gensym104).OptionParser, gensym105, '145', gensym106)(usage='%prog [options]', description='Run the n-body benchmark.')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast1(parser, gensym107, '149', gensym108).parse_args, gensym109, '149', gensym110)(), gensym111, '149', gensym112, 2)
    offset_momentum(mgd_cast_type_dyn(mgd_check_type_tuple(BODIES['sun'], BODIES, 3, 3), gensym113, '151', gensym114))
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast2(options, gensym115, '152', gensym116).num_runs, mgd_cast_type_dyn(test_nbody, gensym117, '152', gensym118))
