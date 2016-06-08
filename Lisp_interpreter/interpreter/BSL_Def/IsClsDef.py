import DirPaths
from BSLError import BSLError

class IsClsDef:
    """
    Determines if some class is a Prim
    """

    def __init__(self, cls):
        """
        :param cls: Subclass name
        """
        self.cls = cls

    def apply(self, vals):
        """
        Is vals[0] a Boolean
        :param vals: List of Values
        :return: True if vals[0] == True or False, and returns False otherwise
        """
        if len(vals) != 1:
            raise BSLError('Length must = 1')

        if isinstance(vals[0], self.cls):
            return True
        else:
            return False






