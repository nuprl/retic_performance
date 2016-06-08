import DirPaths
import operator
from BSLError import BSLError
from Num import Num
from Boolean import Boolean
from BSLExpr import BSLExpr

class ComparisonDef:
    """
    To represent comparison operation
    """
    def __init__(self, comp, cls, argcls):
        """
        :param comp: Function that takes two numbers (num, num -> ?)
         and returns the result of the comparison
        :param cls: class to wrap around the result
        :param argcls: the type that args need to be
        """
        self.comp = comp
        self.cls = cls
        self.argcls = argcls

    def apply(self, name, args):
        self.validate(args, self.argcls)

        return self.cls(self.comp(*args))

    def validate(self, args, type):
        """
        Ensure that list of args are of type type
        :param args: List of values
        :param type: type that args need to be
        :return: True if elements are of type type
        :raise: BSLError if an arg is of the wrong type
        """
        for arg in args:
            if not isinstance(arg, type):
                raise BSLError('Arguments are of incorrect type.')


