import copy
import DirPaths

from BSLDef import BSLDef
from BSLError import BSLError
from Structure import Structure


class ConstructorDef(BSLDef):

    def __init__(self, name, params):
        BSLDef.__init__(self, name, params)

    def apply(self, defs, vals):
        """
        Returns a Structure consisting of the name of the constructor and an
        association list associating structure parameters (fields) w/ values
        :param: make_instance: extend the new scope with the new definitions
        :return: New Scope with parameter defintions
        """

        return Structure(self.name, self.make_tuples(self.params, vals))

    def update(ast,s):
        return s.extend('make-%s' % ast.name, ast)

    def make_tuples(self, params, vals):
        """
        returns a list of tupes of params and vals
        :param params: [String]
        :param vals: [Value]
        :return: [(string, value)]
        :raises: BSLError if len(params) not equal len(vals)
        """
        if len(params) != len(vals):
            raise BSLError("params and vals must be equal")
        new_vals = copy.copy(vals)
        new_params = copy.copy(params)

        result = []
        while len(new_params) != 0:
            name = new_params.pop()
            val = new_vals.pop()
            result.insert(0, (name, val))

        return result