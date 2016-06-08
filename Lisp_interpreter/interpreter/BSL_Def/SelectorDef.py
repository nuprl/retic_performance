import DirPaths
from BSLDef import BSLDef
from BSLError import BSLError
from Structure import Structure

class SelectorDef(BSLDef):

    def __init__(self, name, params):
        """
        :param params:[string] representing only one param to be selected
        """
        BSLDef.__init__(self, name, params)

    def update(ast,s):
        return s.extend('%s-%s' % (ast.name, ast.params[0]), ast)

    def apply(self, defs, vals):

        if not isinstance(vals[0], Structure):
            raise BSLError('Can only select from a Structure')

        if vals[0].name != self.name:
            raise BSLError\
                ('Expects a %s, given a %s' % (self.name, vals[0].name))

        tuples = vals[0].tuples
        param = self.params[0]

        # assoc assq
        for tuple in tuples:
            if tuple[0] == param:
                return tuple[1]


