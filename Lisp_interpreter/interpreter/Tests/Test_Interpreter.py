import pytest
import sys

sys.path.insert(0, '/Users/zeinamigeed/Lisp_interpreter/interpreter/BSL_Expr')
sys.path.insert(0, '/Users/zeinamigeed/Lisp_interpreter/interpreter/Other')

from Variable import Variable
from BSLError import BSLError
from Num import Num
from Boolean import Boolean
from Constants import Constants as c


def test_eval_num():
    assert Num(1).eval_internal(c.defs1) == Num(1)
    assert Num(9).eval_internal(c.defs1) == Num(9)


def test_eval_add():
    assert c.expradd1.eval_internal(c.defs1) == Num(1)
    assert c.expradd123.eval_internal(c.defs1) == Num(6)
    assert c.expradd123.eval(c.defs1) == [Num(6), c.defs1]

    with pytest.raises(BSLError):
        c.expradderror.eval_internal(c.defs1)

def test_eval_sub():
    assert c.exprsub1.eval_internal(c.defs1) == Num(-1)
    assert c.exprsub123.eval_internal(c.defs1) == Num(-4)

def test_eval_mult():
    assert c.exprmul1.eval_internal(c.defs1) == Num(1)
    assert c.exprmul84.eval_internal(c.defs1) == Num(32)

def test_eval_div():
    assert c.exprdiv1.eval_internal(c.defs1) == Num(1)
    assert c.exprdiv84.eval_internal(c.defs1) == Num(2)

def test_eval_comp():
    assert c.expradd_expradd123_exprdiv84.eval_internal(c.defs1) == Num(8)

def test_eval_var():
    assert c.expraddx23.eval_internal(c.defs1) == Num(6)

def test_equals():
    assert c.expradd1 != c.expradd123
    assert c.expradd1 == c.expradd1
    assert c.func_def_varx != c.funcDef2
    assert c.func_def_varx == c.func_def_varx
    assert c.func_def_varx == c.func_def_varx
    assert c.and3 == c.and3
    assert c.and3 != c.and2

def test_funcAppEval():
    assert c.func_app_varx.eval_internal(c.defs1) == Num(4)
    assert c.func_app_emptylist.eval_internal(c.defs1) == Num(6)
    assert c.func_app_varx_vary.eval_internal(c.defs1) == Num(14)

def test_bslError():
    with pytest.raises(BSLError):
        Variable('o').eval_internal(c.defs1)

    with pytest.raises(BSLError):
        c.func_app_error_777.eval_internal(c.defs1)

    # with pytest.raises(BSLError):
    #     c.exprdiv403.eval_internal(c.defs1)

def test_struct():
    assert c.make_posn.eval_internal(c.defs1) == c.value_posn
    assert c.make_posn_comp.eval_internal(c.defs1) == (c.value_posn_comp)
    assert c.is_posn.eval_internal(c.defs1)
    assert c.is_not_posn.eval_internal(c.defs1) == Boolean(False)
    assert c.select_posn_x.eval_internal(c.defs1) == Num(1)
    assert c.select_posn_y.eval_internal(c.defs1) == Num(2)
    assert c.select_posn_y_comp.eval_internal(c.defs1) == Num(2)
    assert c.select_posn_x_comp.eval_internal(c.defs1) == c.value_posn
    assert c.func_app_varx_1.eval_internal(c.defs1) == c.value_posn_func
    assert c.posn_x_func_app_varx_1.eval_internal(c.defs1) == Num(4)


def test_struct_error():
    with pytest.raises(BSLError):
        c.select_posn_x_error.eval_internal(c.defs1)

    with pytest.raises(BSLError):
        c.select_zeina_x.eval_internal(c.defs1)


def test_and():
    assert c.and1.eval_internal(c.defs1) == Boolean(True)
   # assert c.and2.eval_internal(c.defs1) == Boolean(False)
    with pytest.raises(BSLError):
        c.and3.eval_internal(c.defs1)

def test_equal():
    assert c.equals34.eval_internal(c.defs1) == Boolean(False)
    assert c.equals33.eval_internal(c.defs1) == Boolean(True)
    assert c.equals_3_true.eval_internal(c.defs1) == Boolean(False)

def test_str():
    assert str(c.value_posn) == "(posn, 1,2)"
    assert str(c.varx) == 'Variable(x)'
    assert str(Num(3)) == '3'
    assert str(c.posn_def) == "StructureDefinition(posn, ('y', 'x'))"

def test_if():
    assert c.if_1.eval_internal(c.defs1) == Num(4)
    assert c.if_2.eval_internal(c.defs1) == Num(3)

def test_bigger_and_less_than(): #this test occassionally fails
    assert c.biggerthan34.eval_internal(c.defs1) == Boolean(False)
    assert c.lessthan34.eval_internal(c.defs1) == Boolean(True)

    with pytest.raises(BSLError):
        c.lessthan_error.eval_internal(c.defs1)



#error message that comes with the test:

# >       assert c.lessthan34.eval_internal(c.defs1) == Boolean(True)
# E       assert <Boolean.Boolean instance at 0x10ef732d8> == <Boolean.Boolean instance at 0x10ef73560>
# E        +  where <Boolean.Boolean instance at 0x10ef732d8> = <bound method FuncApplication.eval_internal of <FuncApplication.FuncApplication instance at 0x10ef75638>>(<Scope.Scope instance at 0x10ef67cb0>)
# E        +    where <bound method FuncApplication.eval_internal of <FuncApplication.FuncApplication instance at 0x10ef75638>> = <FuncApplication.FuncApplication instance at 0x10ef75638>.eval_internal
# E        +      where <FuncApplication.FuncApplication instance at 0x10ef75638> = c.lessthan34
# E        +    and   <Scope.Scope instance at 0x10ef67cb0> = c.defs1
# E        +  and   <Boolean.Boolean instance at 0x10ef73560> = Boolean(True)