import DirPaths

class Binding:
    """
    To represent a binding between a name and a BSLExpr
    """

    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


