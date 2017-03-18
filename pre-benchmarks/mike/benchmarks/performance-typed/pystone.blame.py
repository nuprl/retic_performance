from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def check0(val, elim, act):
    try:
        val.StringComp
        val.Discr
        val.IntComp
        val.EnumComp
        val.copy
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def cast3(val, src, b, trg):
    try:
        val.argv
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast1(val, src, b, trg):
    try:
        val.PtrComp
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast4(val, src, b, trg):
    try:
        val.exit
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.StringComp
        val.Discr
        val.IntComp
        val.EnumComp
        val.copy
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym97 = Function(AnonymousParameters([Dyn]), Dyn)
gensym238 = Dyn
gensym27 = Function(DynParameters, Dyn)
gensym126 = Dyn
gensym201 = Object('PSRecord', {'PtrComp': Dyn, })
gensym157 = String
gensym231 = Function(NamedParameters([]), Dyn)
gensym256 = Dyn
gensym8 = Int
gensym84 = Dyn
gensym61 = Function(AnonymousParameters([]), Dyn)
gensym4 = Int
gensym149 = Int
gensym239 = Function(NamedParameters([('IntParI1', Int), ('IntParI2', Int)]), Int)
gensym183 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym255 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym197 = Object('PSRecord', {'PtrComp': Dyn, })
gensym180 = Dyn
gensym229 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym291 = Dyn
gensym15 = Object('PSRecord', {'PtrComp': Dyn, })
gensym277 = Int
gensym306 = Function(DynParameters, Dyn)
gensym268 = Dyn
gensym278 = Dyn
gensym12 = Dyn
gensym50 = Dyn
gensym127 = Function(AnonymousParameters([Dyn]), Dyn)
gensym119 = Function(AnonymousParameters([Dyn]), Dyn)
gensym92 = Dyn
gensym272 = Dyn
gensym51 = Function(DynParameters, Tuple(Float, Float))
gensym174 = Tuple(Dyn, Dyn)
gensym69 = Int
gensym269 = Int
gensym309 = Dyn
gensym85 = Function(AnonymousParameters([]), Dyn)
gensym21 = Dyn
gensym52 = Int
gensym121 = Int
gensym182 = Dyn
gensym167 = Int
gensym281 = Int
gensym168 = Dyn
gensym219 = Int
gensym54 = Dyn
gensym70 = Dyn
gensym192 = Dyn
gensym273 = Int
gensym74 = Dyn
gensym247 = Int
gensym166 = Int
gensym13 = Function(NamedParameters([('self', Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), }))]), Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), }))
gensym60 = Dyn
gensym56 = Dyn
gensym39 = Dyn
gensym144 = Dyn
gensym284 = Function(NamedParameters([('CharPar1', String), ('CharPar2', String)]), Int)
gensym122 = Dyn
gensym104 = Dyn
gensym205 = Object('PSRecord', {'PtrComp': Dyn, })
gensym259 = Int
gensym251 = Int
gensym300 = Function(NamedParameters([('msg', Dyn)]), Dyn)
gensym117 = Function(AnonymousParameters([Dyn]), Dyn)
gensym248 = Dyn
gensym233 = Dyn
gensym113 = Int
gensym10 = String
gensym224 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym227 = Object('PSRecord', {'PtrComp': Dyn, })
gensym303 = Dyn
gensym287 = Dyn
gensym93 = Int
gensym2 = Void
gensym243 = Int
gensym68 = Dyn
gensym47 = List(List(Int))
gensym214 = Dyn
gensym22 = String
gensym3 = Dyn
gensym43 = Dyn
gensym185 = Object('PSRecord', {'PtrComp': Dyn, })
gensym253 = Int
gensym110 = Dyn
gensym308 = Object('', {'exit': Dyn, })
gensym292 = Int
gensym221 = Function(NamedParameters([('PtrParOut', Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), }))]), Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), }))
gensym188 = Dyn
gensym213 = Dyn
gensym138 = Function(AnonymousParameters([Dyn]), Dyn)
gensym141 = Int
gensym66 = Dyn
gensym193 = Function(AnonymousParameters([]), Dyn)
gensym209 = Dyn
gensym103 = Function(AnonymousParameters([]), Dyn)
gensym212 = Void
gensym296 = Dyn
gensym301 = Dyn
gensym244 = Dyn
gensym250 = Dyn
gensym305 = Dyn
gensym72 = Dyn
gensym207 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym152 = List(List(Int))
gensym228 = Dyn
gensym123 = Function(AnonymousParameters([]), Dyn)
gensym179 = Object('PSRecord', {'PtrComp': Dyn, })
gensym57 = Function(AnonymousParameters([Dyn]), Dyn)
gensym147 = Dyn
gensym249 = Int
gensym16 = Int
gensym320 = Object('', {'argv': Dyn, })
gensym48 = List(List(Int))
gensym86 = Dyn
gensym63 = Function(AnonymousParameters([Dyn]), Dyn)
gensym25 = Class('PSRecord', {'__init__': Function(DynParameters, Dyn), 'copy': Function(NamedParameters([('self', TypeVariable('PSRecord'))]), TypeVariable('PSRecord')), }, {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, })
gensym45 = Dyn
gensym35 = Function(AnonymousParameters([Dyn]), Dyn)
gensym23 = Dyn
gensym88 = Dyn
gensym75 = Function(AnonymousParameters([Dyn]), Dyn)
gensym200 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym137 = Dyn
gensym203 = Object('PSRecord', {'PtrComp': Dyn, })
gensym267 = Int
gensym17 = Dyn
gensym150 = Dyn
gensym78 = Dyn
gensym115 = Int
gensym223 = Object('PSRecord', {'PtrComp': Dyn, })
gensym310 = Function(AnonymousParameters([Int]), Dyn)
gensym164 = Function(AnonymousParameters([Dyn]), Dyn)
gensym211 = Object('PSRecord', {'PtrComp': Dyn, })
gensym116 = Dyn
gensym106 = Dyn
gensym109 = Function(AnonymousParameters([]), Dyn)
gensym202 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym319 = Dyn
gensym252 = Dyn
gensym91 = Int
gensym38 = Int
gensym274 = Dyn
gensym67 = String
gensym321 = Int
gensym232 = Bool
gensym14 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym271 = Int
gensym146 = Int
gensym153 = Dyn
gensym124 = Dyn
gensym96 = Dyn
gensym265 = Int
gensym261 = Int
gensym32 = Dyn
gensym230 = Dyn
gensym226 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym217 = Dyn
gensym89 = Function(AnonymousParameters([Dyn]), Dyn)
gensym314 = Function(AnonymousParameters([Dyn]), Dyn)
gensym279 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym83 = Function(AnonymousParameters([Dyn]), Dyn)
gensym6 = Int
gensym295 = Int
gensym266 = Dyn
gensym298 = Function(NamedParameters([('EnumParIn', Int)]), Int)
gensym131 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym33 = Function(AnonymousParameters([String]), Dyn)
gensym199 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym222 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym315 = Dyn
gensym288 = Function(NamedParameters([('StrParI1', String), ('StrParI2', String)]), Int)
gensym163 = Dyn
gensym46 = Dyn
gensym145 = Dyn
gensym64 = Dyn
gensym37 = Function(DynParameters, Dyn)
gensym112 = Dyn
gensym42 = Int
gensym190 = Dyn
gensym108 = Dyn
gensym173 = Dyn
gensym286 = Dyn
gensym0 = Dyn
gensym79 = Function(AnonymousParameters([]), Dyn)
gensym29 = Dyn
gensym148 = Int
gensym275 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym195 = Object('PSRecord', {'PtrComp': Dyn, })
gensym264 = Dyn
gensym311 = Dyn
gensym297 = Dyn
gensym134 = Dyn
gensym270 = Dyn
gensym80 = Dyn
gensym111 = Function(AnonymousParameters([Dyn]), Dyn)
gensym293 = Dyn
gensym318 = Function(AnonymousParameters([Dyn]), Dyn)
gensym198 = Dyn
gensym36 = Dyn
gensym191 = Object('', {'copy': Dyn, })
gensym99 = Int
gensym136 = Function(AnonymousParameters([]), Dyn)
gensym20 = Int
gensym170 = Dyn
gensym19 = Dyn
gensym257 = Int
gensym102 = Dyn
gensym143 = Bool
gensym44 = List(List(Int))
gensym177 = Function(NamedParameters([('PtrParIn', Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), }))]), Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), }))
gensym322 = Dyn
gensym59 = Function(AnonymousParameters([]), Dyn)
gensym34 = Dyn
gensym161 = Dyn
gensym114 = Dyn
gensym49 = List(Dyn)
gensym94 = Dyn
gensym276 = Dyn
gensym9 = Dyn
gensym55 = Function(AnonymousParameters([]), Dyn)
gensym158 = Dyn
gensym234 = Dyn
gensym181 = Object('', {'PtrComp': Dyn, })
gensym156 = Int
gensym100 = Dyn
gensym260 = Dyn
gensym215 = Function(NamedParameters([('IntParIO', Int)]), Int)
gensym24 = Dyn
gensym76 = Dyn
gensym280 = Dyn
gensym299 = Dyn
gensym187 = Object('', {'IntComp': Dyn, })
gensym40 = Tuple(Float, Float)
gensym82 = Dyn
gensym41 = Dyn
gensym290 = Dyn
gensym165 = Dyn
gensym129 = Dyn
gensym208 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym307 = Dyn
gensym220 = Dyn
gensym172 = Float
gensym245 = Function(NamedParameters([('Array1Par', List(Int)), ('Array2Par', List(List(Int))), ('IntParI1', Int), ('IntParI2', Int)]), Dyn)
gensym304 = Object('', {'argv': Dyn, })
gensym28 = Int
gensym262 = Dyn
gensym1 = Function(DynParameters, Dyn)
gensym90 = Dyn
gensym71 = Int
gensym81 = Function(AnonymousParameters([]), Dyn)
gensym206 = Dyn
gensym285 = String
gensym120 = Dyn
gensym107 = Function(AnonymousParameters([]), Dyn)
gensym130 = Function(AnonymousParameters([]), Dyn)
gensym196 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym159 = Dyn
gensym73 = Function(AnonymousParameters([Dyn]), Dyn)
gensym30 = Dyn
gensym189 = Int
gensym175 = Tuple(Float, Float)
gensym140 = Dyn
gensym225 = Object('PSRecord', {'PtrComp': Dyn, })
gensym204 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym7 = Dyn
gensym194 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym216 = Int
gensym125 = Function(AnonymousParameters([]), Dyn)
gensym162 = Function(AnonymousParameters([Dyn]), Dyn)
gensym95 = Function(AnonymousParameters([Dyn]), Dyn)
gensym312 = Object('', {'argv': Dyn, })
gensym77 = Int
gensym105 = Function(AnonymousParameters([Dyn]), Dyn)
gensym294 = Int
gensym53 = Dyn
gensym186 = Dyn
gensym11 = Dyn
gensym210 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym246 = Dyn
gensym317 = Dyn
gensym101 = Function(AnonymousParameters([]), Dyn)
gensym171 = Function(AnonymousParameters([]), Dyn)
gensym178 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym133 = Int
gensym62 = Dyn
gensym289 = Int
gensym184 = Object('PSRecord', {'StringComp': String, 'Discr': Int, 'IntComp': Int, 'EnumComp': Int, 'copy': Function(NamedParameters([]), TypeVariable('PSRecord')), })
gensym176 = Dyn
gensym241 = Dyn
gensym98 = Dyn
gensym65 = String
gensym142 = Dyn
gensym151 = List(Dyn)
gensym235 = Function(NamedParameters([]), Dyn)
gensym237 = Function(NamedParameters([('EnumParIn', Int)]), Int)
gensym242 = Dyn
gensym155 = Dyn
gensym236 = Dyn
gensym313 = Dyn
gensym139 = Int
gensym218 = Dyn
gensym5 = Dyn
gensym263 = Int
gensym87 = Function(AnonymousParameters([]), Dyn)
gensym302 = Function(DynParameters, Dyn)
gensym258 = Dyn
gensym132 = Dyn
gensym31 = Tuple(Dyn, Dyn)
gensym154 = Int
gensym18 = Int
gensym240 = Int
gensym316 = Object('', {'argv': Dyn, })
gensym58 = Dyn
gensym118 = Dyn
gensym283 = Dyn
gensym160 = String
gensym26 = Dyn
gensym254 = Dyn
gensym135 = Dyn
LOOPS = 50000
from time import clock
__version__ = '1.1'
Ident1 = 1
Ident2 = 2
Ident3 = 3
Ident4 = 4
Ident5 = 5
Ident6 = 6


