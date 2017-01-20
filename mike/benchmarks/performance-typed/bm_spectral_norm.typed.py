from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check0(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)
from math import sqrt
import time
import itertools
import optparse
from compat import izip, xrange
import util

def eval_A(i, j):
    check_type_float(i)
    check_type_float(j)
    return (1.0 / (((((i + j) * ((i + j) + 1)) // 2) + i) + 1))
eval_A = check_type_function(eval_A)

def eval_times_u(func, u):
    check_type_function(func)
    check_type_list(u)
    return check_type_list([check_type_float(func(check_type_tuple((i, u), 2))) for i in check_type_function(xrange)(check_type_function(len)(check_type_function(list)(u)))])
eval_times_u = check_type_function(eval_times_u)

def eval_AtA_times_u(u):
    check_type_list(u)
    return check_type_list(eval_times_u(part_At_times_u, check_type_list(eval_times_u(part_A_times_u, u))))
eval_AtA_times_u = check_type_function(eval_AtA_times_u)

def part_A_times_u(i_u):
    check_type_tuple(i_u, 2)
    (i, u) = i_u
    partial_sum = 0
    for (j, u_j) in check_type_function(enumerate)(u):
        check_type_tuple((j, u_j), 2)
        partial_sum = (partial_sum + (check_type_float(eval_A(i, check_type_float(j))) * u_j))
    return check_type_float(partial_sum)
part_A_times_u = check_type_function(part_A_times_u)

def part_At_times_u(i_u):
    check_type_tuple(i_u, 2)
    (i, u) = i_u
    partial_sum = 0
    for (j, u_j) in check_type_function(enumerate)(u):
        check_type_tuple((j, u_j), 2)
        partial_sum = (partial_sum + (check_type_float(eval_A(check_type_float(j), i)) * u_j))
    return check_type_float(partial_sum)
part_At_times_u = check_type_function(part_At_times_u)
DEFAULT_N = 130

def main(n, timer):
    check_type_int(n)
    times = []
    for i in check_type_function(xrange)(n):
        t0 = check_type_function(timer)()
        u = check_type_list(([1] * DEFAULT_N))
        for dummy in check_type_function(xrange)(10):
            v = check_type_list(eval_AtA_times_u(check_type_list(u)))
            u = check_type_list(check_type_list(eval_AtA_times_u(v)))
        vBv = vv = 0
        for (ue, ve) in check_type_function(izip)(u, v):
            check_type_tuple((ue, ve), 2)
            vBv = (vBv + (ue * ve))
            vv = (vv + (ve * ve))
        tk = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((tk - t0)))
    return times
main = check_type_function(main)
if (__name__ == '__main__'):
    parser = check_type_function(check0(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check1(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check2(options).num_runs, main)
