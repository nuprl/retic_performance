import copy
import sys
import DirPaths
from LambdaExpr import LambdaExpr
from BSLError import BSLError
from Binding import Binding
from BSLDef import BSLDef


class FuncDef(Binding):

    """
    To represent function definitions
    """

    def __init__(self, name, expr):
        Binding.__init__(self, name, expr)

    def eval(ast,s):
        return [None, s.extend(ast.name, ast.expr.eval_internal(s))]

    def __eq__(self, other):

        if not isinstance(other, FuncDef):
            return False
        else:
            return other.name == self.name and other.expr == other.expr