class PSRecord:

    def __init__(self, PtrComp=mgd_cast_type_dyn(None, gensym2, '53', gensym3), Discr=mgd_cast_type_dyn(0, gensym4, '53', gensym5), EnumComp=mgd_cast_type_dyn(0, gensym6, '53', gensym7), IntComp=mgd_cast_type_dyn(0, gensym8, '54', gensym9), StringComp=mgd_cast_type_dyn('', gensym10, '54', gensym11)):
        self.PtrComp = PtrComp
        self.Discr = Discr
        self.EnumComp = EnumComp
        self.IntComp = IntComp
        self.StringComp = StringComp

    def copy(self):
        check0(self, self.copy, (1, 0))
        return check0(PSRecord(cast1(self, gensym14, '62', gensym15).PtrComp, mgd_cast_type_dyn(mgd_check_type_int(self.Discr, self, (0, 'Discr')), gensym16, '62', gensym17), mgd_cast_type_dyn(mgd_check_type_int(self.EnumComp, self, (0, 'EnumComp')), gensym18, '62', gensym19), mgd_cast_type_dyn(mgd_check_type_int(self.IntComp, self, (0, 'IntComp')), gensym20, '63', gensym21), mgd_cast_type_dyn(mgd_check_type_string(self.StringComp, self, (0, 'StringComp')), gensym22, '63', gensym23)), PSRecord, 2)
