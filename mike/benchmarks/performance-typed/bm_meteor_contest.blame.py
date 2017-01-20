from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def cast0(val, src, b, trg):
    try:
        val.append
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast1(val, src, b, trg):
    try:
        val.remove
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast5(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.insert
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast4(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym118 = List(Int)
gensym211 = Dyn
gensym143 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym36 = Dyn
gensym19 = List(Float)
gensym44 = Function(AnonymousParameters([Dyn]), Dyn)
gensym382 = Object('', {'parse_args': Dyn, })
gensym367 = Dyn
gensym90 = List(List(Dyn))
gensym303 = Dyn
gensym97 = Dyn
gensym94 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym384 = Function(AnonymousParameters([]), Dyn)
gensym67 = Dyn
gensym235 = Dyn
gensym93 = Dyn
gensym141 = List(Int)
gensym365 = Function(AnonymousParameters([Dyn]), Dyn)
gensym370 = List(Dyn)
gensym39 = Function(AnonymousParameters([Dyn]), Dyn)
gensym360 = Dyn
gensym180 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym9 = List(Dyn)
gensym328 = Dyn
gensym375 = List(Dyn)
gensym239 = Dyn
gensym26 = Dyn
gensym151 = Int
gensym42 = Object('', {'append': Dyn, })
gensym387 = Dyn
gensym156 = Function(AnonymousParameters([Dyn]), Dyn)
gensym280 = Dyn
gensym182 = Function(AnonymousParameters([Dyn]), Dyn)
gensym127 = Dyn
gensym49 = List(Float)
gensym134 = Dyn
gensym249 = Function(AnonymousParameters([String]), Dyn)
gensym165 = Dyn
gensym128 = Int
gensym58 = List(Float)
gensym66 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym222 = List(List(Float))
gensym140 = Dyn
gensym122 = Function(AnonymousParameters([Dyn]), Dyn)
gensym104 = Function(AnonymousParameters([Dyn]), Dyn)
gensym38 = Dyn
gensym250 = Dyn
gensym175 = Dyn
gensym191 = List(Dyn)
gensym164 = Int
gensym351 = Function(AnonymousParameters([]), Dyn)
gensym171 = Dyn
gensym286 = Dyn
gensym30 = List(Dyn)
gensym266 = Function(AnonymousParameters([Dyn]), Dyn)
gensym318 = Dyn
gensym255 = Dyn
gensym8 = Dyn
gensym162 = Function(AnonymousParameters([Dyn]), Dyn)
gensym298 = Dyn
gensym256 = Function(DynParameters, Void)
gensym173 = Dyn
gensym212 = Function(AnonymousParameters([Dyn]), Dyn)
gensym73 = Dyn
gensym65 = Dyn
gensym68 = Function(AnonymousParameters([Dyn]), Dyn)
gensym240 = Function(AnonymousParameters([Dyn]), Dyn)
gensym172 = List(List(List(Float)))
gensym299 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym76 = Float
gensym146 = List(Set(List(Int)))
gensym95 = Dyn
gensym132 = List(List(List(Dyn)))
gensym158 = List(Dyn)
gensym242 = Function(AnonymousParameters([Dyn]), Dyn)
gensym366 = Int
gensym1 = Tuple(Dyn, Int)
gensym0 = Tuple(Int, Int)
gensym210 = Int
gensym28 = Dyn
gensym319 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym55 = Dyn
gensym290 = Dyn
gensym274 = Dyn
gensym311 = Function(AnonymousParameters([]), Dyn)
gensym63 = Dyn
gensym103 = Dyn
gensym264 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym307 = Function(NamedParameters([('n', Int), ('timer', Dyn)]), Dyn)
gensym258 = Dyn
gensym361 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym269 = Dyn
gensym363 = Function(AnonymousParameters([Dyn]), Dyn)
gensym385 = Dyn
gensym209 = Dyn
gensym208 = Function(AnonymousParameters([Dyn]), Dyn)
gensym270 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym70 = List(List(Dyn))
gensym199 = Dyn
gensym120 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym314 = Dyn
gensym82 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym189 = List(Dyn)
gensym207 = Dyn
gensym135 = Function(NamedParameters([('board', List(Float)), ('cti', Dict(Float, Int))]), List(Set(List(Int))))
gensym178 = List(Dyn)
gensym174 = Function(AnonymousParameters([Dyn]), Dyn)
gensym46 = Function(AnonymousParameters([Dyn]), Dyn)
gensym7 = Dyn
gensym223 = Dyn
gensym245 = Dyn
gensym160 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym16 = Dyn
gensym168 = List(Float)
gensym304 = Function(AnonymousParameters([Dyn]), Dyn)
gensym3 = Tuple(Dyn, Dyn, Dyn)
gensym224 = List(List(List(Float)))
gensym301 = Function(AnonymousParameters([Dyn]), Dyn)
gensym213 = List(List(Dyn))
gensym108 = Function(AnonymousParameters([Dyn]), Dyn)
gensym237 = Dyn
gensym179 = Dyn
gensym113 = Dyn
gensym325 = Function(AnonymousParameters([Dyn]), Dyn)
gensym354 = Dyn
gensym34 = Dyn
gensym123 = Dyn
gensym309 = Function(AnonymousParameters([Int]), Dyn)
gensym355 = Function(AnonymousParameters([Dyn]), Dyn)
gensym357 = Function(AnonymousParameters([Dyn]), Dyn)
gensym14 = Dict(Dyn, Dyn)
gensym313 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym64 = Function(AnonymousParameters([Dyn]), Dyn)
gensym203 = Dyn
gensym152 = Dyn
gensym24 = Function(DynParameters, List(Float))
gensym105 = Dyn
gensym184 = Int
gensym181 = Dyn
gensym379 = Dyn
gensym112 = List(List(List(Dyn)))
gensym358 = Dyn
gensym310 = Dyn
gensym192 = Dyn
gensym284 = Dyn
gensym187 = List(List(Dyn))
gensym33 = Function(AnonymousParameters([Int]), Dyn)
gensym69 = Dyn
gensym20 = Dyn
gensym261 = Dyn
gensym183 = Dyn
gensym219 = Dyn
gensym50 = Dyn
gensym117 = Dyn
gensym268 = Function(AnonymousParameters([Dyn]), Dyn)
gensym322 = Dyn
gensym321 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym111 = Dyn
gensym300 = Dyn
gensym136 = List(Dyn)
gensym170 = List(List(Float))
gensym177 = Dyn
gensym116 = Float
gensym5 = Function(DynParameters, List(Float))
gensym326 = Dyn
gensym369 = Dyn
gensym51 = Function(NamedParameters([('ido', List(Float))]), List(Float))
gensym295 = Object('', {'insert': Dyn, })
gensym232 = Dyn
gensym197 = Dyn
gensym236 = Function(AnonymousParameters([Dyn]), Dyn)
gensym56 = Function(AnonymousParameters([Dyn]), Dyn)
gensym10 = List(Dyn)
gensym336 = Dyn
gensym233 = Dyn
gensym327 = Function(AnonymousParameters([]), Dyn)
gensym139 = Float
gensym91 = Dyn
gensym60 = Function(NamedParameters([('board', List(Float)), ('cti', Dict(Float, Int)), ('pieces', List(List(List(Float))))]), List(List(List(Set(List(Int))))))
gensym163 = Dyn
gensym142 = Dyn
gensym79 = Dyn
gensym292 = Dyn
gensym329 = Function(AnonymousParameters([Int]), Dyn)
gensym149 = Int
gensym337 = Function(AnonymousParameters([Dyn]), Dyn)
gensym194 = List(Float)
gensym263 = Dyn
gensym371 = Dyn
gensym196 = List(List(Float))
gensym29 = Function(AnonymousParameters([Int]), Dyn)
gensym11 = List(Float)
gensym390 = Dyn
gensym121 = Dyn
gensym248 = Dyn
gensym216 = Dyn
gensym157 = Dyn
gensym338 = Dyn
gensym341 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym288 = Dyn
gensym198 = List(List(List(Float)))
gensym234 = Function(AnonymousParameters([Dyn]), Dyn)
gensym86 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym133 = List(List(List(Set(List(Int)))))
gensym377 = Dyn
gensym96 = Float
gensym271 = Dyn
gensym214 = Dyn
gensym4 = Dyn
gensym150 = Dyn
gensym376 = Dyn
gensym147 = Dyn
gensym205 = Dyn
gensym71 = Dyn
gensym294 = Dyn
gensym148 = Function(DynParameters, Tuple(List(Float), Dict(Float, Int), List(List(List(Float)))))
gensym289 = Object('', {'insert': Dyn, })
gensym106 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym57 = Dyn
gensym72 = List(List(List(Dyn)))
gensym87 = Dyn
gensym364 = Dyn
gensym62 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym231 = Int
gensym59 = Dyn
gensym265 = Dyn
gensym161 = Dyn
gensym89 = Dyn
gensym31 = Dyn
gensym100 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym331 = Function(AnonymousParameters([]), Dyn)
gensym285 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym138 = Dyn
gensym306 = Dyn
gensym53 = Dyn
gensym297 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym282 = Dyn
gensym22 = Function(DynParameters, List(Float))
gensym349 = Function(AnonymousParameters([Int]), Dyn)
gensym88 = Function(AnonymousParameters([Dyn]), Dyn)
gensym101 = Dyn
gensym43 = Dyn
gensym388 = Object('', {'num_runs': Dyn, })
gensym281 = Object('', {'remove': Dyn, })
gensym13 = Function(DynParameters, List(Float))
gensym380 = Function(DynParameters, Dyn)
gensym276 = Dyn
gensym353 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym227 = Dyn
gensym84 = Function(AnonymousParameters([Dyn]), Dyn)
gensym362 = Dyn
gensym202 = Function(AnonymousParameters([Dyn]), Dyn)
gensym15 = Dyn
gensym153 = Dyn
gensym356 = Dyn
gensym6 = Dict(Dyn, Dyn)
gensym359 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym324 = Dyn
gensym37 = Function(AnonymousParameters([Dyn]), Dyn)
gensym312 = Dyn
gensym126 = Int
gensym320 = Dyn
gensym41 = Dyn
gensym18 = List(Dyn)
gensym218 = Dyn
gensym75 = Dyn
gensym296 = Dyn
gensym260 = Dyn
gensym201 = Dyn
gensym115 = Dyn
gensym200 = Function(AnonymousParameters([Dyn]), Dyn)
gensym125 = Dyn
gensym272 = Function(AnonymousParameters([Dyn]), Dyn)
gensym241 = Dyn
gensym185 = Dyn
gensym114 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym230 = Dyn
gensym378 = Object('', {'OptionParser': Dyn, })
gensym251 = Function(AnonymousParameters([String]), Dyn)
gensym45 = Dyn
gensym221 = Dyn
gensym332 = Dyn
gensym277 = Function(AnonymousParameters([Dyn]), Dyn)
gensym315 = Function(AnonymousParameters([Dyn]), Dyn)
gensym308 = Dyn
gensym206 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym74 = Function(AnonymousParameters([List(List(List(Float)))]), Dyn)
gensym254 = Function(AnonymousParameters([]), Dyn)
gensym102 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym238 = Function(AnonymousParameters([Dyn]), Dyn)
gensym137 = Dyn
gensym215 = List(Dyn)
gensym107 = Dyn
gensym21 = Function(DynParameters, List(Float))
gensym334 = Dyn
gensym283 = Function(AnonymousParameters([Dyn]), Dyn)
gensym98 = List(Int)
gensym291 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym204 = List(Dyn)
gensym54 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym169 = Dyn
gensym368 = Int
gensym25 = Dyn
gensym220 = List(Float)
gensym340 = Dyn
gensym339 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym262 = Function(AnonymousParameters([Dyn]), Dyn)
gensym83 = Dyn
gensym228 = Function(DynParameters, Dyn)
gensym287 = Function(AnonymousParameters([Dyn]), Dyn)
gensym109 = Dyn
gensym188 = Dyn
gensym85 = Dyn
gensym323 = Function(AnonymousParameters([Dyn]), Dyn)
gensym195 = Dyn
gensym225 = Tuple(List(Dyn), Dyn, List(List(List(Float))))
gensym345 = Function(AnonymousParameters([Dyn]), Dyn)
gensym23 = Dyn
gensym278 = Dyn
gensym343 = Function(AnonymousParameters([Dyn]), Dyn)
gensym386 = Tuple(Dyn, Dyn)
gensym316 = Dyn
gensym342 = Dyn
gensym35 = Object('', {'append': Dyn, })
gensym99 = Dyn
gensym186 = Function(AnonymousParameters([Dyn]), Dyn)
gensym381 = Dyn
gensym244 = Function(AnonymousParameters([Dyn]), Dyn)
gensym176 = Function(AnonymousParameters([Dyn]), Dyn)
gensym78 = List(Int)
gensym92 = List(List(List(Dyn)))
gensym124 = Function(AnonymousParameters([Dyn]), Dyn)
gensym119 = Dyn
gensym335 = Function(AnonymousParameters([Dyn]), Dyn)
gensym389 = Function(NamedParameters([('n', Int), ('timer', Dyn)]), Dyn)
gensym226 = Tuple(List(Float), Dict(Float, Int), List(List(List(Float))))
gensym229 = Int
gensym12 = Dyn
gensym167 = Dyn
gensym81 = Dyn
gensym279 = Function(AnonymousParameters([Dyn]), Dyn)
gensym330 = Dyn
gensym383 = Dyn
gensym217 = List(Dyn)
gensym348 = Dyn
gensym373 = Function(AnonymousParameters([]), Dyn)
gensym17 = List(Dyn)
gensym246 = Function(AnonymousParameters([Dyn]), Dyn)
gensym77 = Dyn
gensym193 = Dyn
gensym61 = Dyn
gensym275 = Function(AnonymousParameters([Dyn]), Dyn)
gensym2 = Tuple(Int, Dyn, Dyn)
gensym293 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym352 = Dyn
gensym350 = Dyn
gensym253 = Dyn
gensym372 = Dyn
gensym243 = Dyn
gensym346 = Dyn
gensym317 = Function(AnonymousParameters([Dyn]), Dyn)
gensym27 = Function(AnonymousParameters([Int]), Dyn)
gensym80 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym32 = Dyn
gensym154 = Function(AnonymousParameters([Dyn]), Dyn)
gensym145 = List(Dyn)
gensym48 = Dyn
gensym110 = List(List(Dyn))
gensym155 = Dyn
gensym259 = List(Set(List(Int)))
gensym333 = Function(AnonymousParameters([List(Float)]), Dyn)
gensym267 = Dyn
gensym166 = Function(AnonymousParameters([Dyn]), Dyn)
gensym190 = Dyn
gensym347 = Function(AnonymousParameters([]), Dyn)
gensym344 = Dyn
gensym257 = List(List(List(Set(List(Int)))))
gensym159 = Dyn
import optparse
import sys
import time
from bisect import bisect
from compat import xrange
import util
(w, h) = (5, 10)
dir_no = 6
(S, E) = mgd_cast_type_tuple(((w * h), 2), gensym0, '16', gensym1, 2)
SE = (S + (E / 2))
SW = (SE - E)
(W, NW, NE) = mgd_cast_type_tuple(((- E), (- SE), (- SW)), gensym2, '19', gensym3, 3)

def rotate(ido, rd=mgd_cast_type_dyn({E: NE, NE: NW, NW: W, W: SW, SW: SE, SE: E, }, gensym6, '22', gensym7)):
    return mgd_cast_type_list(mgd_cast_type_list([rd[o] for o in ido], gensym8, '23', gensym9), gensym10, '23', gensym11)

def flip(ido, fd=mgd_cast_type_dyn({E: E, NE: SE, NW: SW, W: W, SW: NW, SE: NE, }, gensym14, '25', gensym15)):
    return mgd_cast_type_list(mgd_cast_type_list([fd[o] for o in ido], gensym16, '26', gensym17), gensym18, '26', gensym19)

def permute(ido, r_ido, rotate=mgd_cast_type_dyn(rotate, gensym22, '29', gensym23), flip=mgd_cast_type_dyn(flip, gensym24, '29', gensym25)):
    ps = mgd_cast_type_dyn([ido], gensym30, '30', gensym31)
    gensym40 = mgd_cast_type_function(xrange, gensym32, '31', gensym33)((dir_no - 1))
    for r in gensym40:
        mgd_cast_type_function(cast0(ps, gensym34, '32', gensym35).append, gensym38, '32', gensym39)(mgd_cast_type_function(rotate, gensym36, '32', gensym37)(ps[(- 1)]))
        if (ido == r_ido):
            ps = ps[0:(dir_no // 2)]
    gensym47 = ps[:]
    for pp in gensym47:
        mgd_cast_type_function(cast0(ps, gensym41, '36', gensym42).append, gensym45, '36', gensym46)(mgd_cast_type_function(flip, gensym43, '36', gensym44)(pp))
    return mgd_cast_type_list(ps, gensym48, '37', gensym49)

def convert(ido):
    mgd_check_type_list(ido, convert, (1, 0))
    out = [0.0]
    gensym52 = ido
    for o in gensym52:
        mgd_check_type_float(o, gensym52, 3)
        mgd_check_type_void(mgd_check_type_function(out.append, out, (0, 'append'))((mgd_check_type_float(out[(- 1)], out, 3) + o)), mgd_check_type_function(out.append, out, (0, 'append')), 2)
    return mgd_cast_type_list(mgd_cast_type_function(list, gensym55, '45', gensym56)(mgd_cast_type_function(set, gensym53, '45', gensym54)(out)), gensym57, '45', gensym58)

def get_footprints(board, cti, pieces):
    mgd_check_type_list(board, get_footprints, (1, 0))
    mgd_check_type_dict(cti, get_footprints, (1, 1))
    mgd_check_type_list(pieces, get_footprints, (1, 2))
    fps = mgd_cast_type_list([mgd_cast_type_list([[] for p in mgd_cast_type_function(xrange, gensym107, '50', gensym108)(mgd_cast_type_function(len, gensym105, '50', gensym106)(pieces))], gensym109, '50', gensym110) for ci in mgd_cast_type_function(xrange, gensym103, '50', gensym104)(mgd_cast_type_function(len, gensym101, '50', gensym102)(board))], gensym111, '50', gensym112)
    gensym131 = board
    for c in gensym131:
        mgd_check_type_float(c, gensym131, 3)
        gensym130 = mgd_cast_type_function(enumerate, gensym113, '52', gensym114)(pieces)
        for (pi, p) in gensym130:
            mgd_check_type_tuple((pi, p), gensym130, 3, 2)
            gensym129 = p
            for pp in gensym129:
                fp = mgd_cast_type_function(frozenset, gensym119, '54', gensym120)(mgd_cast_type_list([mgd_check_type_int(cti[mgd_cast_type_float((c + o), gensym115, '54', gensym116)], cti, 3) for o in pp if ((c + o) in cti)], gensym117, '54', gensym118))
                if (mgd_cast_type_function(len, gensym121, '55', gensym122)(fp) == 5):
                    mgd_check_type_void(mgd_check_type_function(mgd_check_type_list(mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3)[mgd_cast_type_int(pi, gensym127, '56', gensym128)], mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3), 3).append, mgd_check_type_list(mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3)[mgd_cast_type_int(pi, gensym127, '56', gensym128)], mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3), 3), (0, 'append'))(fp), mgd_check_type_function(mgd_check_type_list(mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3)[mgd_cast_type_int(pi, gensym127, '56', gensym128)], mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3), 3).append, mgd_check_type_list(mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3)[mgd_cast_type_int(pi, gensym127, '56', gensym128)], mgd_check_type_list(fps[mgd_cast_type_int(mgd_cast_type_function(min, gensym123, '56', gensym124)(fp), gensym125, '56', gensym126)], fps, 3), 3), (0, 'append')), 2)
    return mgd_cast_type_list(fps, gensym132, '57', gensym133)

