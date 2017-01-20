from __future__ import division
from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def check7(val, elim, act):
    try:
        val.GetDomain
        val.__call__
        val.knots
        val.degree
        val.GetIndex
        val.points
        val.__repr__
        val.__len__
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def check1(val, elim, act):
    try:
        val.__rmul__
        val.x
        val.__repr__
        val.linear_combination
        val.Mag
        val.__mul__
        val.__add__
        val.__str__
        val.dist
        val.y
        val.__sub__
        val.z
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def check19(val, elim, act):
    try:
        val.transform_point
        val.maxy
        val.splines
        val.width
        val.thickness
        val.height
        val.minx
        val.create_image_chaos
        val.num_trafos
        val.truncate
        val.miny
        val.get_random_trafo
        val.maxx
        val.num_total
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def cast6(val, src, b, trg):
    try:
        val.z
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast0(val, src, b, trg):
    try:
        val.seed
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast16(val, src, b, trg):
    try:
        val.num_trafos
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast13(val, src, b, trg):
    try:
        val.width
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast24(val, src, b, trg):
    try:
        val.Mag
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast11(val, src, b, trg):
    try:
        val.maxx
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast14(val, src, b, trg):
    try:
        val.height
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast18(val, src, b, trg):
    try:
        val.add
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast15(val, src, b, trg):
    try:
        val.dist
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast21(val, src, b, trg):
    try:
        val.get_random_trafo
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast9(val, src, b, trg):
    try:
        val.maxy
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast4(val, src, b, trg):
    try:
        val.x
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast10(val, src, b, trg):
    try:
        val.miny
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast17(val, src, b, trg):
    try:
        val.append
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast23(val, src, b, trg):
    try:
        val.GetDomain
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast22(val, src, b, trg):
    try:
        val.splines
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast28(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast29(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast8(val, src, b, trg):
    try:
        val.points
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.__rmul__
        val.x
        val.__repr__
        val.linear_combination
        val.Mag
        val.__mul__
        val.__add__
        val.__str__
        val.dist
        val.y
        val.__sub__
        val.z
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast27(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast26(val, src, b, trg):
    try:
        val.truncate
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast12(val, src, b, trg):
    try:
        val.minx
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast25(val, src, b, trg):
    try:
        val.thickness
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast5(val, src, b, trg):
    try:
        val.y
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.sqrt
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast20(val, src, b, trg):
    try:
        val.randrange
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym645 = Dyn
gensym560 = Function(DynParameters, Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym1186 = Function(AnonymousParameters([]), Dyn)
gensym376 = Dyn
gensym62 = Float
gensym222 = Int
gensym1101 = Float
gensym75 = Dyn
gensym253 = Int
gensym49 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1057 = List(Int)
gensym1181 = Dyn
gensym150 = Dyn
gensym744 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym384 = Dyn
gensym236 = Dyn
gensym371 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym881 = Float
gensym1001 = Float
gensym841 = Float
gensym707 = Dyn
gensym44 = Dyn
gensym640 = Function(AnonymousParameters([]), Dyn)
gensym161 = Int
gensym698 = Tuple(Dyn, Dyn)
gensym636 = Object('', {'splines': Dyn, })
gensym793 = Dyn
gensym109 = Object('', {'x': Dyn, })
gensym481 = Function(AnonymousParameters([Dyn]), Dyn)
gensym611 = Dyn
gensym159 = List(Dyn)
gensym459 = Object('', {'miny': Dyn, })
gensym1059 = List(Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), }))
gensym863 = Float
gensym458 = Dyn
gensym929 = Float
gensym84 = Dyn
gensym502 = Dyn
gensym641 = Dyn
gensym552 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym94 = Dyn
gensym916 = Dyn
gensym829 = Dyn
gensym731 = Dyn
gensym136 = Dyn
gensym476 = Dyn
gensym519 = Function(AnonymousParameters([Dyn]), Dyn)
gensym869 = Float
gensym1028 = Dyn
gensym83 = Dyn
gensym809 = Float
gensym870 = Dyn
gensym29 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), ('other', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym305 = Object('', {'points': Dyn, })
gensym45 = Function(AnonymousParameters([Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })]), Dyn)
gensym946 = Dyn
gensym951 = Float
gensym1113 = Float
gensym8 = Int
gensym1035 = Float
gensym464 = List(Dyn)
gensym110 = Dyn
gensym616 = Function(AnonymousParameters([]), Dyn)
gensym713 = Dyn
gensym537 = Function(AnonymousParameters([Dyn]), Dyn)
gensym606 = Function(AnonymousParameters([]), Dyn)
gensym345 = Object('', {'width': Dyn, })
gensym470 = Int
gensym175 = Function(AnonymousParameters([Dyn]), Dyn)
gensym133 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym765 = Dyn
gensym834 = Dyn
gensym283 = Dyn
gensym346 = Dyn
gensym385 = List(Dyn)
gensym255 = Dyn
gensym70 = Float
gensym599 = Dyn
gensym603 = Dyn
gensym1117 = Float
gensym903 = Float
gensym1175 = Dyn
gensym1009 = Float
gensym73 = Dyn
gensym976 = Dyn
gensym986 = Dyn
gensym473 = Function(AnonymousParameters([Int]), Dyn)
gensym1141 = Float
gensym192 = Int
gensym865 = Float
gensym965 = Float
gensym497 = Object('', {'num_trafos': Dyn, })
gensym374 = Dyn
gensym453 = List(Dyn)
gensym747 = Dyn
gensym974 = Dyn
gensym943 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym701 = Dyn
gensym441 = Object('', {'points': Dyn, })
gensym572 = Object('', {'miny': Dyn, })
gensym52 = Float
gensym178 = Dyn
gensym1090 = Dyn
gensym1008 = Dyn
gensym524 = Dyn
gensym754 = Dyn
gensym193 = Dyn
gensym788 = Function(AnonymousParameters([]), Dyn)
gensym651 = Dyn
gensym647 = Dyn
gensym796 = Function(AnonymousParameters([Dyn]), Dyn)
gensym487 = Dyn
gensym890 = Dyn
gensym772 = Function(AnonymousParameters([Dyn]), Dyn)
gensym941 = Float
gensym1016 = Dyn
gensym101 = Object('', {'y': Dyn, })
gensym770 = Function(AnonymousParameters([Dyn]), Dyn)
gensym710 = Object('', {'splines': Dyn, })
gensym1084 = Dyn
gensym1122 = Dyn
gensym520 = Dyn
gensym1072 = Dyn
gensym717 = Dyn
gensym485 = Dyn
gensym592 = Object('', {'splines': Dyn, })
gensym811 = Int
gensym1064 = Dyn
gensym888 = Dyn
gensym877 = Float
gensym935 = Float
gensym281 = Dyn
gensym609 = Dyn
gensym241 = Dyn
gensym1054 = Dyn
gensym570 = Object('', {'y': Dyn, })
gensym302 = Float
gensym1021 = Float
gensym525 = Int
gensym1152 = Dyn
gensym324 = Dyn
gensym864 = Dyn
gensym960 = Dyn
gensym355 = Object('', {'dist': Dyn, })
gensym444 = Dyn
gensym932 = Dyn
gensym751 = Dyn
gensym297 = Dyn
gensym76 = Float
gensym541 = Object('', {'randrange': Dyn, })
gensym337 = Object('', {'maxy': Dyn, })
gensym787 = Dyn
gensym244 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym323 = Object('', {'x': Dyn, })
gensym723 = Dyn
gensym404 = Dyn
gensym249 = Int
gensym1110 = Dyn
gensym668 = Object('', {'x': Dyn, })
gensym686 = Object('', {'height': Dyn, })
gensym750 = Function(AnonymousParameters([Int]), Dyn)
gensym687 = Dyn
gensym613 = Dyn
gensym439 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym996 = Dyn
gensym588 = Object('', {'splines': Dyn, })
gensym286 = Dyn
gensym40 = Float
gensym1032 = Dyn
gensym393 = List(Dyn)
gensym57 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), ('other', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym792 = Dyn
gensym666 = Object('', {'y': Dyn, })
gensym68 = Float
gensym961 = Float
gensym65 = Dyn
gensym313 = Object('', {'points': Dyn, })
gensym106 = Dyn
gensym936 = Dyn
gensym420 = Dyn
gensym716 = Function(AnonymousParameters([]), Dyn)
gensym100 = Dyn
gensym673 = Dyn
gensym689 = Dyn
gensym625 = Dyn
gensym55 = Dyn
gensym82 = Void
gensym115 = Object('', {'y': Dyn, })
gensym35 = Dyn
gensym352 = Dyn
gensym705 = Dyn
gensym762 = Function(AnonymousParameters([]), Dyn)
gensym769 = Dyn
gensym180 = Dyn
gensym455 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym282 = Int
gensym450 = Dyn
gensym391 = Object('', {'y': Dyn, })
gensym2 = Dyn
gensym913 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym300 = Dyn
gensym1078 = Dyn
gensym483 = Dyn
gensym617 = Dyn
gensym1125 = Float
gensym826 = Function(AnonymousParameters([Dyn]), Dyn)
gensym452 = Dyn
gensym808 = Dyn
gensym97 = Object('', {'x': Dyn, })
gensym491 = Dyn
gensym288 = Dyn
gensym1080 = Dyn
gensym963 = Float
gensym410 = Dyn
gensym602 = Object('', {'y': Dyn, })
gensym508 = Dyn
gensym1185 = Dyn
gensym828 = Function(AnonymousParameters([Dyn]), Dyn)
gensym875 = Float
gensym108 = Dyn
gensym799 = Dyn
gensym695 = Dyn
gensym43 = Function(AnonymousParameters([Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }), Class('GVector', {'__rmul__': Dyn, '__repr__': Function(NamedParameters([('self', TypeVariable('GVector'))]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([('self', TypeVariable('GVector'))]), Float), '__mul__': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([('self', TypeVariable('GVector'))]), Dyn), 'dist': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', TypeVariable('GVector'))]), Float), '__sub__': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__init__': Function(DynParameters, Dyn), }, {'x': Float, 'y': Float, 'z': Float, })]), Dyn)
gensym422 = Dyn
gensym702 = Object('', {'splines': Dyn, })
gensym1171 = List(Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), }))
gensym34 = Float
gensym848 = Dyn
gensym906 = Dyn
gensym58 = Dyn
gensym576 = Object('', {'get_random_trafo': Dyn, })
gensym857 = Float
gensym678 = Object('', {'minx': Dyn, })
gensym181 = Function(AnonymousParameters([Dyn]), Dyn)
gensym746 = Function(NamedParameters([('self', Object('Chaosgame', {'transform_point': Function(DynParameters, Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), 'maxy': Float, 'splines': List(Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), })), 'width': Float, 'thickness': Float, 'height': Float, 'minx': Float, 'create_image_chaos': Function(NamedParameters([('timer', Dyn), ('w', Int), ('h', Int), ('n', Int)]), List(Dyn)), 'num_trafos': List(Int), 'truncate': Function(NamedParameters([('point', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn), 'miny': Float, 'get_random_trafo': Function(NamedParameters([]), Tuple(Int, Int)), 'maxx': Float, 'num_total': Int, })), ('point', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn)
gensym143 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym1178 = Dyn
gensym411 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym1170 = Dyn
gensym311 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym164 = Dyn
gensym860 = Dyn
gensym235 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym369 = List(Dyn)
gensym908 = Dyn
gensym128 = Dyn
gensym275 = Dyn
gensym729 = Dyn
gensym844 = Dyn
gensym1105 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym468 = Dyn
gensym1074 = Dyn
gensym955 = Float
gensym670 = Object('', {'Mag': Dyn, })
gensym1106 = Dyn
gensym1183 = Dyn
gensym1133 = Float
gensym725 = Dyn
gensym336 = Dyn
gensym615 = Dyn
gensym204 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym37 = Dyn
gensym382 = Dyn
gensym598 = Function(AnonymousParameters([Dyn]), Dyn)
gensym993 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym312 = Dyn
gensym177 = Function(AnonymousParameters([String]), Dyn)
gensym1038 = Dyn
gensym276 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym314 = Dyn
gensym138 = Dyn
gensym510 = Dyn
gensym77 = Dyn
gensym433 = Object('', {'points': Dyn, })
gensym309 = List(Dyn)
gensym889 = Float
gensym130 = Dyn
gensym987 = Float
gensym377 = List(Dyn)
gensym1109 = List(Int)
gensym465 = Dyn
gensym209 = Dyn
gensym577 = Dyn
gensym902 = Dyn
gensym634 = Function(AnonymousParameters([]), Dyn)
gensym1120 = Dyn
gensym224 = Int
gensym1043 = Float
gensym1042 = Dyn
gensym813 = Dyn
gensym756 = Dyn
gensym342 = Dyn
gensym339 = Object('', {'miny': Dyn, })
gensym198 = Int
gensym250 = Dyn
gensym759 = Dyn
gensym442 = Dyn
gensym413 = Function(AnonymousParameters([Dyn]), Dyn)
gensym230 = Int
gensym223 = Dyn
gensym1167 = Int
gensym543 = Int
gensym61 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), ('other', Float)]), Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym880 = Dyn
gensym364 = Dyn
gensym886 = Dyn
gensym589 = Dyn
gensym107 = Object('', {'z': Dyn, })
gensym872 = Dyn
gensym1177 = List(Dyn)
gensym816 = Function(AnonymousParameters([]), Dyn)
gensym325 = List(Dyn)
gensym614 = Object('', {'Mag': Dyn, })
gensym630 = Object('', {'height': Dyn, })
gensym60 = Dyn
gensym172 = Dyn
gensym370 = Dyn
gensym1012 = Dyn
gensym820 = Dyn
gensym333 = List(Dyn)
gensym247 = Dyn
gensym1023 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym896 = Dyn
gensym654 = Function(AnonymousParameters([Dyn]), Dyn)
gensym802 = Function(AnonymousParameters([]), Dyn)
gensym781 = Float
gensym1151 = Float
gensym831 = Dyn
gensym466 = Dyn
gensym539 = Int
gensym125 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn)
gensym120 = Dyn
gensym406 = Dyn
gensym145 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym803 = Dyn
gensym303 = Dyn
gensym122 = String
gensym740 = Object('', {'truncate': Dyn, })
gensym619 = Dyn
gensym1058 = Dyn
gensym135 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym418 = Dyn
gensym184 = Dyn
gensym742 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1051 = Float
gensym845 = Float
gensym412 = Dyn
gensym937 = Float
gensym958 = Dyn
gensym78 = Float
gensym290 = Dyn
gensym335 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym1111 = Float
gensym649 = Dyn
gensym1148 = Dyn
gensym233 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym362 = Dyn
gensym917 = List(Int)
gensym127 = Dyn
gensym1154 = Dyn
gensym240 = Int
gensym268 = Function(NamedParameters([('self', Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), })), ('u', Float)]), Int)
gensym989 = Float
gensym480 = Dyn
gensym332 = Dyn
gensym1149 = Float
gensym1031 = Float
gensym774 = Function(AnonymousParameters([]), Dyn)
gensym408 = Dyn
gensym780 = Dyn
gensym123 = Dyn
gensym1169 = List(Int)
gensym1005 = Float
gensym392 = Dyn
gensym1014 = Dyn
gensym871 = Float
gensym967 = Float
gensym952 = Dyn
gensym96 = Dyn
gensym944 = Dyn
gensym894 = Dyn
gensym394 = Dyn
gensym478 = Dyn
gensym167 = List(Dyn)
gensym1034 = Dyn
gensym947 = List(Int)
gensym1065 = Float
gensym330 = Dyn
gensym659 = Dyn
gensym1030 = Dyn
gensym317 = List(Dyn)
gensym862 = Dyn
gensym730 = Object('', {'x': Dyn, })
gensym985 = Float
gensym842 = Dyn
gensym344 = Dyn
gensym112 = Dyn
gensym990 = Dyn
gensym971 = Float
gensym964 = Dyn
gensym174 = Dyn
gensym448 = Dyn
gensym523 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1027 = List(Int)
gensym688 = Object('', {'get_random_trafo': Dyn, })
gensym426 = Dyn
gensym767 = Dyn
gensym708 = Function(AnonymousParameters([Dyn]), Dyn)
gensym753 = Float
gensym213 = Dyn
gensym1029 = Float
gensym997 = List(Int)
gensym843 = Float
gensym920 = Dyn
gensym6 = Int
gensym117 = Object('', {'z': Dyn, })
gensym191 = Dyn
gensym1179 = Dyn
gensym416 = Dyn
gensym486 = Object('', {'append': Dyn, })
gensym388 = Dyn
gensym1094 = Dyn
gensym853 = Float
gensym18 = Dyn
gensym895 = Float
gensym531 = Function(AnonymousParameters([Dyn]), Dyn)
gensym267 = Dyn
gensym36 = Float
gensym306 = Dyn
gensym1081 = Float
gensym327 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym574 = Object('', {'height': Dyn, })
gensym919 = Float
gensym162 = Dyn
gensym814 = Function(AnonymousParameters([Int]), Dyn)
gensym665 = Dyn
gensym778 = List(List(Int))
gensym447 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym569 = Dyn
gensym652 = Object('', {'splines': Dyn, })
gensym153 = Function(DynParameters, Dyn)
gensym580 = Object('', {'splines': Dyn, })
gensym329 = Object('', {'points': Dyn, })
gensym1039 = Float
gensym837 = Dyn
gensym940 = Dyn
gensym591 = Dyn
gensym812 = Dyn
gensym141 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym994 = Dyn
gensym661 = Dyn
gensym966 = Dyn
gensym414 = Dyn
gensym451 = Object('', {'y': Dyn, })
gensym1190 = Object('', {'num_runs': Dyn, })
gensym752 = List(List(Int))
gensym927 = Float
gensym1112 = Dyn
gensym503 = Object('', {'randrange': Dyn, })
gensym882 = Dyn
gensym1086 = Dyn
gensym597 = Dyn
gensym169 = Int
gensym969 = Float
gensym850 = Dyn
gensym41 = Dyn
gensym839 = Dyn
gensym349 = Function(AnonymousParameters([Int]), Dyn)
gensym764 = Function(AnonymousParameters([Int]), Dyn)
gensym221 = Dyn
gensym469 = Object('', {'height': Dyn, })
gensym975 = Float
gensym1047 = Float
gensym46 = Dyn
gensym10 = Int
gensym1132 = Dyn
gensym445 = List(Dyn)
gensym782 = Dyn
gensym1 = Object('', {'seed': Dyn, })
gensym166 = Dyn
gensym1107 = Int
gensym1087 = Float
gensym1191 = Function(NamedParameters([('n', Dyn), ('timer', Dyn)]), Dyn)
gensym887 = List(Int)
gensym291 = Function(AnonymousParameters([List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn)
gensym984 = Dyn
gensym26 = Dyn
gensym189 = Dyn
gensym1022 = Dyn
gensym643 = Dyn
gensym672 = Function(AnonymousParameters([]), Dyn)
gensym301 = Function(DynParameters, Dyn)
gensym203 = Dyn
gensym648 = Object('', {'splines': Dyn, })
gensym1123 = Float
gensym786 = Function(AnonymousParameters([Int]), Dyn)
gensym1010 = Dyn
gensym1036 = Dyn
gensym489 = Dyn
gensym287 = Int
gensym32 = Float
gensym626 = Object('', {'y': Dyn, })
gensym142 = Dyn
gensym977 = Float
gensym88 = Dyn
gensym575 = Dyn
gensym555 = Dyn
gensym1077 = Float
gensym1024 = Dyn
gensym692 = Object('', {'splines': Dyn, })
gensym548 = Dyn
gensym477 = Function(AnonymousParameters([Dyn]), Dyn)
gensym113 = Object('', {'y': Dyn, })
gensym1173 = Float
gensym66 = Float
gensym1104 = Dyn
gensym1172 = Dyn
gensym358 = Dyn
gensym293 = Int
gensym1085 = Float
gensym1068 = Dyn
gensym878 = Dyn
gensym835 = Function(AnonymousParameters([]), Dyn)
gensym972 = Dyn
gensym93 = Object('', {'z': Dyn, })
gensym866 = Dyn
gensym962 = Dyn
gensym1092 = Dyn
gensym434 = Dyn
gensym637 = Dyn
gensym948 = Dyn
gensym734 = Function(AnonymousParameters([]), Dyn)
gensym1004 = Dyn
gensym438 = Dyn
gensym1162 = Dyn
gensym693 = Dyn
gensym409 = Function(AnonymousParameters([Int]), Dyn)
gensym585 = Dyn
gensym593 = Dyn
gensym421 = Object('', {'num_trafos': Dyn, })
gensym1002 = Dyn
gensym1070 = Dyn
gensym897 = Float
gensym1097 = Float
gensym901 = Float
gensym356 = Dyn
gensym595 = Dyn
gensym348 = Dyn
gensym104 = Dyn
gensym199 = Dyn
gensym430 = Dyn
gensym1067 = Float
gensym779 = Float
gensym156 = Void
gensym583 = Dyn
gensym28 = Dyn
gensym683 = Dyn
gensym31 = Dyn
gensym655 = Dyn
gensym534 = Dyn
gensym1044 = Dyn
gensym696 = Function(AnonymousParameters([]), Dyn)
gensym215 = Dyn
gensym296 = String
gensym205 = Dyn
gensym949 = Float
gensym755 = Float
gensym861 = Float
gensym867 = Float
gensym682 = Object('', {'y': Dyn, })
gensym777 = Dyn
gensym800 = Int
gensym892 = Dyn
gensym807 = Float
gensym1052 = Dyn
gensym307 = Object('', {'x': Dyn, })
gensym225 = Dyn
gensym1102 = Dyn
gensym25 = Function(AnonymousParameters([Float]), Dyn)
gensym11 = Dyn
gensym328 = Dyn
gensym200 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym680 = Object('', {'width': Dyn, })
gensym208 = Function(AnonymousParameters([Dyn, Dyn, Dyn]), Dyn)
gensym621 = Dyn
gensym1088 = Dyn
gensym627 = Dyn
gensym578 = Function(AnonymousParameters([]), Dyn)
gensym758 = Dyn
gensym0 = Dyn
gensym738 = Dyn
gensym431 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym1076 = Dyn
gensym564 = Object('', {'x': Dyn, })
gensym832 = Int
gensym501 = Function(NamedParameters([('self', Object('Chaosgame', {'transform_point': Function(DynParameters, Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), 'maxy': Float, 'splines': List(Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), })), 'width': Float, 'thickness': Float, 'height': Float, 'minx': Float, 'create_image_chaos': Function(NamedParameters([('timer', Dyn), ('w', Int), ('h', Int), ('n', Int)]), List(Dyn)), 'num_trafos': List(Int), 'truncate': Function(NamedParameters([('point', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn), 'miny': Float, 'get_random_trafo': Function(NamedParameters([]), Tuple(Int, Int)), 'maxx': Float, 'num_total': Int, }))]), Tuple(Int, Int))
gensym775 = Dyn
gensym1071 = Float
gensym514 = Dyn
gensym474 = Dyn
gensym72 = Float
gensym676 = Object('', {'x': Dyn, })
gensym876 = Dyn
gensym170 = List(Int)
gensym375 = Object('', {'y': Dyn, })
gensym662 = Function(AnonymousParameters([]), Dyn)
gensym1135 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym152 = Dyn
gensym810 = Dyn
gensym795 = Dyn
gensym95 = Object('', {'z': Dyn, })
gensym1153 = Float
gensym190 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym724 = Function(AnonymousParameters([]), Dyn)
gensym840 = Function(NamedParameters([('n', Dyn), ('timer', Dyn)]), Dyn)
gensym318 = Dyn
gensym1049 = Float
gensym945 = Int
gensym429 = List(Dyn)
gensym24 = Dyn
gensym15 = Object('', {'sqrt': Dyn, })
gensym743 = Dyn
gensym231 = Dyn
gensym957 = Float
gensym553 = Dyn
gensym535 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym1160 = Dyn
gensym852 = Dyn
gensym129 = Class('GVector', {'__rmul__': Dyn, '__repr__': Function(NamedParameters([('self', TypeVariable('GVector'))]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([('self', TypeVariable('GVector'))]), Float), '__mul__': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([('self', TypeVariable('GVector'))]), Dyn), 'dist': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', TypeVariable('GVector'))]), Float), '__sub__': Function(NamedParameters([('self', TypeVariable('GVector')), ('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__init__': Function(DynParameters, Dyn), }, {'x': Float, 'y': Float, 'z': Float, })
gensym981 = Float
gensym389 = Object('', {'points': Dyn, })
gensym1100 = Dyn
gensym463 = Object('', {'minx': Dyn, })
gensym846 = Dyn
gensym252 = Int
gensym632 = Object('', {'get_random_trafo': Dyn, })
gensym646 = Function(AnonymousParameters([Dyn]), Dyn)
gensym938 = Dyn
gensym736 = Object('', {'thickness': Dyn, })
gensym1129 = Float
gensym1138 = Dyn
gensym1082 = Dyn
gensym847 = Float
gensym379 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym98 = Dyn
gensym228 = Dyn
gensym378 = Dyn
gensym1045 = Float
gensym612 = Object('', {'x': Dyn, })
gensym1144 = Dyn
gensym970 = Dyn
gensym499 = Function(AnonymousParameters([Dyn, Dyn, Int]), Dyn)
gensym562 = Dyn
gensym361 = Object('', {'num_trafos': Dyn, })
gensym657 = Dyn
gensym783 = Int
gensym134 = Dyn
gensym885 = Int
gensym319 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym400 = Dyn
gensym12 = Dyn
gensym930 = Dyn
gensym1128 = Dyn
gensym590 = Function(AnonymousParameters([Dyn]), Dyn)
gensym269 = Dyn
gensym144 = Dyn
gensym399 = Object('', {'miny': Dyn, })
gensym748 = Function(NamedParameters([('self', Object('Chaosgame', {'transform_point': Function(DynParameters, Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), 'maxy': Float, 'splines': List(Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), })), 'width': Float, 'thickness': Float, 'height': Float, 'minx': Float, 'create_image_chaos': Function(NamedParameters([('timer', Dyn), ('w', Int), ('h', Int), ('n', Int)]), List(Dyn)), 'num_trafos': List(Int), 'truncate': Function(NamedParameters([('point', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn), 'miny': Float, 'get_random_trafo': Function(NamedParameters([]), Tuple(Int, Int)), 'maxx': Float, 'num_total': Int, })), ('timer', Dyn), ('w', Int), ('h', Int), ('n', Int)]), List(Dyn))
gensym749 = Dyn
gensym210 = Function(AnonymousParameters([Int]), Dyn)
gensym979 = Float
gensym398 = Dyn
gensym509 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym838 = Class('Chaosgame', {'transform_point': Function(DynParameters, Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), 'truncate': Function(NamedParameters([('self', TypeVariable('Chaosgame')), ('point', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn), 'create_image_chaos': Function(NamedParameters([('self', TypeVariable('Chaosgame')), ('timer', Dyn), ('w', Int), ('h', Int), ('n', Int)]), List(Dyn)), '__init__': Function(DynParameters, Dyn), 'get_random_trafo': Function(NamedParameters([('self', TypeVariable('Chaosgame'))]), Tuple(Int, Int)), }, {'maxy': Float, 'splines': List(Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), })), 'height': Float, 'minx': Float, 'num_trafos': List(Int), 'width': Float, 'miny': Float, 'thickness': Float, 'maxx': Float, 'num_total': Int, })
gensym921 = Float
gensym257 = Dyn
gensym380 = Dyn
gensym722 = Object('', {'Mag': Dyn, })
gensym1041 = Float
gensym804 = Function(AnonymousParameters([Int]), Dyn)
gensym353 = Function(AnonymousParameters([Dyn]), Dyn)
gensym21 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), ('other', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Float)
gensym105 = Object('', {'z': Dyn, })
gensym656 = Object('', {'x': Dyn, })
gensym407 = Object('', {'height': Dyn, })
gensym823 = Float
gensym1025 = Int
gensym950 = Dyn
gensym304 = Dyn
gensym587 = Dyn
gensym155 = Dyn
gensym227 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym321 = Object('', {'points': Dyn, })
gensym484 = Object('', {'num_trafos': Dyn, })
gensym271 = Dyn
gensym315 = Object('', {'y': Dyn, })
gensym530 = Dyn
gensym1146 = Dyn
gensym776 = Function(AnonymousParameters([Int]), Dyn)
gensym1118 = Dyn
gensym545 = Function(AnonymousParameters([Int]), Dyn)
gensym988 = Dyn
gensym50 = Float
gensym316 = Dyn
gensym818 = Function(AnonymousParameters([Int]), Dyn)
gensym42 = Dyn
gensym435 = Object('', {'y': Dyn, })
gensym1037 = Float
gensym973 = Float
gensym1161 = Float
gensym479 = Object('', {'dist': Dyn, })
gensym540 = Dyn
gensym449 = Object('', {'points': Dyn, })
gensym1096 = Dyn
gensym160 = Dyn
gensym737 = String
gensym771 = Dyn
gensym1062 = Dyn
gensym785 = Dyn
gensym922 = Dyn
gensym383 = Object('', {'x': Dyn, })
gensym258 = Int
gensym806 = List(List(Int))
gensym685 = Dyn
gensym196 = Function(AnonymousParameters([Int]), Dyn)
gensym909 = Float
gensym822 = Dyn
gensym1011 = Float
gensym33 = Dyn
gensym675 = Dyn
gensym295 = Function(NamedParameters([('self', Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), }))]), Dyn)
gensym151 = List(Int)
gensym121 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Dyn)
gensym437 = List(Dyn)
gensym4 = Dyn
gensym270 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym905 = Float
gensym308 = Dyn
gensym386 = Dyn
gensym16 = Dyn
gensym1168 = Dyn
gensym642 = Object('', {'num_trafos': Dyn, })
gensym118 = Dyn
gensym608 = Object('', {'thickness': Dyn, })
gensym671 = Dyn
gensym338 = Dyn
gensym907 = Float
gensym925 = Float
gensym405 = Object('', {'width': Dyn, })
gensym1188 = Tuple(Dyn, Dyn)
gensym528 = Dyn
gensym163 = List(Dyn)
gensym1182 = Function(DynParameters, Dyn)
gensym1184 = Object('', {'parse_args': Dyn, })
gensym334 = Dyn
gensym859 = Float
gensym326 = Dyn
gensym216 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym238 = Function(AnonymousParameters([Int]), Dyn)
gensym182 = Dyn
gensym171 = Dyn
gensym234 = Dyn
gensym147 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym558 = Tuple(Int, Int)
gensym219 = Dyn
gensym554 = Object('', {'randrange': Dyn, })
gensym71 = Dyn
gensym460 = Dyn
gensym350 = Dyn
gensym741 = Dyn
gensym292 = Dyn
gensym260 = Dyn
gensym299 = Class('Spline', {'GetDomain': Function(NamedParameters([('self', TypeVariable('Spline'))]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('self', TypeVariable('Spline')), ('u', Float)]), Dyn), '__len__': Function(NamedParameters([('self', TypeVariable('Spline'))]), Int), '__init__': Function(DynParameters, Dyn), 'GetIndex': Function(NamedParameters([('self', TypeVariable('Spline')), ('u', Float)]), Int), '__repr__': Function(NamedParameters([('self', TypeVariable('Spline'))]), Dyn), }, {'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), 'knots': List(Int), 'degree': Int, })
gensym1013 = Float
gensym959 = Float
gensym417 = Function(AnonymousParameters([Dyn]), Dyn)
gensym733 = Dyn
gensym581 = Dyn
gensym27 = Float
gensym239 = Dyn
gensym331 = Object('', {'y': Dyn, })
gensym357 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1158 = Dyn
gensym116 = Dyn
gensym791 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym220 = Int
gensym532 = Int
gensym1155 = Float
gensym600 = Object('', {'x': Dyn, })
gensym571 = Dyn
gensym436 = Dyn
gensym89 = Object('', {'y': Dyn, })
gensym1050 = Dyn
gensym446 = Dyn
gensym1140 = Dyn
gensym522 = Dyn
gensym1150 = Dyn
gensym898 = Dyn
gensym547 = Tuple(Int, Int)
gensym1126 = Dyn
gensym279 = Dyn
gensym1159 = Float
gensym310 = Dyn
gensym365 = Object('', {'points': Dyn, })
gensym1003 = Float
gensym709 = Dyn
gensym366 = Dyn
gensym855 = Float
gensym1006 = Dyn
gensym363 = Function(AnonymousParameters([Dyn, Dyn, Int]), Dyn)
gensym211 = Dyn
gensym86 = Dyn
gensym1018 = Dyn
gensym559 = Dyn
gensym401 = Object('', {'maxx': Dyn, })
gensym635 = Dyn
gensym546 = Tuple(Dyn, Dyn)
gensym879 = Float
gensym760 = Function(AnonymousParameters([Int]), Dyn)
gensym1053 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym395 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym277 = Dyn
gensym139 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym1033 = Float
gensym1157 = Float
gensym817 = Dyn
gensym188 = Function(NamedParameters([('self', Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), }))]), Tuple(Int, Int))
gensym1073 = Float
gensym991 = Float
gensym594 = Function(AnonymousParameters([Dyn]), Dyn)
gensym246 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym549 = Int
gensym368 = Dyn
gensym149 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym207 = Dyn
gensym517 = Function(AnonymousParameters([Int]), Dyn)
gensym934 = Dyn
gensym669 = Dyn
gensym1134 = Dyn
gensym605 = Dyn
gensym1124 = Dyn
gensym102 = Dyn
gensym1116 = Dyn
gensym5 = Function(DynParameters, Dyn)
gensym13 = Function(NamedParameters([('self', Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))]), Float)
gensym53 = Dyn
gensym1015 = Float
gensym284 = Int
gensym492 = Function(AnonymousParameters([Dyn]), Dyn)
gensym739 = Dyn
gensym891 = Float
gensym67 = Dyn
gensym237 = Dyn
gensym874 = Dyn
gensym201 = Dyn
gensym85 = Object('', {'x': Dyn, })
gensym69 = Dyn
gensym1089 = Float
gensym933 = Float
gensym1020 = Dyn
gensym187 = Dyn
gensym623 = Dyn
gensym1007 = Float
gensym658 = Object('', {'y': Dyn, })
gensym1017 = Float
gensym1095 = Float
gensym763 = Dyn
gensym454 = Dyn
gensym124 = Dyn
gensym424 = Dyn
gensym1103 = Float
gensym978 = Dyn
gensym359 = Object('', {'add': Dyn, })
gensym1174 = Dyn
gensym1137 = Int
gensym883 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym59 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym87 = Object('', {'x': Dyn, })
gensym195 = Dyn
gensym924 = Dyn
gensym38 = Float
gensym132 = Dyn
gensym111 = Object('', {'x': Dyn, })
gensym801 = Dyn
gensym660 = Object('', {'Mag': Dyn, })
gensym596 = Object('', {'splines': Dyn, })
gensym30 = Float
gensym214 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym703 = Dyn
gensym322 = Dyn
gensym538 = Dyn
gensym126 = String
gensym784 = Dyn
gensym563 = Dyn
gensym697 = Dyn
gensym773 = Dyn
gensym706 = Object('', {'splines': Dyn, })
gensym956 = Dyn
gensym633 = Dyn
gensym650 = Function(AnonymousParameters([Dyn]), Dyn)
gensym691 = Dyn
gensym119 = Object('', {'z': Dyn, })
gensym529 = Function(AnonymousParameters([Int]), Dyn)
gensym262 = Int
gensym1000 = Dyn
gensym280 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym931 = Float
gensym1139 = List(Int)
gensym824 = Dyn
gensym604 = Object('', {'Mag': Dyn, })
gensym995 = Int
gensym298 = Dyn
gensym20 = Dyn
gensym536 = Dyn
gensym584 = Function(AnonymousParameters([]), Dyn)
gensym1115 = Float
gensym402 = Dyn
gensym664 = Object('', {'thickness': Dyn, })
gensym146 = Dyn
gensym1061 = Float
gensym900 = Dyn
gensym511 = Function(AnonymousParameters([Dyn]), Dyn)
gensym620 = Object('', {'x': Dyn, })
gensym1083 = Float
gensym1091 = Float
gensym910 = Dyn
gensym396 = Dyn
gensym953 = Float
gensym81 = Function(DynParameters, Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym1166 = Dyn
gensym815 = Dyn
gensym663 = Dyn
gensym500 = Dyn
gensym821 = Float
gensym1147 = Float
gensym515 = Object('', {'randrange': Dyn, })
gensym794 = Function(AnonymousParameters([Dyn]), Dyn)
gensym103 = Object('', {'y': Dyn, })
gensym48 = Dyn
gensym1165 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym518 = Dyn
gensym423 = Function(AnonymousParameters([Dyn, Dyn, Int]), Dyn)
gensym622 = Object('', {'minx': Dyn, })
gensym999 = Float
gensym505 = Function(AnonymousParameters([Int]), Dyn)
gensym397 = Object('', {'maxy': Dyn, })
gensym704 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1142 = Dyn
gensym504 = Dyn
gensym340 = Dyn
gensym1019 = Float
gensym912 = Dyn
gensym1056 = Dyn
gensym456 = Dyn
gensym206 = Object('', {'linear_combination': Dyn, })
gensym573 = Dyn
gensym467 = Object('', {'width': Dyn, })
gensym47 = Function(AnonymousParameters([Dyn]), Dyn)
gensym496 = Dyn
gensym711 = Dyn
gensym242 = List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, }))
gensym381 = Object('', {'points': Dyn, })
gensym461 = Object('', {'maxx': Dyn, })
gensym1145 = Float
gensym915 = Int
gensym610 = Object('', {'y': Dyn, })
gensym873 = Float
gensym173 = Function(AnonymousParameters([Dyn]), Dyn)
gensym218 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym294 = Dyn
gensym968 = Dyn
gensym419 = Object('', {'add': Dyn, })
gensym677 = Dyn
gensym148 = Dyn
gensym1026 = Dyn
gensym720 = Object('', {'y': Dyn, })
gensym494 = Dyn
gensym566 = Object('', {'minx': Dyn, })
gensym712 = Function(AnonymousParameters([Dyn]), Dyn)
gensym185 = Function(AnonymousParameters([String]), Dyn)
gensym718 = Object('', {'x': Dyn, })
gensym256 = Int
gensym157 = Dyn
gensym19 = Float
gensym856 = Dyn
gensym272 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym1187 = Dyn
gensym360 = Dyn
gensym653 = Dyn
gensym521 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym248 = Int
gensym628 = Object('', {'miny': Dyn, })
gensym942 = Dyn
gensym805 = Dyn
gensym498 = Dyn
gensym245 = Dyn
gensym17 = Function(AnonymousParameters([Float]), Dyn)
gensym39 = Dyn
gensym131 = Function(NamedParameters([('points', List(Dyn)), ('degree', Int)]), List(Int))
gensym674 = Object('', {'thickness': Dyn, })
gensym367 = Object('', {'x': Dyn, })
gensym939 = Float
gensym757 = Int
gensym851 = Float
gensym495 = Object('', {'add': Dyn, })
gensym1119 = Float
gensym23 = Object('', {'sqrt': Dyn, })
gensym582 = Object('', {'GetDomain': Dyn, })
gensym176 = Dyn
gensym1192 = Dyn
gensym726 = Object('', {'thickness': Dyn, })
gensym923 = Float
gensym727 = Dyn
gensym928 = Dyn
gensym1164 = Dyn
gensym443 = Object('', {'x': Dyn, })
gensym194 = Function(NamedParameters([('self', Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), })), ('u', Float)]), Dyn)
gensym273 = Dyn
gensym690 = Function(AnonymousParameters([]), Dyn)
gensym644 = Object('', {'splines': Dyn, })
gensym904 = Dyn
gensym694 = Object('', {'GetDomain': Dyn, })
gensym254 = Dyn
gensym639 = Dyn
gensym768 = Object('', {'y': Dyn, })
gensym373 = Object('', {'points': Dyn, })
gensym1127 = Float
gensym490 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym854 = Dyn
gensym830 = Int
gensym472 = Dyn
gensym488 = Function(AnonymousParameters([Dyn]), Dyn)
gensym868 = Dyn
gensym462 = Dyn
gensym1069 = Float
gensym858 = Dyn
gensym700 = Object('', {'num_trafos': Dyn, })
gensym475 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym728 = Object('', {'y': Dyn, })
gensym341 = Object('', {'maxx': Dyn, })
gensym266 = Dyn
gensym568 = Object('', {'width': Dyn, })
gensym74 = Float
gensym432 = Dyn
gensym1121 = Float
gensym403 = Object('', {'minx': Dyn, })
gensym565 = Dyn
gensym1143 = Float
gensym14 = Dyn
gensym168 = Dyn
gensym140 = Dyn
gensym320 = Dyn
gensym884 = Dyn
gensym631 = Dyn
gensym551 = Dyn
gensym542 = Dyn
gensym607 = Dyn
gensym1098 = Dyn
gensym513 = Int
gensym638 = Object('', {'GetDomain': Dyn, })
gensym1060 = Dyn
gensym64 = Float
gensym1189 = Dyn
gensym1055 = Int
gensym914 = Dyn
gensym79 = Dyn
gensym1180 = Object('', {'OptionParser': Dyn, })
gensym679 = Dyn
gensym561 = Void
gensym667 = Dyn
gensym347 = Object('', {'height': Dyn, })
gensym158 = Dyn
gensym526 = Dyn
gensym56 = Dyn
gensym354 = Dyn
gensym372 = Dyn
gensym982 = Dyn
gensym789 = Dyn
gensym1108 = Dyn
gensym567 = Dyn
gensym745 = Dyn
gensym516 = Dyn
gensym63 = Dyn
gensym1099 = Float
gensym226 = Int
gensym261 = Dyn
gensym202 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym714 = Object('', {'Mag': Dyn, })
gensym251 = Dyn
gensym232 = Function(AnonymousParameters([String]), Dyn)
gensym80 = Dyn
gensym684 = Object('', {'miny': Dyn, })
gensym54 = Float
gensym715 = Dyn
gensym165 = Int
gensym556 = Function(AnonymousParameters([Int]), Dyn)
gensym629 = Dyn
gensym137 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym507 = Function(AnonymousParameters([Dyn]), Dyn)
gensym274 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym1156 = Dyn
gensym183 = Function(AnonymousParameters([String]), Dyn)
gensym1075 = Float
gensym428 = Dyn
gensym1066 = Dyn
gensym90 = Dyn
gensym1130 = Dyn
gensym427 = Object('', {'x': Dyn, })
gensym579 = Dyn
gensym954 = Dyn
gensym761 = Dyn
gensym351 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym212 = Int
gensym1046 = Dyn
gensym827 = Dyn
gensym197 = Dyn
gensym440 = Dyn
gensym7 = Dyn
gensym471 = Dyn
gensym289 = Function(NamedParameters([('self', Object('Spline', {'GetDomain': Function(NamedParameters([]), Tuple(Int, Int)), '__call__': Function(NamedParameters([('u', Float)]), Dyn), 'knots': List(Int), 'degree': Int, 'GetIndex': Function(NamedParameters([('u', Float)]), Int), 'points': List(Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })), '__repr__': Function(NamedParameters([]), Dyn), '__len__': Function(NamedParameters([]), Int), }))]), Int)
gensym1176 = Int
gensym735 = Dyn
gensym51 = Dyn
gensym766 = Object('', {'x': Dyn, })
gensym114 = Dyn
gensym259 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym911 = Float
gensym926 = Dyn
gensym1063 = Float
gensym415 = Object('', {'dist': Dyn, })
gensym544 = Dyn
gensym92 = Dyn
gensym217 = Dyn
gensym899 = Float
gensym992 = Dyn
gensym533 = Dyn
gensym918 = Dyn
gensym265 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym1136 = Dyn
gensym243 = Dyn
gensym1163 = Float
gensym732 = Object('', {'Mag': Dyn, })
gensym798 = Int
gensym719 = Dyn
gensym1093 = Float
gensym980 = Dyn
gensym229 = Dyn
gensym390 = Dyn
gensym586 = Object('', {'num_trafos': Dyn, })
gensym3 = Function(AnonymousParameters([Int]), Dyn)
gensym278 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym512 = Dyn
gensym457 = Object('', {'maxy': Dyn, })
gensym9 = Dyn
gensym849 = Float
gensym1079 = Float
gensym618 = Object('', {'thickness': Dyn, })
gensym1040 = Dyn
gensym825 = Dyn
gensym527 = Object('', {'randrange': Dyn, })
gensym790 = Function(AnonymousParameters([Int]), Dyn)
gensym681 = Dyn
gensym983 = Float
gensym154 = Int
gensym22 = Dyn
gensym1114 = Dyn
gensym91 = Object('', {'y': Dyn, })
gensym99 = Object('', {'x': Dyn, })
gensym557 = Tuple(Dyn, Dyn)
gensym387 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym1048 = Dyn
gensym601 = Dyn
gensym998 = Dyn
gensym699 = Dyn
gensym1131 = Float
gensym721 = Dyn
gensym343 = Object('', {'minx': Dyn, })
gensym506 = Dyn
gensym179 = Function(AnonymousParameters([Dyn]), Dyn)
gensym425 = Object('', {'points': Dyn, })
gensym624 = Object('', {'width': Dyn, })
gensym819 = Object('GVector', {'__rmul__': Dyn, 'x': Float, '__repr__': Function(NamedParameters([]), Dyn), 'linear_combination': Function(DynParameters, TypeVariable('GVector')), 'Mag': Function(NamedParameters([]), Float), '__mul__': Function(NamedParameters([('other', Float)]), TypeVariable('GVector')), '__add__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), '__str__': Function(NamedParameters([]), Dyn), 'dist': Function(NamedParameters([('other', TypeVariable('GVector'))]), Float), 'y': Float, '__sub__': Function(NamedParameters([('other', TypeVariable('GVector'))]), TypeVariable('GVector')), 'z': Float, })
gensym797 = Dyn
gensym893 = Float
import operator
import optparse
import random
mgd_cast_type_function(cast0(random, gensym0, '11', gensym1).seed, gensym2, '11', gensym3)(1234)
import math
import os
import sys
import time
from compat import print_, reduce, xrange


class GVector(retic_actual(object)):

    def __init__(self, x=mgd_cast_type_dyn(0, gensym6, '21', gensym7), y=mgd_cast_type_dyn(0, gensym8, '21', gensym9), z=mgd_cast_type_dyn(0, gensym10, '21', gensym11)):
        self.x = x
        self.y = y
        self.z = z

    def Mag(self):
        check1(self, self.Mag, (1, 0))
        return mgd_cast_type_float(mgd_cast_type_function(cast2(math, gensym14, '27', gensym15).sqrt, gensym16, '27', gensym17)((((mgd_check_type_float(self.x, self, (0, 'x')) ** 2) + (mgd_check_type_float(self.y, self, (0, 'y')) ** 2)) + (mgd_check_type_float(self.z, self, (0, 'z')) ** 2))), gensym18, '27', gensym19)

    def dist(self, other):
        check1(self, self.dist, (1, 0))
        check1(other, self.dist, (1, 1))
        return mgd_cast_type_float(mgd_cast_type_function(cast2(math, gensym22, '30', gensym23).sqrt, gensym24, '30', gensym25)(((((mgd_check_type_float(self.x, self, (0, 'x')) - mgd_check_type_float(other.x, other, (0, 'x'))) ** 2) + ((mgd_check_type_float(self.y, self, (0, 'y')) - mgd_check_type_float(other.y, other, (0, 'y'))) ** 2)) + ((mgd_check_type_float(self.z, self, (0, 'z')) - mgd_check_type_float(other.z, other, (0, 'z'))) ** 2))), gensym26, '30', gensym27)

    def __add__(self, other):
        check1(self, self.__add__, (1, 0))
        check1(other, self.__add__, (1, 1))
        if (not mgd_cast_type_function(isinstance, gensym42, '35', gensym43)(other, GVector)):
            raise mgd_cast_type_function(ValueError, gensym48, '36', gensym49)(("Can't add GVector to " + mgd_cast_type_function(str, gensym46, '36', gensym47)(mgd_cast_type_function(type, gensym44, '36', gensym45)(other))))
        v = check1(GVector(mgd_cast_type_dyn((mgd_check_type_float(self.x, self, (0, 'x')) + mgd_check_type_float(other.x, other, (0, 'x'))), gensym50, '37', gensym51), mgd_cast_type_dyn((mgd_check_type_float(self.y, self, (0, 'y')) + mgd_check_type_float(other.y, other, (0, 'y'))), gensym52, '37', gensym53), mgd_cast_type_dyn((mgd_check_type_float(self.z, self, (0, 'z')) + mgd_check_type_float(other.z, other, (0, 'z'))), gensym54, '37', gensym55)), GVector, 2)
        return v

    def __sub__(self, other):
        check1(self, self.__sub__, (1, 0))
        check1(other, self.__sub__, (1, 1))
        return cast3((self + (other * (- 1))), gensym58, '41', gensym59)

    def __mul__(self, other):
        check1(self, self.__mul__, (1, 0))
        mgd_check_type_float(other, self.__mul__, (1, 1))
        v = check1(GVector(mgd_cast_type_dyn((mgd_check_type_float(self.x, self, (0, 'x')) * other), gensym74, '44', gensym75), mgd_cast_type_dyn((mgd_check_type_float(self.y, self, (0, 'y')) * other), gensym76, '44', gensym77), mgd_cast_type_dyn((mgd_check_type_float(self.z, self, (0, 'z')) * other), gensym78, '44', gensym79)), GVector, 2)
        return v
    __rmul__ = __mul__

    def linear_combination(self, other, l1, l2=mgd_cast_type_dyn(None, gensym82, '48', gensym83)):
        if (l2 is None):
            l2 = (1 - l1)
        v = check1(GVector(((cast4(self, gensym108, '51', gensym109).x * l1) + (cast4(other, gensym110, '51', gensym111).x * l2)), ((cast5(self, gensym112, '52', gensym113).y * l1) + (cast5(other, gensym114, '52', gensym115).y * l2)), ((cast6(self, gensym116, '53', gensym117).z * l1) + (cast6(other, gensym118, '53', gensym119).z * l2))), GVector, 2)
        return v

    def __str__(self):
        check1(self, self.__str__, (1, 0))
        return mgd_cast_type_dyn(('<%f, %f, %f>' % (mgd_check_type_float(self.x, self, (0, 'x')), mgd_check_type_float(self.y, self, (0, 'y')), mgd_check_type_float(self.z, self, (0, 'z')))), gensym122, '58', gensym123)

    def __repr__(self):
        check1(self, self.__repr__, (1, 0))
        return mgd_cast_type_dyn(('GVector(%f, %f, %f)' % (mgd_check_type_float(self.x, self, (0, 'x')), mgd_check_type_float(self.y, self, (0, 'y')), mgd_check_type_float(self.z, self, (0, 'z')))), gensym126, '61', gensym127)
GVector = mgd_cast_type_class(GVector, gensym128, '19', gensym129, ['__rmul__', '__repr__', 'linear_combination', 'Mag', '__mul__', '__add__', '__str__', 'dist', '__sub__', '__init__'])

def GetKnots(points, degree):
    mgd_check_type_list(points, GetKnots, (1, 0))
    mgd_check_type_int(degree, GetKnots, (1, 1))
    knots = (([0] * degree) + mgd_cast_type_function(range, gensym146, '64', gensym147)(1, (mgd_cast_type_function(len, gensym144, '64', gensym145)(points) - degree)))
    knots = (knots + ([(mgd_cast_type_function(len, gensym148, '65', gensym149)(points) - degree)] * degree))
    return mgd_cast_type_list(knots, gensym150, '66', gensym151)


class Spline(retic_actual(object)):

    def __init__(self, points, degree=mgd_cast_type_dyn(3, gensym154, '71', gensym155), knots=mgd_cast_type_dyn(None, gensym156, '71', gensym157)):
        if (knots == None):
            self.knots = mgd_cast_type_dyn(mgd_check_type_list(GetKnots(mgd_cast_type_list(points, gensym166, '75', gensym167), mgd_cast_type_int(degree, gensym168, '75', gensym169)), GetKnots, 2), gensym170, '75', gensym171)
        else:
            if (mgd_cast_type_function(len, gensym172, '77', gensym173)(points) > ((mgd_cast_type_function(len, gensym174, '77', gensym175)(knots) - degree) + 1)):
                raise mgd_cast_type_function(ValueError, gensym176, '78', gensym177)('too many control points')
            elif (mgd_cast_type_function(len, gensym178, '79', gensym179)(points) < ((mgd_cast_type_function(len, gensym180, '79', gensym181)(knots) - degree) + 1)):
                raise mgd_cast_type_function(ValueError, gensym182, '80', gensym183)('not enough control points')
            last = knots[0]
            gensym186 = knots[1:]
            for cur in gensym186:
                if (cur < last):
                    raise mgd_cast_type_function(ValueError, gensym184, '84', gensym185)('knots not strictly increasing')
                last = cur
            self.knots = knots
        self.points = points
        self.degree = degree

    def GetDomain(self):
        check7(self, self.GetDomain, (1, 0))
        return (mgd_check_type_int(mgd_check_type_list(self.knots, self, (0, 'knots'))[(mgd_check_type_int(self.degree, self, (0, 'degree')) - 1)], mgd_check_type_list(self.knots, self, (0, 'knots')), 3), mgd_check_type_int(mgd_check_type_list(self.knots, self, (0, 'knots'))[mgd_cast_type_int((mgd_cast_type_function(len, gensym189, '93', gensym190)(mgd_check_type_list(self.knots, self, (0, 'knots'))) - mgd_check_type_int(self.degree, self, (0, 'degree'))), gensym191, '93', gensym192)], mgd_check_type_list(self.knots, self, (0, 'knots')), 3))

    def __call__(self, u):
        check7(self, self.__call__, (1, 0))
        mgd_check_type_float(u, self.__call__, (1, 1))
        dom = mgd_check_type_tuple(mgd_check_type_function(self.GetDomain, self, (0, 'GetDomain'))(), mgd_check_type_function(self.GetDomain, self, (0, 'GetDomain')), 2, 2)
        if ((u < dom[0]) or (u > dom[1])):
            raise mgd_cast_type_function(ValueError, gensym231, '99', gensym232)('Function value not in domain')
        if (u == dom[0]):
            return mgd_cast_type_dyn(check1(mgd_check_type_list(self.points, self, (0, 'points'))[0], mgd_check_type_list(self.points, self, (0, 'points')), 3), gensym233, '101', gensym234)
        if (u == dom[1]):
            return mgd_cast_type_dyn(check1(mgd_check_type_list(self.points, self, (0, 'points'))[(- 1)], mgd_check_type_list(self.points, self, (0, 'points')), 3), gensym235, '103', gensym236)
        I = mgd_check_type_int(mgd_check_type_function(self.GetIndex, self, (0, 'GetIndex'))(u), mgd_check_type_function(self.GetIndex, self, (0, 'GetIndex')), 2)
        d = mgd_cast_type_list([check1(mgd_check_type_list(self.points, self, (0, 'points'))[mgd_cast_type_int((((I - mgd_check_type_int(self.degree, self, (0, 'degree'))) + 1) + ii), gensym239, '105', gensym240)], mgd_check_type_list(self.points, self, (0, 'points')), 3) for ii in mgd_cast_type_function(range, gensym237, '106', gensym238)((mgd_check_type_int(self.degree, self, (0, 'degree')) + 1))], gensym241, '105', gensym242)
        U = mgd_check_type_list(self.knots, self, (0, 'knots'))
        gensym264 = mgd_cast_type_function(range, gensym243, '108', gensym244)(1, (mgd_check_type_int(self.degree, self, (0, 'degree')) + 1))
        for ik in gensym264:
            gensym263 = mgd_cast_type_function(range, gensym245, '109', gensym246)((((I - mgd_check_type_int(self.degree, self, (0, 'degree'))) + ik) + 1), (I + 2))
            for ii in gensym263:
                ua = mgd_cast_type_dyn(mgd_check_type_int(U[mgd_cast_type_int(((ii + mgd_check_type_int(self.degree, self, (0, 'degree'))) - ik), gensym247, '110', gensym248)], U, 3), gensym249, '110', gensym250)
                ub = mgd_cast_type_dyn(mgd_check_type_int(U[mgd_cast_type_int((ii - 1), gensym251, '111', gensym252)], U, 3), gensym253, '111', gensym254)
                co1 = ((ua - u) / (ua - ub))
                co2 = ((u - ub) / (ua - ub))
                index = ((((ii - I) + mgd_check_type_int(self.degree, self, (0, 'degree'))) - ik) - 1)
                d[mgd_cast_type_int(index, gensym261, '115', gensym262)] = check1(mgd_check_type_function(check1(d[mgd_cast_type_int(index, gensym255, '115', gensym256)], d, 3).linear_combination, check1(d[mgd_cast_type_int(index, gensym255, '115', gensym256)], d, 3), (0, 'linear_combination'))(mgd_cast_type_dyn(check1(d[mgd_cast_type_int((index + 1), gensym257, '115', gensym258)], d, 3), gensym259, '115', gensym260), co1, co2), mgd_check_type_function(mgd_check_type_object(d[mgd_cast_type_int(index, gensym255, '115', gensym256)], d, 3, ['__rmul__', 'x', '__repr__', 'linear_combination', 'Mag', '__mul__', '__add__', '__str__', 'dist', 'y', '__sub__', 'z']).linear_combination, mgd_check_type_object(d[mgd_cast_type_int(index, gensym255, '115', gensym256)], d, 3, ['__rmul__', 'x', '__repr__', 'linear_combination', 'Mag', '__mul__', '__add__', '__str__', 'dist', 'y', '__sub__', 'z']), (0, 'linear_combination')), 2)
        return mgd_cast_type_dyn(check1(d[0], d, 3), gensym265, '116', gensym266)

    def GetIndex(self, u):
        check7(self, self.GetIndex, (1, 0))
        mgd_check_type_float(u, self.GetIndex, (1, 1))
        dom = mgd_check_type_tuple(mgd_check_type_function(self.GetDomain, self, (0, 'GetDomain'))(), mgd_check_type_function(self.GetDomain, self, (0, 'GetDomain')), 2, 2)
        gensym285 = mgd_cast_type_function(range, gensym279, '120', gensym280)((mgd_check_type_int(self.degree, self, (0, 'degree')) - 1), (mgd_cast_type_function(len, gensym277, '120', gensym278)(mgd_check_type_list(self.knots, self, (0, 'knots'))) - mgd_check_type_int(self.degree, self, (0, 'degree'))))
        for ii in gensym285:
            if ((u >= mgd_check_type_int(mgd_check_type_list(self.knots, self, (0, 'knots'))[mgd_cast_type_int(ii, gensym281, '121', gensym282)], mgd_check_type_list(self.knots, self, (0, 'knots')), 3)) and (u < mgd_check_type_int(mgd_check_type_list(self.knots, self, (0, 'knots'))[mgd_cast_type_int((ii + 1), gensym283, '121', gensym284)], mgd_check_type_list(self.knots, self, (0, 'knots')), 3))):
                I = ii
                break
        else:
            I = (dom[1] - 1)
        return mgd_cast_type_int(I, gensym286, '126', gensym287)

    def __len__(self):
        check7(self, self.__len__, (1, 0))
        return mgd_cast_type_int(mgd_cast_type_function(len, gensym290, '129', gensym291)(mgd_check_type_list(self.points, self, (0, 'points'))), gensym292, '129', gensym293)

    def __repr__(self):
        check7(self, self.__repr__, (1, 0))
        return mgd_cast_type_dyn(('Spline(%r, %r, %r)' % (mgd_check_type_list(self.points, self, (0, 'points')), mgd_check_type_int(self.degree, self, (0, 'degree')), mgd_check_type_list(self.knots, self, (0, 'knots')))), gensym296, '132', gensym297)
Spline = mgd_cast_type_class(Spline, gensym298, '68', gensym299, ['GetDomain', '__call__', '__len__', '__init__', 'GetIndex', '__repr__'])


class Chaosgame(retic_actual(object)):

    def __init__(self, splines, thickness=mgd_cast_type_dyn(0.1, gensym302, '138', gensym303)):
        self.splines = splines
        self.thickness = thickness
        self.minx = mgd_cast_type_function(min, gensym430, '141', gensym431)(mgd_cast_type_list([cast4(p, gensym426, '141', gensym427).x for spl in splines for p in cast8(spl, gensym424, '141', gensym425).points], gensym428, '141', gensym429))
        self.miny = mgd_cast_type_function(min, gensym438, '142', gensym439)(mgd_cast_type_list([cast5(p, gensym434, '142', gensym435).y for spl in splines for p in cast8(spl, gensym432, '142', gensym433).points], gensym436, '142', gensym437))
        self.maxx = mgd_cast_type_function(max, gensym446, '143', gensym447)(mgd_cast_type_list([cast4(p, gensym442, '143', gensym443).x for spl in splines for p in cast8(spl, gensym440, '143', gensym441).points], gensym444, '143', gensym445))
        self.maxy = mgd_cast_type_function(max, gensym454, '144', gensym455)(mgd_cast_type_list([cast5(p, gensym450, '144', gensym451).y for spl in splines for p in cast8(spl, gensym448, '144', gensym449).points], gensym452, '144', gensym453))
        self.height = (cast9(self, gensym456, '145', gensym457).maxy - cast10(self, gensym458, '145', gensym459).miny)
        self.width = (cast11(self, gensym460, '146', gensym461).maxx - cast12(self, gensym462, '146', gensym463).minx)
        self.num_trafos = mgd_cast_type_dyn([], gensym464, '147', gensym465)
        maxlength = ((thickness * cast13(self, gensym466, '148', gensym467).width) / cast14(self, gensym468, '148', gensym469).height)
        gensym493 = splines
        for spl in gensym493:
            length = mgd_cast_type_dyn(0, gensym470, '150', gensym471)
            curr = mgd_cast_type_function(spl, gensym472, '151', gensym473)(0)
            gensym482 = mgd_cast_type_function(range, gensym474, '152', gensym475)(1, 1000)
            for i in gensym482:
                last = curr
                t = ((1 / 999) * i)
                curr = mgd_cast_type_function(spl, gensym476, '155', gensym477)(t)
                length = (length + mgd_cast_type_function(cast15(curr, gensym478, '156', gensym479).dist, gensym480, '156', gensym481)(last))
            mgd_cast_type_function(cast17(cast16(self, gensym483, '157', gensym484).num_trafos, gensym485, '157', gensym486).append, gensym491, '157', gensym492)(mgd_cast_type_function(max, gensym489, '157', gensym490)(1, mgd_cast_type_function(int, gensym487, '157', gensym488)(((length / maxlength) * 1.5))))
        self.num_total = mgd_cast_type_function(reduce, gensym498, '158', gensym499)(cast18(operator, gensym494, '158', gensym495).add, cast16(self, gensym496, '158', gensym497).num_trafos, 0)

    def get_random_trafo(self):
        check19(self, self.get_random_trafo, (1, 0))
        r = mgd_cast_type_function(cast20(random, gensym526, '162', gensym527).randrange, gensym530, '162', gensym531)((mgd_cast_type_function(int, gensym528, '162', gensym529)(mgd_check_type_int(self.num_total, self, (0, 'num_total'))) + 1))
        l = mgd_cast_type_dyn(0, gensym532, '163', gensym533)
        gensym550 = mgd_cast_type_function(range, gensym536, '164', gensym537)(mgd_cast_type_function(len, gensym534, '164', gensym535)(mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos'))))
        for i in gensym550:
            if ((r >= l) and (r < (l + mgd_check_type_int(mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos'))[mgd_cast_type_int(i, gensym538, '165', gensym539)], mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos')), 3)))):
                return mgd_cast_type_tuple((i, mgd_cast_type_function(cast20(random, gensym540, '166', gensym541).randrange, gensym544, '166', gensym545)(mgd_check_type_int(mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos'))[mgd_cast_type_int(i, gensym542, '166', gensym543)], mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos')), 3))), gensym546, '166', gensym547, 2)
            l = (l + mgd_check_type_int(mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos'))[mgd_cast_type_int(i, gensym548, '167', gensym549)], mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos')), 3))
        return mgd_cast_type_tuple(((mgd_cast_type_function(len, gensym551, '168', gensym552)(mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos'))) - 1), mgd_cast_type_function(cast20(random, gensym553, '168', gensym554).randrange, gensym555, '168', gensym556)(mgd_check_type_int(mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos'))[(- 1)], mgd_check_type_list(self.num_trafos, self, (0, 'num_trafos')), 3))), gensym557, '168', gensym558, 2)

    def transform_point(self, point, trafo=mgd_cast_type_dyn(None, gensym561, '170', gensym562)):
        x = ((cast4(point, gensym675, '171', gensym676).x - cast12(self, gensym677, '171', gensym678).minx) / cast13(self, gensym679, '171', gensym680).width)
        y = ((cast5(point, gensym681, '172', gensym682).y - cast10(self, gensym683, '172', gensym684).miny) / cast14(self, gensym685, '172', gensym686).height)
        if (trafo is None):
            trafo = mgd_cast_type_function(cast21(self, gensym687, '174', gensym688).get_random_trafo, gensym689, '174', gensym690)()
        (start, end) = mgd_cast_type_tuple(mgd_cast_type_function(cast23(cast22(self, gensym691, '175', gensym692).splines[trafo[0]], gensym693, '175', gensym694).GetDomain, gensym695, '175', gensym696)(), gensym697, '175', gensym698, 2)
        length = (end - start)
        seg_length = (length / cast16(self, gensym699, '177', gensym700).num_trafos[trafo[0]])
        t = ((start + (seg_length * trafo[1])) + (seg_length * x))
        basepoint = mgd_cast_type_function(cast22(self, gensym701, '179', gensym702).splines[trafo[0]], gensym703, '179', gensym704)(t)
        if ((t + (1 / 50000)) > end):
            neighbour = mgd_cast_type_function(cast22(self, gensym705, '181', gensym706).splines[trafo[0]], gensym707, '181', gensym708)((t - (1 / 50000)))
            derivative = (neighbour - basepoint)
        else:
            neighbour = mgd_cast_type_function(cast22(self, gensym709, '184', gensym710).splines[trafo[0]], gensym711, '184', gensym712)((t + (1 / 50000)))
            derivative = (basepoint - neighbour)
        if (mgd_cast_type_function(cast24(derivative, gensym713, '186', gensym714).Mag, gensym715, '186', gensym716)() != 0):
            basepoint.x = (cast4(basepoint, gensym717, '187', gensym718).x + (((cast5(derivative, gensym719, '187', gensym720).y / mgd_cast_type_function(cast24(derivative, gensym721, '187', gensym722).Mag, gensym723, '187', gensym724)()) * (y - 0.5)) * cast25(self, gensym725, '188', gensym726).thickness))
            basepoint.y = (cast5(basepoint, gensym727, '189', gensym728).y + ((((- cast4(derivative, gensym729, '189', gensym730).x) / mgd_cast_type_function(cast24(derivative, gensym731, '189', gensym732).Mag, gensym733, '189', gensym734)()) * (y - 0.5)) * cast25(self, gensym735, '190', gensym736).thickness))
        else:
            print_(mgd_cast_type_dyn('r', gensym737, '192', gensym738), end='')
        mgd_cast_type_function(cast26(self, gensym739, '193', gensym740).truncate, gensym741, '193', gensym742)(basepoint)
        return cast3(basepoint, gensym743, '194', gensym744)

    def truncate(self, point):
        check19(self, self.truncate, (1, 0))
        check1(point, self.truncate, (1, 1))
        if (mgd_check_type_float(point.x, point, (0, 'x')) >= mgd_check_type_float(self.maxx, self, (0, 'maxx'))):
            point.x = mgd_check_type_float(self.maxx, self, (0, 'maxx'))
        if (mgd_check_type_float(point.y, point, (0, 'y')) >= mgd_check_type_float(self.maxy, self, (0, 'maxy'))):
            point.y = mgd_check_type_float(self.maxy, self, (0, 'maxy'))
        if (mgd_check_type_float(point.x, point, (0, 'x')) < mgd_check_type_float(self.minx, self, (0, 'minx'))):
            point.x = mgd_check_type_float(self.minx, self, (0, 'minx'))
        if (mgd_check_type_float(point.y, point, (0, 'y')) < mgd_check_type_float(self.miny, self, (0, 'miny'))):
            point.y = mgd_check_type_float(self.miny, self, (0, 'miny'))

    def create_image_chaos(self, timer, w, h, n):
        check19(self, self.create_image_chaos, (1, 0))
        mgd_check_type_int(w, self.create_image_chaos, (1, 2))
        mgd_check_type_int(h, self.create_image_chaos, (1, 3))
        mgd_check_type_int(n, self.create_image_chaos, (1, 4))
        im = mgd_cast_type_list([([1] * h) for i in mgd_cast_type_function(range, gensym803, '207', gensym804)(w)], gensym805, '207', gensym806)
        point = check1(GVector(mgd_cast_type_dyn(((mgd_check_type_float(self.maxx, self, (0, 'maxx')) + mgd_check_type_float(self.minx, self, (0, 'minx'))) / 2), gensym807, '208', gensym808), mgd_cast_type_dyn(((mgd_check_type_float(self.maxy, self, (0, 'maxy')) + mgd_check_type_float(self.miny, self, (0, 'miny'))) / 2), gensym809, '209', gensym810), mgd_cast_type_dyn(0, gensym811, '209', gensym812)), GVector, 2)
        colored = 0
        times = []
        gensym836 = mgd_cast_type_function(range, gensym813, '212', gensym814)(n)
        for _ in gensym836:
            t1 = mgd_cast_type_function(timer, gensym815, '213', gensym816)()
            gensym833 = mgd_cast_type_function(xrange, gensym817, '214', gensym818)(5000)
            for i in gensym833:
                point = check1(mgd_check_type_function(self.transform_point, self, (0, 'transform_point'))(mgd_cast_type_dyn(point, gensym819, '215', gensym820)), mgd_check_type_function(self.transform_point, self, (0, 'transform_point')), 2)
                x = mgd_cast_type_dyn((((mgd_check_type_float(point.x, point, (0, 'x')) - mgd_check_type_float(self.minx, self, (0, 'minx'))) / mgd_check_type_float(self.width, self, (0, 'width'))) * w), gensym821, '216', gensym822)
                y = mgd_cast_type_dyn((((mgd_check_type_float(point.y, point, (0, 'y')) - mgd_check_type_float(self.miny, self, (0, 'miny'))) / mgd_check_type_float(self.height, self, (0, 'height'))) * h), gensym823, '217', gensym824)
                x = mgd_cast_type_function(int, gensym825, '218', gensym826)(x)
                y = mgd_cast_type_function(int, gensym827, '219', gensym828)(y)
                if (x == w):
                    x = (x - 1)
                if (y == h):
                    y = (y - 1)
                mgd_check_type_list(im[mgd_cast_type_int(x, gensym829, '224', gensym830)], im, 3)[mgd_cast_type_int(((h - y) - 1), gensym831, '224', gensym832)] = 0
            t2 = mgd_cast_type_function(timer, gensym834, '225', gensym835)()
            mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t2 - t1)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
        return times