PSRecord = mgd_cast_type_class(PSRecord, gensym24, '50', gensym25, ['__init__', 'copy'])
TRUE = 1
FALSE = 0

def main(loops=mgd_cast_type_dyn(LOOPS, gensym28, '68', gensym29)):
    (benchtime, stones) = mgd_cast_type_tuple(pystones(loops), gensym30, '69', gensym31, 2)
    mgd_cast_type_function(print, gensym32, '70', gensym33)(('Pystone(%s) time for %d passes = %g' % (__version__, loops, benchtime)))
    mgd_cast_type_function(print, gensym34, '72', gensym35)(('This machine benchmarks at %g pystones/second' % stones))

def pystones(loops=mgd_cast_type_dyn(LOOPS, gensym38, '75', gensym39)):
    return mgd_cast_type_dyn(mgd_check_type_tuple(Proc0(loops), Proc0, 2, 2), gensym40, '76', gensym41)
IntGlob = 0
BoolGlob = mgd_cast_type_dyn(FALSE, gensym42, '79', gensym43)
Char1Glob = '\x00'
Char2Glob = '\x00'
Array1Glob = ([0] * 51)
Array2Glob = mgd_cast_type_list(mgd_cast_type_list([mgd_check_type_list(x[:], x, 3) for x in mgd_cast_type_dyn(([Array1Glob] * 51), gensym44, '83', gensym45)], gensym46, '83', gensym47), gensym48, '83', gensym49)
PtrGlb = check0(PSRecord(), PSRecord, 2)
PtrGlbNext = check0(PSRecord(), PSRecord, 2)