def get_senh(board, cti):
    mgd_check_type_list(board, get_senh, (1, 0))
    mgd_check_type_dict(cti, get_senh, (1, 1))
    se_nh = []
    nh = [E, SW, SE]
    gensym144 = board
    for c in gensym144:
        mgd_check_type_float(c, gensym144, 3)
        mgd_check_type_void(mgd_check_type_function(se_nh.append, se_nh, (0, 'append'))(mgd_cast_type_function(frozenset, gensym142, '65', gensym143)(mgd_cast_type_list([mgd_check_type_int(cti[mgd_cast_type_float((c + o), gensym138, '65', gensym139)], cti, 3) for o in mgd_cast_type_dyn(nh, gensym136, '65', gensym137) if ((c + o) in cti)], gensym140, '65', gensym141))), mgd_check_type_function(se_nh.append, se_nh, (0, 'append')), 2)
    return mgd_cast_type_list(se_nh, gensym145, '66', gensym146)

def get_puzzle(w=mgd_cast_type_dyn(w, gensym149, '69', gensym150), h=mgd_cast_type_dyn(h, gensym151, '69', gensym152)):
    board = mgd_cast_type_list([(((E * x) + (S * y)) + (y % 2)) for y in mgd_cast_type_function(xrange, gensym199, '70', gensym200)(h) for x in mgd_cast_type_function(xrange, gensym201, '70', gensym202)(w)], gensym203, '70', gensym204)
    cti = mgd_cast_type_function(dict, gensym211, '71', gensym212)(((board[mgd_cast_type_int(i, gensym209, '71', gensym210)], i) for i in mgd_cast_type_function(xrange, gensym207, '71', gensym208)(mgd_cast_type_function(len, gensym205, '71', gensym206)(board))))
    idos = [[E, E, E, SE], [SE, SW, W, SW], [W, W, SW, SE], [E, E, SW, SE], [NW, W, NW, SE, SW], [E, E, NE, W], [NW, NE, NE, W], [NE, SE, E, NE], [SE, SE, E, SE], [E, NW, NW, NW]]
    perms = (mgd_check_type_list(permute(mgd_cast_type_dyn(p, gensym215, '84', gensym216), mgd_cast_type_dyn(mgd_check_type_list(idos[3], idos, 3), gensym217, '84', gensym218)), permute, 2) for p in mgd_cast_type_dyn(idos, gensym213, '84', gensym214))
    pieces = mgd_cast_type_list([mgd_cast_type_list([mgd_check_type_list(convert(mgd_cast_type_list(pp, gensym219, '85', gensym220)), convert, 2) for pp in p], gensym221, '85', gensym222) for p in perms], gensym223, '85', gensym224)
    return mgd_cast_type_tuple((board, cti, pieces), gensym225, '86', gensym226, 3)

