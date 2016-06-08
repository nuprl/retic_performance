import copy
import DirPaths
import operator
from functools import reduce
from BSLError import BSLError
from ComparisonDef import ComparisonDef
from Num import Num
from Boolean import Boolean
from BSLExpr import BSLExpr
from copy import copy

class Scope:
    """
    To represent the definitions as a tuple T, where t[0] is a key, t[1] is a value and t[2] is
    the old scope
    """

    def __init__(self, defs):
        """
        Initialises the scope from a tuple with three elements
        :param defs: Tuple containing three elements. If no definitions exist, we may use an empty tuple
        """
        self.defs = defs

    def __str__(self):
        return self.defs[0]

    def extend(self, name, val):
        """
        Expends this Scope with name and val
        :param name: String
        :param val: Value corresponding to name
        :return: New scope with extended definitions
        """
        if not isinstance(name, str) :
            raise BSLError('name field must be a string')
        return Scope((name, val, self))

    def get(self, key):
        if not self.defs:
            return None
        else:
            name = self.defs[0]
            val = self.defs[1]
            old_self = self.defs[2]
            if key == name:
                return val
            else:
                return old_self.get(key)

    def add_definitions(self):
        add = self.extend('+', ComparisonDef(lambda *args: reduce(operator.__add__, (arg.num for arg in args)), Num, Num))
        sub = add.extend('-', ComparisonDef(lambda *args: (-1 * args[0].num if len(args) == 1 else reduce(operator.__sub__, (arg.num for arg in args))), Num, Num))
        mul = sub.extend('*',ComparisonDef(lambda *args: reduce(operator.__mul__, (arg.num for arg in args)), Num, Num))
        div = mul.extend('/', ComparisonDef(lambda *args: reduce(operator.__floordiv__, (arg.num for arg in args)), Num, Num))
        exp = div.extend('^', ComparisonDef((lambda x, y: pow(x,y)), Num, Num))
        equals = exp.extend('=', ComparisonDef((lambda x, y: x == y), Boolean, BSLExpr))
        bigger_than = equals.extend('>', ComparisonDef((lambda x, y: x > y), Boolean, Num))
        smaller_than = bigger_than.extend('<', ComparisonDef((lambda x, y: x < y), Boolean, Num))
        return smaller_than