def Proc0(loops=mgd_cast_type_dyn(LOOPS, gensym52, '87', gensym53)):
    global IntGlob
    global BoolGlob
    global Char1Glob
    global Char2Glob
    global Array1Glob
    global Array2Glob
    global PtrGlb
    global PtrGlbNext
    starttime = mgd_cast_type_function(clock, gensym124, '97', gensym125)()
    gensym128 = mgd_cast_type_function(range, gensym126, '98', gensym127)(loops)
    for i in gensym128:
        pass
    nulltime = (mgd_cast_type_function(clock, gensym129, '100', gensym130)() - starttime)
    PtrGlbNext = check0(PSRecord(), PSRecord, 2)
    PtrGlb = check0(PSRecord(), PSRecord, 2)
    PtrGlb.PtrComp = mgd_cast_type_dyn(PtrGlbNext, gensym131, '104', gensym132)
    PtrGlb.Discr = Ident1
    PtrGlb.EnumComp = Ident3
    PtrGlb.IntComp = 40
    PtrGlb.StringComp = 'DHRYSTONE PROGRAM, SOME STRING'
    String1Loc = "DHRYSTONE PROGRAM, 1'ST STRING"
    Array2Glob[8][7] = mgd_cast_type_dyn(10, gensym133, '110', gensym134)
    starttime = mgd_cast_type_function(clock, gensym135, '112', gensym136)()
    gensym169 = mgd_cast_type_function(range, gensym137, '114', gensym138)(loops)
    for i in gensym169:
        Proc5()
        Proc4()
        IntLoc1 = mgd_cast_type_dyn(2, gensym139, '117', gensym140)
        IntLoc2 = mgd_cast_type_dyn(3, gensym141, '118', gensym142)
        String2Loc = "DHRYSTONE PROGRAM, 2'ND STRING"
        EnumLoc = Ident2
        BoolGlob = mgd_cast_type_dyn((not mgd_check_type_int(Func2(String1Loc, String2Loc), Func2, 2)), gensym143, '121', gensym144)
        while (IntLoc1 < IntLoc2):
            IntLoc3 = ((5 * IntLoc1) - IntLoc2)
            IntLoc3 = mgd_cast_type_dyn(mgd_check_type_int(Proc7(mgd_cast_type_int(IntLoc1, gensym145, '124', gensym146), mgd_cast_type_int(IntLoc2, gensym147, '124', gensym148)), Proc7, 2), gensym149, '124', gensym150)
            IntLoc1 = (IntLoc1 + 1)
        Proc8(Array1Glob, mgd_cast_type_list(Array2Glob, gensym151, '126', gensym152), mgd_cast_type_int(IntLoc1, gensym153, '126', gensym154), mgd_cast_type_int(IntLoc3, gensym155, '126', gensym156))
        PtrGlb = check0(Proc1(PtrGlb), Proc1, 2)
        CharIndex = mgd_cast_type_dyn('A', gensym157, '128', gensym158)
        while (CharIndex <= Char2Glob):
            if (EnumLoc == mgd_check_type_int(Func1(mgd_cast_type_string(CharIndex, gensym159, '130', gensym160), 'C'), Func1, 2)):
                EnumLoc = mgd_check_type_int(Proc6(Ident1), Proc6, 2)
            CharIndex = mgd_cast_type_function(chr, gensym163, '132', gensym164)((mgd_cast_type_function(ord, gensym161, '132', gensym162)(CharIndex) + 1))
        IntLoc3 = (IntLoc2 * IntLoc1)
        IntLoc2 = (IntLoc3 / IntLoc1)
        IntLoc2 = ((7 * (IntLoc3 - IntLoc2)) - IntLoc1)
        IntLoc1 = mgd_cast_type_dyn(mgd_check_type_int(Proc2(mgd_cast_type_int(IntLoc1, gensym165, '136', gensym166)), Proc2, 2), gensym167, '136', gensym168)
    benchtime = ((mgd_cast_type_function(clock, gensym170, '138', gensym171)() - starttime) - nulltime)
    if (benchtime == 0.0):
        loopsPerBenchtime = mgd_cast_type_dyn(0.0, gensym172, '140', gensym173)
    else:
        loopsPerBenchtime = (loops / benchtime)
    return mgd_cast_type_tuple((benchtime, loopsPerBenchtime), gensym174, '143', gensym175, 2)

