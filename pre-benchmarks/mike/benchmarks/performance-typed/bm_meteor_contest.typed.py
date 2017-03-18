from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check2(val):
    try:
        val.insert
        return val
    except:
        raise CheckError(val)

def check5(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.remove
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.append
        return val
    except:
        raise CheckError(val)

def check4(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)
import optparse
import sys
import time
from bisect import bisect
from compat import xrange
import util
(w, h) = (5, 10)
dir_no = 6
(S, E) = check_type_tuple(((w * h), 2), 2)
SE = (S + (E / 2))
SW = (SE - E)
(W, NW, NE) = check_type_tuple(((- E), (- SE), (- SW)), 3)

def rotate(ido, rd={E: NE, NE: NW, NW: W, W: SW, SW: SE, SE: E, }):
    return check_type_list(check_type_list([rd[o] for o in ido]))
rotate = check_type_function(rotate)

def flip(ido, fd={E: E, NE: SE, NW: SW, W: W, SW: NW, SE: NE, }):
    return check_type_list(check_type_list([fd[o] for o in ido]))
flip = check_type_function(flip)

def permute(ido, r_ido, rotate=rotate, flip=flip):
    ps = [ido]
    for r in check_type_function(xrange)((dir_no - 1)):
        check_type_function(check0(ps).append)(check_type_function(rotate)(ps[(- 1)]))
        if (ido == r_ido):
            ps = ps[0:(dir_no // 2)]
    for pp in ps[:]:
        check_type_function(check0(ps).append)(check_type_function(flip)(pp))
    return check_type_list(ps)
permute = check_type_function(permute)

def convert(ido):
    check_type_list(ido)
    out = [0.0]
    for o in ido:
        check_type_float(o)
        check_type_void(check_type_function(out.append)((check_type_float(out[(- 1)]) + o)))
    return check_type_list(check_type_function(list)(check_type_function(set)(out)))
convert = check_type_function(convert)

def get_footprints(board, cti, pieces):
    check_type_list(board)
    check_type_dict(cti)
    check_type_list(pieces)
    fps = check_type_list([check_type_list([[] for p in check_type_function(xrange)(check_type_function(len)(pieces))]) for ci in check_type_function(xrange)(check_type_function(len)(board))])
    for c in board:
        check_type_float(c)
        for (pi, p) in check_type_function(enumerate)(pieces):
            check_type_tuple((pi, p), 2)
            for pp in p:
                fp = check_type_function(frozenset)(check_type_list([check_type_int(cti[check_type_float((c + o))]) for o in pp if ((c + o) in cti)]))
                if (check_type_function(len)(fp) == 5):
                    check_type_void(check_type_function(check_type_list(check_type_list(fps[check_type_int(check_type_function(min)(fp))])[check_type_int(pi)]).append)(fp))
    return check_type_list(fps)
get_footprints = check_type_function(get_footprints)

def get_senh(board, cti):
    check_type_list(board)
    check_type_dict(cti)
    se_nh = []
    nh = [E, SW, SE]
    for c in board:
        check_type_float(c)
        check_type_void(check_type_function(se_nh.append)(check_type_function(frozenset)(check_type_list([check_type_int(cti[check_type_float((c + o))]) for o in nh if ((c + o) in cti)]))))
    return check_type_list(se_nh)
get_senh = check_type_function(get_senh)

def get_puzzle(w=w, h=h):
    board = check_type_list([(((E * x) + (S * y)) + (y % 2)) for y in check_type_function(xrange)(h) for x in check_type_function(xrange)(w)])
    cti = check_type_function(dict)(((board[check_type_int(i)], i) for i in check_type_function(xrange)(check_type_function(len)(board))))
    idos = [[E, E, E, SE], [SE, SW, W, SW], [W, W, SW, SE], [E, E, SW, SE], [NW, W, NW, SE, SW], [E, E, NE, W], [NW, NE, NE, W], [NE, SE, E, NE], [SE, SE, E, SE], [E, NW, NW, NW]]
    perms = (check_type_list(permute(p, check_type_list(idos[3]))) for p in idos)
    pieces = check_type_list([check_type_list([check_type_list(convert(check_type_list(pp))) for pp in p]) for p in perms])
    return check_type_tuple((board, cti, pieces), 3)
get_puzzle = check_type_function(get_puzzle)

def print_board(board, w=w, h=h):
    for y in check_type_function(xrange)(h):
        for x in check_type_function(xrange)(w):
            check_type_function(print)(board[(x + (y * w))])
        check_type_function(print)('')
        if ((y % 2) == 0):
            check_type_function(print)('')
    check_type_function(print)()
print_board = check_type_function(print_board)
(board, cti, pieces) = check_type_tuple(get_puzzle(), 3)
fps = check_type_list(get_footprints(board, cti, pieces))
se_nh = check_type_list(get_senh(board, cti))

def solve(n, i_min, free, curr_board, pieces_left, solutions, fps=fps, se_nh=se_nh, bisect=bisect):
    fp_i_cands = fps[i_min]
    for p in pieces_left:
        fp_cands = fp_i_cands[p]
        for fp in fp_cands:
            if (fp <= free):
                n_curr_board = curr_board[:]
                for ci in fp:
                    n_curr_board[ci] = p
                if (check_type_function(len)(pieces_left) > 1):
                    n_free = (free - fp)
                    n_i_min = check_type_function(min)(n_free)
                    if (check_type_function(len)((n_free & se_nh[n_i_min])) > 0):
                        n_pieces_left = pieces_left[:]
                        check_type_function(check1(n_pieces_left).remove)(p)
                        check_type_void(solve(n, n_i_min, n_free, n_curr_board, n_pieces_left, solutions))
                else:
                    s = check_type_function(''.join)(check_type_function(map)(str, n_curr_board))
                    check_type_function(check2(solutions).insert)(check_type_function(bisect)(solutions, s), s)
                    rs = s[::(- 1)]
                    check_type_function(check2(solutions).insert)(check_type_function(bisect)(solutions, rs), rs)
                    if (check_type_function(len)(solutions) >= n):
                        return
        if (check_type_function(len)(solutions) >= n):
            return
    return
solve = check_type_function(solve)
SOLVE_ARG = 60

def main(n, timer):
    check_type_int(n)
    times = []
    for i in check_type_function(xrange)(n):
        t0 = check_type_function(timer)()
        free = check_type_function(frozenset)(check_type_function(xrange)(check_type_function(len)(board)))
        curr_board = ([(- 1)] * check_type_function(len)(board))
        pieces_left = check_type_function(list)(check_type_function(range)(check_type_function(len)(pieces)))
        solutions = []
        check_type_void(solve(SOLVE_ARG, 0, free, curr_board, pieces_left, solutions))
        tk = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((tk - t0)))
    return times
main = check_type_function(main)
if (__name__ == '__main__'):
    parser = check_type_function(check3(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of the Float benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check4(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check5(options).num_runs, main)
