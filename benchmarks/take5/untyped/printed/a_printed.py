from retic.runtime import *
from retic.transient import *
from retic.typing import *
from retic import Int

def f(x):
    check_type_int(x)
    return x
f = check_type_function(f)
f(1)
