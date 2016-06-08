import sys

sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Def')
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/BSL_Expr')
sys.path.insert(0, '/Users/zeina/Lisp_interpreter/interpreter/Other')

from Num import Num
from Variable import Variable
from FuncDef import FuncDef
from FuncApplication import FuncApplication
from If import If
from Scope import Scope
from Structure import Structure
from StructDef import StructDef
from And import And
from Boolean import Boolean
from LambdaExpr import LambdaExpr


class Constants:

    varx = Variable('x')
    vary = Variable('y')
    varz = Variable('z')
    varo = Variable('o')

    emptyList = []
    list123 = [Num(1), Num(2), Num(3)]
    listadd123 = [FuncApplication(Variable('+'), list123), Num(-3)]
    list12True = [Num(1), Num(2), Boolean(True)]

    listaddsubtract123 = [FuncApplication(Variable('-'),list123), FuncApplication('+', list123)]
    listmultiply123 = [FuncApplication(Variable('*'), list123)]
    list84 = [Num(8), Num(4)]
    listdivide84 = [FuncApplication(Variable('/'), list84)]
    listx23 = [varx, Num(2), Num(3)]
    listy3 = [vary, Num(3)]
    list43 = [Num(4), Num(3)]
    list403 = [Num(4), Num(0), Num(3)]

    expradd1 = FuncApplication(Variable('+'), [Num(1)])
    expradd123 = FuncApplication(Variable('+'), list123)
    expradd43 = FuncApplication(Variable('+'), list43)
    expradderror = FuncApplication(Variable('+'), list12True)

    exprsub1 = FuncApplication(Variable('-'), [Num(1)])
    exprsub123 = FuncApplication(Variable('-'), list123)
    exprsub_add123_add123 = FuncApplication(Variable('-'), [expradd123, expradd43])

    exprdiv1 = FuncApplication(Variable('/'), [Num(1)])
    exprdiv84 = FuncApplication(Variable('/'), list84)
    exprdiv403 = FuncApplication(Variable('/'), list403)

    exprmul1 = FuncApplication(Variable('*'), [Num(1)])
    exprmul84 = FuncApplication(Variable('*'), list84)

    expradd_expradd123_exprdiv84 = FuncApplication(Variable('+'),
                                                   [expradd123, exprdiv84])

    expraddx23 = FuncApplication(Variable('+'), listx23)
    expraddy3 = FuncApplication(Variable('+'), listy3)
    expsub_expraddx23_expradd3 = FuncApplication(Variable('-'), [expraddx23,
                                                                 expraddy3])

    #functions
    func_def_varx = FuncDef("f", LambdaExpr(["x"], Variable("x")))
    func_app_varx = FuncApplication(Variable('f'), [Num(4)])

    list_func_app_varx = [func_app_varx, Num(2)]
    expradd_func_app_varx = FuncApplication(Variable('+'), list_func_app_varx)

    funcDef2 = FuncDef('g',LambdaExpr([], expradd_func_app_varx))
    func_app_emptylist = FuncApplication(Variable('g'), []) ###############

    expradd_varx_vary = FuncApplication(Variable('+'), [varx, vary])

    func_def_add_varx_vary = FuncDef('z', LambdaExpr(['x', 'y'], expradd_varx_vary))
    func_app_varx_vary = FuncApplication(Variable('z'), [Num(7), Num(7)])
    func_app_error_777 = FuncApplication(Variable('z'), [Num(7), Num(7), Num(7)])

    func_app_100 = FuncApplication(Variable('d'), [Num(100)])

    defs1 = Scope(()).add_definitions()
    defs1 = defs1.extend('x', Num(1)).extend('y', Num(4))

    #set the scope by mutating to second arg of the tuple
    defs1 = func_def_varx.eval(defs1)[1]
    defs1 = funcDef2.eval(defs1)[1]
    defs1 = func_def_add_varx_vary.eval(defs1)[1]

    #structs
    posn_def = StructDef('posn', ['x', 'y'])
    defs1 = posn_def.update(defs1)

    zeina_def = StructDef('zeina', ['x', 'y'])
    defs1 = zeina_def.update(defs1)

    make_zeina = FuncApplication(Variable('make-posn'), [Num(10), Num(20)])

    select_zeina_x = FuncApplication(Variable('zeina-x'), [make_zeina])

    make_posn = FuncApplication(Variable('make-posn'), [Num(1), Num(2)])
    make_posn_comp = FuncApplication(Variable('make-posn'), [make_posn,
                                                             Num(2)])

    is_posn = FuncApplication(Variable('posn?'), [make_posn])
    is_not_posn = FuncApplication(Variable('posn?'), [Num(3)])

    select_posn_x = FuncApplication(Variable('posn-x'), [make_posn])
    select_posn_y = FuncApplication(Variable('posn-y'), [make_posn])

    select_posn_x_comp = FuncApplication(Variable('posn-x'), [make_posn_comp])
    select_posn_y_comp = FuncApplication(Variable('posn-y'), [make_posn_comp])

    value_posn = Structure('posn', [('x', Num(1)), ('y', Num(2))])
    value_posn_comp = Structure('posn', [('x', value_posn), ('y', Num(2))])

    #functions using struct
    make_posn_func = FuncApplication(Variable('make-posn'), [func_app_varx, Num(1)])
    func_app_varx_1 = FuncApplication(Variable('f'), [make_posn_func])

    value_posn_func = Structure('posn', [('x', Num(4)), ('y', Num(1))])

    posn_x_func_app_varx_1 = FuncApplication(Variable('posn-x'), [func_app_varx_1])

    select_posn_x_error = FuncApplication(Variable('posn-x'), [Num(3)])

    ex1 = '(ex*'
    ex_abc = 'abc'
    ex_1 = '1'
    exx1 = ')'
    exx2 = ex_abc + exx1

    #And
    and1 = And([Boolean(True), Boolean(False)])
    and2 = And([Boolean(False), FuncApplication(Variable('/'), [Num(1), Num(0)])])
    and3 = And([Boolean(True), FuncApplication(Variable('/'), [Num(1), Num(1)])])

    #equals
    equals34 = FuncApplication(Variable('='), [Num(3), Num(4)])
    equals33 = FuncApplication(Variable('='), [Num(3), Num(3)])
    equals_3_true = FuncApplication(Variable('='), [Num(3), Boolean(False)])

    #bigger and less than
    biggerthan34 = FuncApplication(Variable('>'), [Num(3), Num(4)])
    lessthan34 = FuncApplication(Variable('<'), [Num(3), Num(4)])
    lessthan_error = FuncApplication(Variable('>'), [Variable('xyz'), Num(4)])

    #if.
    if_1 = If([equals34, Num(3), Num(4)])
    if_2 = If([equals33, Num(3), Num(4)])

