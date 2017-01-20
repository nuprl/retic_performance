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
        val.pop
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.insert
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.parse_args
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
import util
from compat import xrange

def fannkuch(n):
    check_type_int(n)
    count = check_type_function(list)(check_type_function(range)(1, (n + 1)))
    max_flips = 0
    m = (n - 1)
    r = n
    check = 0
    perm1 = check_type_function(list)(check_type_function(range)(n))
    perm = check_type_function(list)(check_type_function(range)(n))
    perm1_ins = check0(perm1).insert
    perm1_pop = check1(perm1).pop
    while 1:
        if (check < 30):
            check = (check + 1)
        while (r != 1):
            count[(r - 1)] = r
            r = (r - 1)
        if ((perm1[0] != 0) and (perm1[m] != m)):
            perm = perm1[:]
            flips_count = 0
            k = perm[0]
            while k:
                perm[:(k + 1)] = perm[k::(- 1)]
                flips_count = (flips_count + 1)
                k = perm[0]
            if (flips_count > max_flips):
                max_flips = flips_count
        while (r != n):
            check_type_function(perm1_ins)(r, check_type_function(perm1_pop)(0))
            count[r] = (count[r] - 1)
            if (count[r] > 0):
                break
            r = (r + 1)
        else:
            return check_type_int(max_flips)
    return (- 1)
fannkuch = check_type_function(fannkuch)
DEFAULT_ARG = 9

def main(n, timer):
    times = []
    for i in check_type_function(xrange)(n):
        t0 = check_type_function(timer)()
        check_type_int(fannkuch(DEFAULT_ARG))
        tk = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((tk - t0)))
    return times
main = check_type_function(main)
if (__name__ == '__main__'):
    parser = check_type_function(check2(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check3(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check4(options).num_runs, main)
