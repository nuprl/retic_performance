from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check2(val):
    try:
        val.argv
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.IntComp
        val.StringComp
        val.Discr
        val.copy
        val.EnumComp
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.exit
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.PtrComp
        return val
    except:
        raise CheckError(val)
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

    def __init__(self, PtrComp=None, Discr=0, EnumComp=0, IntComp=0, StringComp=''):
        self.PtrComp = PtrComp
        self.Discr = Discr
        self.EnumComp = EnumComp
        self.IntComp = IntComp
        self.StringComp = StringComp
    __init__ = check_type_function(__init__)

    def copy(self):
        check0(self)
        return check0(PSRecord(check1(self).PtrComp, check_type_int(self.Discr), check_type_int(self.EnumComp), check_type_int(self.IntComp), check_type_string(self.StringComp)))
    copy = check_type_function(copy)
PSRecord = check_type_class(PSRecord, ['__init__', 'copy'])
TRUE = 1
FALSE = 0

def main(loops=LOOPS):
    (benchtime, stones) = check_type_tuple(pystones(loops), 2)
    check_type_function(print)(('Pystone(%s) time for %d passes = %g' % (__version__, loops, benchtime)))
    check_type_function(print)(('This machine benchmarks at %g pystones/second' % stones))
main = check_type_function(main)

def pystones(loops=LOOPS):
    return check_type_tuple(Proc0(loops), 2)
pystones = check_type_function(pystones)
IntGlob = 0
BoolGlob = FALSE
Char1Glob = '\x00'
Char2Glob = '\x00'
Array1Glob = ([0] * 51)
Array2Glob = check_type_list(check_type_list([check_type_list(x[:]) for x in ([Array1Glob] * 51)]))
PtrGlb = check0(PSRecord())
PtrGlbNext = check0(PSRecord())

def Proc0(loops=LOOPS):
    global IntGlob
    global BoolGlob
    global Char1Glob
    global Char2Glob
    global Array1Glob
    global Array2Glob
    global PtrGlb
    global PtrGlbNext
    starttime = check_type_function(clock)()
    for i in check_type_function(range)(loops):
        pass
    nulltime = (check_type_function(clock)() - starttime)
    PtrGlbNext = check0(PSRecord())
    PtrGlb = check0(PSRecord())
    PtrGlb.PtrComp = PtrGlbNext
    PtrGlb.Discr = Ident1
    PtrGlb.EnumComp = Ident3
    PtrGlb.IntComp = 40
    PtrGlb.StringComp = 'DHRYSTONE PROGRAM, SOME STRING'
    String1Loc = "DHRYSTONE PROGRAM, 1'ST STRING"
    Array2Glob[8][7] = 10
    starttime = check_type_function(clock)()
    for i in check_type_function(range)(loops):
        Proc5()
        Proc4()
        IntLoc1 = 2
        IntLoc2 = 3
        String2Loc = "DHRYSTONE PROGRAM, 2'ND STRING"
        EnumLoc = Ident2
        BoolGlob = (not check_type_int(Func2(String1Loc, String2Loc)))
        while (IntLoc1 < IntLoc2):
            IntLoc3 = ((5 * IntLoc1) - IntLoc2)
            IntLoc3 = check_type_int(Proc7(check_type_int(IntLoc1), check_type_int(IntLoc2)))
            IntLoc1 = (IntLoc1 + 1)
        Proc8(Array1Glob, check_type_list(Array2Glob), check_type_int(IntLoc1), check_type_int(IntLoc3))
        PtrGlb = check0(Proc1(PtrGlb))
        CharIndex = 'A'
        while (CharIndex <= Char2Glob):
            if (EnumLoc == check_type_int(Func1(check_type_string(CharIndex), 'C'))):
                EnumLoc = check_type_int(Proc6(Ident1))
            CharIndex = check_type_function(chr)((check_type_function(ord)(CharIndex) + 1))
        IntLoc3 = (IntLoc2 * IntLoc1)
        IntLoc2 = (IntLoc3 / IntLoc1)
        IntLoc2 = ((7 * (IntLoc3 - IntLoc2)) - IntLoc1)
        IntLoc1 = check_type_int(Proc2(check_type_int(IntLoc1)))
    benchtime = ((check_type_function(clock)() - starttime) - nulltime)
    if (benchtime == 0.0):
        loopsPerBenchtime = 0.0
    else:
        loopsPerBenchtime = (loops / benchtime)
    return check_type_tuple((benchtime, loopsPerBenchtime), 2)
Proc0 = check_type_function(Proc0)

def Proc1(PtrParIn):
    check0(PtrParIn)
    PtrParIn.PtrComp = NextPSRecord = check0(check_type_function(PtrGlb.copy)())
    PtrParIn.IntComp = 5
    NextPSRecord.IntComp = check_type_int(PtrParIn.IntComp)
    NextPSRecord.PtrComp = check1(PtrParIn).PtrComp
    NextPSRecord.PtrComp = check0(Proc3(check0(check1(NextPSRecord).PtrComp)))
    if (check_type_int(NextPSRecord.Discr) == Ident1):
        NextPSRecord.IntComp = 6
        NextPSRecord.EnumComp = check_type_int(Proc6(check_type_int(PtrParIn.EnumComp)))
        NextPSRecord.PtrComp = check1(PtrGlb).PtrComp
        NextPSRecord.IntComp = check_type_int(Proc7(check_type_int(NextPSRecord.IntComp), 10))
    else:
        PtrParIn = check0(check_type_function(NextPSRecord.copy)())
    NextPSRecord.PtrComp = None
    return PtrParIn
