from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check1(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.time
        return val
    except:
        raise CheckError(val)
import optparse
import time
import util
from compat import xrange

def foo(a, b, c, d):
    check_type_int(b)
    check_type_int(c)
    check_type_int(d)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
foo = check_type_function(foo)

def bar(a, b, c):
    check_type_int(b)
    check_type_int(c)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
bar = check_type_function(bar)

def baz(a, b):
    check_type_int(b)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
baz = check_type_function(baz)

def quux(a):
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
quux = check_type_function(quux)

def qux():
    pass
qux = check_type_function(qux)

def test_calls(iterations, timer):
    times = []
    for _ in check_type_function(xrange)(iterations):
        t0 = check_type_function(timer)()
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        t1 = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((t1 - t0)))
    return times
test_calls = check_type_function(test_calls)
if (__name__ == '__main__'):
    parser = check_type_function(check0(optparse).OptionParser)(usage='%prog [options] [test]', description='Test the performance of simple Python-to-Python function calls.')
    check_type_function(util.add_standard_options_to)(parser)
    (options, _) = check_type_tuple(check_type_function(check1(parser).parse_args)(), 2)
    test_calls(1, check2(time).time)
    check_type_function(util.run_benchmark)(options, check3(options).num_runs, test_calls)