def print_board(board, w=mgd_cast_type_dyn(w, gensym229, '89', gensym230), h=mgd_cast_type_dyn(h, gensym231, '89', gensym232)):
    gensym252 = mgd_cast_type_function(xrange, gensym241, '90', gensym242)(h)
    for y in gensym252:
        gensym247 = mgd_cast_type_function(xrange, gensym243, '91', gensym244)(w)
        for x in gensym247:
            mgd_cast_type_function(print, gensym245, '92', gensym246)(board[(x + (y * w))])
        mgd_cast_type_function(print, gensym248, '93', gensym249)('')
        if ((y % 2) == 0):
            mgd_cast_type_function(print, gensym250, '95', gensym251)('')
    mgd_cast_type_function(print, gensym253, '96', gensym254)()
(board, cti, pieces) = mgd_check_type_tuple(get_puzzle(), get_puzzle, 2, 3)
fps = mgd_check_type_list(get_footprints(board, cti, pieces), get_footprints, 2)
se_nh = mgd_check_type_list(get_senh(board, cti), get_senh, 2)

def solve(n, i_min, free, curr_board, pieces_left, solutions, fps=mgd_cast_type_dyn(fps, gensym257, '105', gensym258), se_nh=mgd_cast_type_dyn(se_nh, gensym259, '105', gensym260), bisect=bisect):
    fp_i_cands = fps[i_min]
    gensym305 = pieces_left
    for p in gensym305:
        fp_cands = fp_i_cands[p]
        gensym302 = fp_cands
        for fp in gensym302:
            if (fp <= free):
                n_curr_board = curr_board[:]
                gensym273 = fp
                for ci in gensym273:
                    n_curr_board[ci] = p
                if (mgd_cast_type_function(len, gensym274, '114', gensym275)(pieces_left) > 1):
                    n_free = (free - fp)
                    n_i_min = mgd_cast_type_function(min, gensym276, '116', gensym277)(n_free)
                    if (mgd_cast_type_function(len, gensym278, '117', gensym279)((n_free & se_nh[n_i_min])) > 0):
                        n_pieces_left = pieces_left[:]
                        mgd_cast_type_function(cast1(n_pieces_left, gensym280, '119', gensym281).remove, gensym282, '119', gensym283)(p)
                        mgd_check_type_void(solve(n, n_i_min, n_free, n_curr_board, n_pieces_left, solutions), solve, 2)
                else:
                    s = mgd_cast_type_function(''.join, gensym286, '123', gensym287)(mgd_cast_type_function(map, gensym284, '123', gensym285)(str, n_curr_board))
                    mgd_cast_type_function(cast2(solutions, gensym288, '124', gensym289).insert, gensym292, '124', gensym293)(mgd_cast_type_function(bisect, gensym290, '124', gensym291)(solutions, s), s)
                    rs = s[::(- 1)]
                    mgd_cast_type_function(cast2(solutions, gensym294, '126', gensym295).insert, gensym298, '126', gensym299)(mgd_cast_type_function(bisect, gensym296, '126', gensym297)(solutions, rs), rs)
                    if (mgd_cast_type_function(len, gensym300, '127', gensym301)(solutions) >= n):
                        return
        if (mgd_cast_type_function(len, gensym303, '129', gensym304)(solutions) >= n):
            return
    return
