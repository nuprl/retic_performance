import sys
sys.path.insert(0, '/Users/zeinamigeed/Lisp_interpreter/interpreter/Other')

from Scope import Scope

class Test_scope:

    def test_get(self):

        defs = Scope(()).extend('g', 2).extend('f', 1).extend('x', 2).extend('x', 3)
        defs2 = defs.extend('x', 3)
        defs3 = defs.extend('f', 3)

        assert defs2.get('x') == 3
        assert defs2.get('x') == 3
        assert defs3.get('f') == 3
        assert defs.get('x') == 3

        defs_a = Scope(())
        defs_b = defs_a.extend('x',0)
        assert(defs_b.get('x') == 0)
        assert(defs_b.get('x') == 0)