def Proc1(PtrParIn):
    check0(PtrParIn, Proc1, (1, 0))
    PtrParIn.PtrComp = NextPSRecord = check0(mgd_check_type_function(PtrGlb.copy, PtrGlb, (0, 'copy'))(), mgd_check_type_function(PtrGlb.copy, PtrGlb, (0, 'copy')), 2)
    PtrParIn.IntComp = 5
    NextPSRecord.IntComp = mgd_check_type_int(PtrParIn.IntComp, PtrParIn, (0, 'IntComp'))
    NextPSRecord.PtrComp = cast1(PtrParIn, gensym202, '149', gensym203).PtrComp
    NextPSRecord.PtrComp = mgd_cast_type_dyn(check0(Proc3(cast2(cast1(NextPSRecord, gensym204, '150', gensym205).PtrComp, gensym206, '150', gensym207)), Proc3, 2), gensym208, '150', gensym209)
    if (mgd_check_type_int(NextPSRecord.Discr, NextPSRecord, (0, 'Discr')) == Ident1):
        NextPSRecord.IntComp = 6
        NextPSRecord.EnumComp = mgd_check_type_int(Proc6(mgd_check_type_int(PtrParIn.EnumComp, PtrParIn, (0, 'EnumComp'))), Proc6, 2)
        NextPSRecord.PtrComp = cast1(PtrGlb, gensym210, '154', gensym211).PtrComp
        NextPSRecord.IntComp = mgd_check_type_int(Proc7(mgd_check_type_int(NextPSRecord.IntComp, NextPSRecord, (0, 'IntComp')), 10), Proc7, 2)
    else:
        PtrParIn = check0(mgd_check_type_function(NextPSRecord.copy, NextPSRecord, (0, 'copy'))(), mgd_check_type_function(NextPSRecord.copy, NextPSRecord, (0, 'copy')), 2)
    NextPSRecord.PtrComp = mgd_cast_type_dyn(None, gensym212, '158', gensym213)
    return PtrParIn