Proc1 = check_type_function(Proc1)

def Proc2(IntParIO):
    check_type_int(IntParIO)
    IntLoc = (IntParIO + 10)
    while 1:
        if (Char1Glob == 'A'):
            IntLoc = (IntLoc - 1)
            IntParIO = check_type_int((IntLoc - IntGlob))
            EnumLoc = Ident1
        if (EnumLoc == Ident1):
            break
    return IntParIO
Proc2 = check_type_function(Proc2)

def Proc3(PtrParOut):
    check0(PtrParOut)
    global IntGlob
    if (PtrGlb is not None):
        PtrParOut = check0(check1(PtrGlb).PtrComp)
    else:
        IntGlob = 100
    PtrGlb.IntComp = check_type_int(Proc7(10, IntGlob))
    return PtrParOut
Proc3 = check_type_function(Proc3)

def Proc4():
    global Char2Glob
    BoolLoc = (Char1Glob == 'A')
    BoolLoc = (BoolLoc or BoolGlob)
    Char2Glob = 'B'
Proc4 = check_type_function(Proc4)

def Proc5():
    global Char1Glob
    global BoolGlob
    Char1Glob = 'A'
    BoolGlob = FALSE
Proc5 = check_type_function(Proc5)

def Proc6(EnumParIn):
    check_type_int(EnumParIn)
    EnumParOut = EnumParIn
    if (not check_type_int(Func3(EnumParIn))):
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
Proc6 = check_type_function(Proc6)

def Proc7(IntParI1, IntParI2):
    check_type_int(IntParI1)
    check_type_int(IntParI2)
    IntLoc = (IntParI1 + 2)
    IntParOut = (IntParI2 + IntLoc)
    return check_type_int(IntParOut)
Proc7 = check_type_function(Proc7)

def Proc8(Array1Par, Array2Par, IntParI1, IntParI2):
    check_type_list(Array1Par)
    check_type_list(Array2Par)
    check_type_int(IntParI1)
    check_type_int(IntParI2)
    global IntGlob
    IntLoc = (IntParI1 + 5)
    Array1Par[IntLoc] = IntParI2
    Array1Par[(IntLoc + 1)] = check_type_int(Array1Par[IntLoc])
    Array1Par[(IntLoc + 30)] = IntLoc
    for IntIndex in check_type_function(range)(IntLoc, (IntLoc + 2)):
        check_type_list(Array2Par[IntLoc])[check_type_int(IntIndex)] = IntLoc
    check_type_list(Array2Par[IntLoc])[(IntLoc - 1)] = (check_type_int(check_type_list(Array2Par[IntLoc])[(IntLoc - 1)]) + 1)
    check_type_list(Array2Par[(IntLoc + 20)])[IntLoc] = check_type_int(Array1Par[IntLoc])
    IntGlob = 5
Proc8 = check_type_function(Proc8)

def Func1(CharPar1, CharPar2):
    check_type_string(CharPar1)
    check_type_string(CharPar2)
    CharLoc1 = CharPar1
    CharLoc2 = CharLoc1
    if (CharLoc2 != CharPar2):
        return Ident1
    else:
        return Ident2
Func1 = check_type_function(Func1)

def Func2(StrParI1, StrParI2):
    check_type_string(StrParI1)
    check_type_string(StrParI2)
    IntLoc = 1
    while (IntLoc <= 1):
        if (check_type_int(Func1(check_type_string(StrParI1[check_type_int(IntLoc)]), check_type_string(StrParI2[check_type_int((IntLoc + 1))]))) == Ident1):
            CharLoc = 'A'
            IntLoc = (IntLoc + 1)
    if ((CharLoc >= 'W') and (CharLoc <= 'Z')):
        IntLoc = 7
    if (CharLoc == 'X'):
        return TRUE
    elif (StrParI1 > StrParI2):
        IntLoc = (IntLoc + 7)
        return TRUE
    else:
        return FALSE
Func2 = check_type_function(Func2)

def Func3(EnumParIn):
    check_type_int(EnumParIn)
    EnumLoc = EnumParIn
    if (EnumLoc == Ident3):
        return TRUE
    return FALSE
Func3 = check_type_function(Func3)
if (__name__ == '__main__'):
    import sys

    def error(msg):
        check_type_function(print)(msg, end=' ', file=sys.stderr)
        check_type_function(print)(('usage: %s [number_of_loops]' % check2(sys).argv[0]), file=sys.stderr)
        check_type_function(check3(sys).exit)(100)
    error = check_type_function(error)
    nargs = (check_type_function(len)(check2(sys).argv) - 1)
    if (nargs > 1):
        error(('%d arguments are too many;' % nargs))
    elif (nargs == 1):
        try:
            loops = check_type_function(int)(check2(sys).argv[1])
        except ValueError:
            error(('Invalid argument %r;' % check2(sys).argv[1]))
    else:
        loops = LOOPS
    main(loops)
