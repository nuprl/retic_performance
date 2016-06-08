import DirPaths

from BSLExpr import BSLExpr
from BSLError import BSLError

class Num(BSLExpr):
    """
    To represent an atomic, numerical sExpression
    """

    def __init__(self, num):
        """
        :param num: Number
        """
        self.num = self.validate(num)
        #self.num = num

    def eval_internal(self, defs):
        return self

    def validate(self, num):
        if not isinstance(num, (complex, int, float)):
            raise BSLError('field must be a number')
        else:
            return num

    def __eq__(self, other):
        if not isinstance(other, Num):
            return False
        else:
            return other.num == self.num

    def __str__(self):
        return str(self.num)