def Proc2(IntParIO):
    mgd_check_type_int(IntParIO, Proc2, (1, 0))
    IntLoc = mgd_cast_type_dyn((IntParIO + 10), gensym216, '162', gensym217)
    while 1:
        if (Char1Glob == 'A'):
            IntLoc = (IntLoc - 1)
            IntParIO = mgd_cast_type_int((IntLoc - IntGlob), gensym218, '166', gensym219)
            EnumLoc = Ident1
        if (EnumLoc == Ident1):
            break
    return IntParIO

def Proc3(PtrParOut):
    check0(PtrParOut, Proc3, (1, 0))
    global IntGlob
    if (PtrGlb is not None):
        PtrParOut = cast2(cast1(PtrGlb, gensym226, '176', gensym227).PtrComp, gensym228, '176', gensym229)
    else:
        IntGlob = 100
    PtrGlb.IntComp = mgd_check_type_int(Proc7(10, IntGlob), Proc7, 2)
    return PtrParOut

def Proc4():
    global Char2Glob
    BoolLoc = mgd_cast_type_dyn((Char1Glob == 'A'), gensym232, '185', gensym233)
    BoolLoc = (BoolLoc or BoolGlob)
    Char2Glob = 'B'

def Proc5():
    global Char1Glob
    global BoolGlob
    Char1Glob = 'A'
    BoolGlob = FALSE

def Proc6(EnumParIn):
    mgd_check_type_int(EnumParIn, Proc6, (1, 0))
    EnumParOut = EnumParIn
    if (not mgd_check_type_int(Func3(EnumParIn), Func3, 2)):
        EnumParOut = Ident4
    if (EnumParIn == Ident1):
        EnumParOut = Ident1
    elif (EnumParIn == Ident2):
        if (IntGlob > 100):
            EnumParOut = Ident1
        else:
            EnumParOut = Ident4
    elif (EnumParIn == Ident3):
        EnumParOut = Ident2
    elif (EnumParIn == Ident4):
        pass
    elif (EnumParIn == Ident5):
        EnumParOut = Ident3
    return EnumParOut

def Proc7(IntParI1, IntParI2):
    mgd_check_type_int(IntParI1, Proc7, (1, 0))
    mgd_check_type_int(IntParI2, Proc7, (1, 1))
    IntLoc = (IntParI1 + 2)
    IntParOut = mgd_cast_type_dyn((IntParI2 + IntLoc), gensym240, '217', gensym241)
    return mgd_cast_type_int(IntParOut, gensym242, '218', gensym243)

