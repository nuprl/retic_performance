from retic.runtime import *
from retic.guarded import *
from retic.typing import *
from benchmark_tools.Timer import Timer
import os, sys
this_package_path = retic_cast(retic_cast(retic_cast(os, Dyn, Object('', {'path': Dyn, }), '\nmain.py:4:20: Accessing nonexistant object attribute path from value %s. (code WIDTH_DOWNCAST)').path, Dyn, Object('', {'dirname': Dyn, }), '\nmain.py:4:20: Accessing nonexistant object attribute dirname from value %s. (code WIDTH_DOWNCAST)').dirname, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nmain.py:4:20: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(retic_cast(retic_cast(retic_cast(os, Dyn, Object('', {'path': Dyn, }), '\nmain.py:4:36: Accessing nonexistant object attribute path from value %s. (code WIDTH_DOWNCAST)').path, Dyn, Object('', {'abspath': Dyn, }), '\nmain.py:4:36: Accessing nonexistant object attribute abspath from value %s. (code WIDTH_DOWNCAST)').abspath, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nmain.py:4:36: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(__file__))
retic_cast(retic_cast(retic_cast(sys, Dyn, Object('', {'path': Dyn, }), '\nmain.py:5:0: Accessing nonexistant object attribute path from value %s. (code WIDTH_DOWNCAST)').path, Dyn, Object('', {'insert': Dyn, }), '\nmain.py:5:0: Accessing nonexistant object attribute insert from value %s. (code WIDTH_DOWNCAST)').insert, Dyn, Function(AnonymousParameters([Int, Dyn]), Dyn), "\nmain.py:5:0: Expected function of type Function(['Int', 'Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(0, retic_cast(retic_cast(retic_cast(os, Dyn, Object('', {'path': Dyn, }), '\nmain.py:5:19: Accessing nonexistant object attribute path from value %s. (code WIDTH_DOWNCAST)').path, Dyn, Object('', {'join': Dyn, }), '\nmain.py:5:19: Accessing nonexistant object attribute join from value %s. (code WIDTH_DOWNCAST)').join, Dyn, Function(AnonymousParameters([Dyn, String]), Dyn), "\nmain.py:5:19: Expected function of type Function(['Dyn', 'String'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(this_package_path, '..'))
data = retic_cast(list, Dyn, Function(AnonymousParameters([Dyn]), Dyn), "\nmain.py:6:8: Expected function of type Function(['Dyn'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(retic_cast(map, Dyn, Function(AnonymousParameters([Dyn, List(Dyn)]), Dyn), "\nmain.py:6:13: Expected function of type Function(['Dyn', 'List(Dyn)'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(int, [retic_cast(retic_cast(line, Dyn, Object('', {'strip': Dyn, }), '\nmain.py:6:23: Accessing nonexistant object attribute strip from value %s. (code WIDTH_DOWNCAST)').strip, Dyn, Function(AnonymousParameters([]), Dyn), '\nmain.py:6:23: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')() for line in retic_cast(open, Dyn, Function(AnonymousParameters([String]), Dyn), "\nmain.py:6:48: Expected function of type Function(['String'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")('numbers.txt')]))
rand_num = (element for element in data)

def main():
    total = retic_cast(0, Int, Dyn, '\nmain.py:11:2: Right hand side of assignment was expected to be of type Dyn, but value %s provided instead. (code SINGLE_ASSIGN_ERROR)')
    for n in rand_num:
        total = (total + n)
    return total
main = retic_cast(main, Dyn, Function(NamedParameters([]), Dyn), '\nmain.py:10:0: Function %s does not match specified type Function([], Dyn). Consider changing the type or setting it to Dyn. (code BAD_FUNCTION_INJECTION)')
t = retic_cast(Timer, Dyn, Function(AnonymousParameters([]), Dyn), '\nmain.py:16:4: Expected function of type Function([], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)')()
with t:
    for i in retic_cast(range, Dyn, Function(AnonymousParameters([Int]), Dyn), "\nmain.py:18:11: Expected function of type Function(['Int'], Dyn) at call site but but value %s was provided instead. (code FUNC_ERROR)")(100):
        main()