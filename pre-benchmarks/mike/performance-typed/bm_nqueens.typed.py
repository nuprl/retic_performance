from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check0(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)
__author__ = 'collinwinter@google.com (Collin Winter)'
import optparse
import re
import string
import time
import util
from compat import xrange

def permutations(iterable, r=None):
    pool = check_type_function(tuple)(iterable)
    n = check_type_function(len)(pool)
    if (r is None):
        r = n
    indices = check_type_function(list)(check_type_function(range)(n))
    cycles = check_type_function(list)(check_type_function(range)(((n - r) + 1), (n + 1)))[::(- 1)]
    yield check_type_function(tuple)((pool[i] for i in indices[:r]))
    while n:
        for i in check_type_function(reversed)(check_type_function(range)(r)):
            cycles[i] = (cycles[i] - 1)
            if (cycles[i] == 0):
                indices[i:] = (indices[(i + 1):] + indices[i:(i + 1)])
                cycles[i] = (n - i)
            else:
                j = cycles[i]
                (indices[i], indices[(- j)]) = (indices[(- j)], indices[i])
                yield check_type_function(tuple)((pool[i] for i in indices[:r]))
                break
        else:
            return
permutations = check_type_function(permutations)

def n_queens(queen_count):
    check_type_int(queen_count)
    cols = check_type_function(range)(queen_count)
    for vec in permutations(cols):
        if (queen_count == check_type_function(len)(check_type_function(set)(((vec[i] + i) for i in cols))) == check_type_function(len)(check_type_function(set)(((vec[i] - i) for i in cols)))):
            yield vec
n_queens = check_type_function(n_queens)

def test_n_queens(iterations, timer):
    check_type_function(list)(n_queens(8))
    check_type_function(list)(n_queens(8))
    times = []
    for _ in check_type_function(xrange)(iterations):
        t0 = check_type_function(timer)()
        check_type_function(list)(n_queens(8))
        t1 = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((t1 - t0)))
    return times
test_n_queens = check_type_function(test_n_queens)
if (__name__ == '__main__'):
    parser = check_type_function(check0(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of an N-Queens solvers.')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check1(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check2(options).num_runs, test_n_queens)