Chaosgame = mgd_cast_type_class(Chaosgame, gensym837, '134', gensym838, ['transform_point', 'truncate', 'create_image_chaos', '__init__', 'get_random_trafo'])

def main(n, timer):
    splines = [check7(Spline(mgd_cast_type_dyn([check1(GVector(mgd_cast_type_dyn(1.59735, gensym1063, '233', gensym1064), mgd_cast_type_dyn(3.30446, gensym1065, '233', gensym1066), mgd_cast_type_dyn(0.0, gensym1067, '233', gensym1068)), GVector, 2), check1(GVector(mgd_cast_type_dyn(1.57581, gensym1069, '234', gensym1070), mgd_cast_type_dyn(4.12326, gensym1071, '234', gensym1072), mgd_cast_type_dyn(0.0, gensym1073, '234', gensym1074)), GVector, 2), check1(GVector(mgd_cast_type_dyn(1.31321, gensym1075, '235', gensym1076), mgd_cast_type_dyn(5.28835, gensym1077, '235', gensym1078), mgd_cast_type_dyn(0.0, gensym1079, '235', gensym1080)), GVector, 2), check1(GVector(mgd_cast_type_dyn(1.6189, gensym1081, '236', gensym1082), mgd_cast_type_dyn(5.32991, gensym1083, '236', gensym1084), mgd_cast_type_dyn(0.0, gensym1085, '236', gensym1086)), GVector, 2), check1(GVector(mgd_cast_type_dyn(2.88994, gensym1087, '237', gensym1088), mgd_cast_type_dyn(5.5027, gensym1089, '237', gensym1090), mgd_cast_type_dyn(0.0, gensym1091, '237', gensym1092)), GVector, 2), check1(GVector(mgd_cast_type_dyn(2.37306, gensym1093, '238', gensym1094), mgd_cast_type_dyn(4.38183, gensym1095, '238', gensym1096), mgd_cast_type_dyn(0.0, gensym1097, '238', gensym1098)), GVector, 2), check1(GVector(mgd_cast_type_dyn(1.662, gensym1099, '239', gensym1100), mgd_cast_type_dyn(4.36028, gensym1101, '239', gensym1102), mgd_cast_type_dyn(0.0, gensym1103, '239', gensym1104)), GVector, 2)], gensym1105, '232', gensym1106), mgd_cast_type_dyn(3, gensym1107, '240', gensym1108), mgd_cast_type_dyn([0, 0, 0, 1, 1, 1, 2, 2, 2], gensym1109, '240', gensym1110)), Spline, 2), check7(Spline(mgd_cast_type_dyn([check1(GVector(mgd_cast_type_dyn(2.8045, gensym1111, '242', gensym1112), mgd_cast_type_dyn(4.01735, gensym1113, '242', gensym1114), mgd_cast_type_dyn(0.0, gensym1115, '242', gensym1116)), GVector, 2), check1(GVector(mgd_cast_type_dyn(2.5505, gensym1117, '243', gensym1118), mgd_cast_type_dyn(3.52523, gensym1119, '243', gensym1120), mgd_cast_type_dyn(0.0, gensym1121, '243', gensym1122)), GVector, 2), check1(GVector(mgd_cast_type_dyn(1.97901, gensym1123, '244', gensym1124), mgd_cast_type_dyn(2.62036, gensym1125, '244', gensym1126), mgd_cast_type_dyn(0.0, gensym1127, '244', gensym1128)), GVector, 2), check1(GVector(mgd_cast_type_dyn(1.97901, gensym1129, '245', gensym1130), mgd_cast_type_dyn(2.62036, gensym1131, '245', gensym1132), mgd_cast_type_dyn(0.0, gensym1133, '245', gensym1134)), GVector, 2)], gensym1135, '241', gensym1136), mgd_cast_type_dyn(3, gensym1137, '246', gensym1138), mgd_cast_type_dyn([0, 0, 0, 1, 1, 1], gensym1139, '246', gensym1140)), Spline, 2), check7(Spline(mgd_cast_type_dyn([check1(GVector(mgd_cast_type_dyn(2.00167, gensym1141, '248', gensym1142), mgd_cast_type_dyn(4.01132, gensym1143, '248', gensym1144), mgd_cast_type_dyn(0.0, gensym1145, '248', gensym1146)), GVector, 2), check1(GVector(mgd_cast_type_dyn(2.33504, gensym1147, '249', gensym1148), mgd_cast_type_dyn(3.31283, gensym1149, '249', gensym1150), mgd_cast_type_dyn(0.0, gensym1151, '249', gensym1152)), GVector, 2), check1(GVector(mgd_cast_type_dyn(2.3668, gensym1153, '250', gensym1154), mgd_cast_type_dyn(3.23346, gensym1155, '250', gensym1156), mgd_cast_type_dyn(0.0, gensym1157, '250', gensym1158)), GVector, 2), check1(GVector(mgd_cast_type_dyn(2.3668, gensym1159, '251', gensym1160), mgd_cast_type_dyn(3.23346, gensym1161, '251', gensym1162), mgd_cast_type_dyn(0.0, gensym1163, '251', gensym1164)), GVector, 2)], gensym1165, '247', gensym1166), mgd_cast_type_dyn(3, gensym1167, '252', gensym1168), mgd_cast_type_dyn([0, 0, 0, 1, 1, 1], gensym1169, '252', gensym1170)), Spline, 2)]
    c = check19(Chaosgame(mgd_cast_type_dyn(splines, gensym1171, '254', gensym1172), mgd_cast_type_dyn(0.25, gensym1173, '254', gensym1174)), Chaosgame, 2)
    return mgd_cast_type_dyn(mgd_check_type_list(mgd_check_type_function(c.create_image_chaos, c, (0, 'create_image_chaos'))(timer, 1000, 1200, mgd_cast_type_int(n, gensym1175, '255', gensym1176)), mgd_check_type_function(c.create_image_chaos, c, (0, 'create_image_chaos')), 2), gensym1177, '255', gensym1178)
if (__name__ == '__main__'):
    import util
    parser = mgd_cast_type_function(cast27(optparse, gensym1179, '261', gensym1180).OptionParser, gensym1181, '261', gensym1182)(usage='%prog [options]', description='Test the performance of the Chaos benchmark')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast28(parser, gensym1183, '265', gensym1184).parse_args, gensym1185, '265', gensym1186)(), gensym1187, '265', gensym1188, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast29(options, gensym1189, '267', gensym1190).num_runs, mgd_cast_type_dyn(main, gensym1191, '267', gensym1192))
