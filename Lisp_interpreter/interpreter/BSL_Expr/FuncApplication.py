from BSLExpr import BSLExpr

class FuncApplication(BSLExpr):
    """
    To represent function applications
    """

    def __init__(self, name, sl):
        """
        :param name: Name of the function
        :param sl: [BSLExpr]
        """
        self.name = name
        self.sl = sl

    def eval_internal(self, defs):
        vals = [x.eval_internal(defs) for x in self.sl]
        fun = self.name.eval_internal(defs)
        # if fun is not a primitive function or a Closure, ERROR!
        return fun.apply(defs, vals)

    def __eq__(self, other):
        if not isinstance(other, FuncApplication):
            return False

        else:
            return self.name == other.name and self.sl.__eq__(other.sl)
