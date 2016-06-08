import DirPaths
from BSLDef import BSLDef
from Structure import Structure
from BSLError import BSLError
from Boolean import Boolean

class PredicateDef(BSLDef):
    """
    Represents a structure predicate definition
    """

    def __init__(self, name, params):
        BSLDef.__init__(self, name, params)

    def update(ast,s):
        return s.extend('%s?' % ast.name, ast)

    def apply(self, defs, vals):
        result = Boolean(True)
        if not len(vals) == 1:
            raise BSLError('Wrong number of arguments')
        elif not isinstance(vals[0], Structure):
            result = Boolean(False)

        return result