def Proc8(Array1Par, Array2Par, IntParI1, IntParI2):
    mgd_check_type_list(Array1Par, Proc8, (1, 0))
    mgd_check_type_list(Array2Par, Proc8, (1, 1))
    mgd_check_type_int(IntParI1, Proc8, (1, 2))
    mgd_check_type_int(IntParI2, Proc8, (1, 3))
    global IntGlob
    IntLoc = (IntParI1 + 5)
    Array1Par[IntLoc] = IntParI2
    Array1Par[(IntLoc + 1)] = mgd_check_type_int(Array1Par[IntLoc], Array1Par, 3)
    Array1Par[(IntLoc + 30)] = IntLoc
    gensym282 = mgd_cast_type_function(range, gensym278, '227', gensym279)(IntLoc, (IntLoc + 2))
    for IntIndex in gensym282:
        mgd_check_type_list(Array2Par[IntLoc], Array2Par, 3)[mgd_cast_type_int(IntIndex, gensym280, '228', gensym281)] = IntLoc
    mgd_check_type_list(Array2Par[IntLoc], Array2Par, 3)[(IntLoc - 1)] = (mgd_check_type_int(mgd_check_type_list(Array2Par[IntLoc], Array2Par, 3)[(IntLoc - 1)], mgd_check_type_list(Array2Par[IntLoc], Array2Par, 3), 3) + 1)
    mgd_check_type_list(Array2Par[(IntLoc + 20)], Array2Par, 3)[IntLoc] = mgd_check_type_int(Array1Par[IntLoc], Array1Par, 3)
    IntGlob = 5

def Func1(CharPar1, CharPar2):
    mgd_check_type_string(CharPar1, Func1, (1, 0))
    mgd_check_type_string(CharPar2, Func1, (1, 1))
    CharLoc1 = CharPar1
    CharLoc2 = mgd_cast_type_dyn(CharLoc1, gensym285, '235', gensym286)
    if (CharLoc2 != CharPar2):
        return Ident1
    else:
        return Ident2

def Func2(StrParI1, StrParI2):
    mgd_check_type_string(StrParI1, Func2, (1, 0))
    mgd_check_type_string(StrParI2, Func2, (1, 1))
    IntLoc = mgd_cast_type_dyn(1, gensym289, '242', gensym290)
    while (IntLoc <= 1):
        if (mgd_check_type_int(Func1(mgd_check_type_string(StrParI1[mgd_cast_type_int(IntLoc, gensym291, '244', gensym292)], StrParI1, 3), mgd_check_type_string(StrParI2[mgd_cast_type_int((IntLoc + 1), gensym293, '244', gensym294)], StrParI2, 3)), Func1, 2) == Ident1):
            CharLoc = 'A'
            IntLoc = (IntLoc + 1)
    if ((CharLoc >= 'W') and (CharLoc <= 'Z')):
        IntLoc = mgd_cast_type_dyn(7, gensym295, '248', gensym296)
    if (CharLoc == 'X'):
        return TRUE
    elif (StrParI1 > StrParI2):
        IntLoc = (IntLoc + 7)
        return TRUE
    else:
        return FALSE

def Func3(EnumParIn):
    mgd_check_type_int(EnumParIn, Func3, (1, 0))
    EnumLoc = EnumParIn
    if (EnumLoc == Ident3):
        return TRUE
    return FALSE
if (__name__ == '__main__'):
    import sys

    def error(msg):
        mgd_cast_type_function(print, gensym301, '266', gensym302)(msg, end=' ', file=sys.stderr)
        mgd_cast_type_function(print, gensym305, '267', gensym306)(('usage: %s [number_of_loops]' % cast3(sys, gensym303, '267', gensym304).argv[0]), file=sys.stderr)
        mgd_cast_type_function(cast4(sys, gensym307, '268', gensym308).exit, gensym309, '268', gensym310)(100)
    nargs = (mgd_cast_type_function(len, gensym313, '269', gensym314)(cast3(sys, gensym311, '269', gensym312).argv) - 1)
    if (nargs > 1):
        error(('%d arguments are too many;' % nargs))
    elif (nargs == 1):
        try:
            loops = mgd_cast_type_function(int, gensym317, '273', gensym318)(cast3(sys, gensym315, '273', gensym316).argv[1])
        except ValueError:
            error(('Invalid argument %r;' % cast3(sys, gensym319, '275', gensym320).argv[1]))
    else:
        loops = mgd_cast_type_dyn(LOOPS, gensym321, '277', gensym322)
    main(loops)
