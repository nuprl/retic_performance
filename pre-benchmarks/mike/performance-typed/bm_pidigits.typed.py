from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check4(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.islice
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.count
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)
import optparse
import time
import itertools
import util
from compat import xrange, imap, next
NDIGITS = 2000

def test_pidgits(iterations, timer):
    check_type_int(iterations)
    _map = imap
    _count = check0(itertools).count
    _islice = check1(itertools).islice

    def calc_ndigits(n):
        check_type_int(n)

        def gen_x():
            return check_type_function(_map)((lambda k: (k, ((4 * k) + 2), 0, ((2 * k) + 1))), check_type_function(_count)(1))
        gen_x = check_type_function(gen_x)

        def compose(a, b):
            check_type_tuple(a, 4)
            check_type_tuple(b, 4)
            (aq, ar, as_, at) = a
            (bq, br, bs, bt) = b
            return ((aq * bq), ((aq * br) + (ar * bt)), ((as_ * bq) + (at * bs)), ((as_ * br) + (at * bt)))
        compose = check_type_function(compose)

        def extract(z, j):
            check_type_tuple(z, 4)
            check_type_int(j)
            (q, r, s, t) = z
            return (((q * j) + r) // ((s * j) + t))
        extract = check_type_function(extract)

        def pi_digits():
            z = (1, 0, 0, 1)
            x = gen_x()
            while 1:
                y = check_type_int(extract(z, 3))
                while (y != check_type_int(extract(z, 4))):
                    z = check_type_tuple(compose(z, check_type_tuple(next(x), 4)), 4)
                    y = check_type_int(extract(z, 3))
                z = check_type_tuple(compose((10, ((- 10) * y), 0, 1), z), 4)
                yield y
        pi_digits = check_type_function(pi_digits)
        return check_type_list(check_type_function(list)(check_type_function(_islice)(pi_digits(), n)))
    calc_ndigits = check_type_function(calc_ndigits)
    check_type_list(calc_ndigits(NDIGITS))
    check_type_list(calc_ndigits(NDIGITS))
    times = []
    for _ in check_type_function(xrange)(iterations):
        t0 = check_type_function(timer)()
        check_type_list(calc_ndigits(NDIGITS))
        t1 = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((t1 - t0)))
    return times
test_pidgits = check_type_function(test_pidgits)
if (__name__ == '__main__'):
    parser = check_type_function(check2(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of pi calculation.')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check3(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check4(options).num_runs, test_pidgits)
