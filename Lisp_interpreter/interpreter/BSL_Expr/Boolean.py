from BSLExpr import BSLExpr

class Boolean(BSLExpr):
    """
    To represent BSL Booleans
    """

    def __init__(self, boolean):
        """
        :param boolean: True or False
        """
        self.boolean = boolean

    def eval_internal(self, defs):
        return self

    def __eq__(self, other):
        if not isinstance(other, Boolean):
            return False

        else:
            return self.boolean == other.boolean

    def __str__(self):
        if self.boolean:
            return 'true'
        else:
            return 'false'