SOLVE_ARG = 60

def main(n, timer):
    mgd_check_type_int(n, main, (1, 0))
    times = []
    gensym374 = mgd_cast_type_function(xrange, gensym348, '137', gensym349)(n)
    for i in gensym374:
        t0 = mgd_cast_type_function(timer, gensym350, '138', gensym351)()
        free = mgd_cast_type_function(frozenset, gensym356, '139', gensym357)(mgd_cast_type_function(xrange, gensym354, '139', gensym355)(mgd_cast_type_function(len, gensym352, '139', gensym353)(board)))
        curr_board = ([(- 1)] * mgd_cast_type_function(len, gensym358, '140', gensym359)(board))
        pieces_left = mgd_cast_type_function(list, gensym364, '141', gensym365)(mgd_cast_type_function(range, gensym362, '141', gensym363)(mgd_cast_type_function(len, gensym360, '141', gensym361)(pieces)))
        solutions = []
        mgd_check_type_void(solve(mgd_cast_type_dyn(SOLVE_ARG, gensym366, '143', gensym367), mgd_cast_type_dyn(0, gensym368, '143', gensym369), free, curr_board, pieces_left, mgd_cast_type_dyn(solutions, gensym370, '143', gensym371)), solve, 2)
        tk = mgd_cast_type_function(timer, gensym372, '146', gensym373)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((tk - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym375, '148', gensym376)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast3(optparse, gensym377, '151', gensym378).OptionParser, gensym379, '151', gensym380)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast4(parser, gensym381, '155', gensym382).parse_args, gensym383, '155', gensym384)(), gensym385, '155', gensym386, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast5(options, gensym387, '157', gensym388).num_runs, mgd_cast_type_dyn(main, gensym389, '157', gensym390))
