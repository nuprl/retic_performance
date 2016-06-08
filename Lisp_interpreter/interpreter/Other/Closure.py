import DirPaths
import copy

from BSLError import BSLError

class Closure:
    """
    To represent the value of the function and the current scope
    """

    def __init__(self, lambda_expr, curr_scope):
        """
        :param lambda_expr:
        :param curr_scope:
        """
        self.lambda_expr = lambda_expr
        self.curr_scope = curr_scope

    def __str__(self):
        return '(lambda (a1 a2) ...)'

    def apply(self, ___defs, args):
        """
        Applies a function application to this function defintion
        :param defs: Scope
        :param sl: [BSLExpr]
        :return: Value
        """
        body = self.lambda_expr.body
        params = copy.copy(self.lambda_expr.params)
        defs = self.helper_extend(self.curr_scope, params, args)

        return body.eval_internal(defs)

    def helper_extend(self, defs, params, vals):
        """
        Extends defs with params and vals
        :param defs: Scope representing the definitions
        :param params: [String]
        :param vals: [number]
        :return: Scope
        :raises: BSLError if len(params) not equal len(vals)
        """

        if len(params) != len(vals):
            raise BSLError("params and vals must be equal")
        new_vals = copy.copy(vals)
        new_params = copy.copy(params)
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            defs = defs.extend(name, val)

        return defs

