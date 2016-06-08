from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check4(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.bar
        val.baz
        val.qux
        val.__slots__
        val.foo
        val.quux
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.time
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)
import optparse
import time
import util
from compat import xrange


class Foo(retic_actual(object)):
    __slots__ = ()

    def foo(self, a, b, c, d):
        check0(self)
        check_type_int(a)
        check_type_int(b)
        check_type_int(c)
        check_type_int(d)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
        check_type_function(self.bar)(a, b, c)
    foo = check_type_function(foo)

    def bar(self, a, b, c):
        check0(self)
        check_type_int(a)
        check_type_int(b)
        check_type_int(c)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
        check_type_function(self.baz)(a, b)
    bar = check_type_function(bar)

    def baz(self, a, b):
        check0(self)
        check_type_int(a)
        check_type_int(b)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
        check_type_function(self.quux)(a)
    baz = check_type_function(baz)

    def quux(self, a):
        check0(self)
        check_type_int(a)
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
        check_type_function(self.qux)()
    quux = check_type_function(quux)

    def qux(self):
        pass
    qux = check_type_function(qux)
Foo = check_type_class(Foo, ['bar', 'baz', 'qux', '__slots__', 'foo', 'quux'])

def test_calls(iterations, timer):
    check_type_int(iterations)
    times = []
    f = check0(Foo())
    if check_type_function(hasattr)(f, '__dict__'):
        raise check_type_function(Exception)('f has a __dict__ attribute!')
    for _ in check_type_function(xrange)(iterations):
        t0 = check_type_function(timer)()
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        check_type_function(f.foo)(1, 2, 3, 4)
        t1 = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((t1 - t0)))
    return times
test_calls = check_type_function(test_calls)
if (__name__ == '__main__'):
    parser = check_type_function(check1(optparse).OptionParser)(usage='%prog [options] [test]', description='Test the performance of method calls on objects that use __slots__.')
    check_type_function(util.add_standard_options_to)(parser)
    (options, _) = check_type_tuple(check_type_function(check2(parser).parse_args)(), 2)
    test_calls(1, check3(time).time)
    check_type_function(util.run_benchmark)(options, check4(options).num_runs, test_calls)
