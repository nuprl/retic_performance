class P_Expr:
    """
    Represents a union type p-expr
    """
    def __init__(self, expr):
        """
        :param p_expr: List of string or None
        :return: None
        """
        self.expr = expr


class Line:
    """
    To represent the read line or False if no line was read
    """
    def __init__(self, line):
        """
        :param line: [String, ...] or False
        """
        self.line = line