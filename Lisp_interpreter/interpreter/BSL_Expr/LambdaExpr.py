import DirPaths
from BSLExpr import BSLExpr
from Closure import Closure

class LambdaExpr(BSLExpr):
    """
    To represent a lambda expression.
    """

    def __init__(self, params, body):
        """
        :param params: [Strings]
        :param body: [BSLExpr]
        """
        self.params = params
        self.body = body

    def eval_internal(self, defs):
        """
        Evaluates this expression
        :param defs: Scope
        :return: Value of this expresson
        """
        return Closure(self, defs)

    def __eq__(self, other):
        if not isinstance(other, LambdaExpr):
            return False
        else:
            return (self.params == other.params) \
                   and (self.body == other.body)


