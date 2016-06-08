import DirPaths
from BSLExpr import BSLExpr
from BSLError import BSLError

class If(BSLExpr):
    """
    To represent an if-statement
    """

    def __init__(self, sl):
        """
        :param sl: BSLlist
        """
        self.test = sl[0]
        self.if_branch = sl[1]
        self.else_branch = sl[2]

    def eval_internal(self, defs):

        self.validate()

        if self.test.eval_internal(defs).boolean:
            return self.if_branch.eval_internal(defs)
        else:
            return self.else_branch.eval_internal(defs)

    def validate(self):
        if not isinstance(self.test, BSLExpr):
            raise BSLError('test must be a BSL expression')
        elif not isinstance(self.if_branch, BSLExpr):
            raise BSLError('if_branch must be a BSL expression')
        elif not isinstance(self.else_branch, BSLExpr):
            raise BSLError('else_branch must be a BSL expression')

    def __eq__(self, other):
        if not isinstance(other, If):
            return False
        else:
            return self.test == other.test and \
                   self.if_branch == other.if_branch\
                   and self.else_branch == other.else_branch