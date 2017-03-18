from __future__ import division, print_function
from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check25(val):
    try:
        val.append
        return val
    except:
        raise CheckError(val)

def check6(val):
    try:
        val.next_cell_min_choice
        return val
    except:
        raise CheckError(val)

def check22(val):
    try:
        val.remove_unfixed
        return val
    except:
        raise CheckError(val)

def check30(val):
    try:
        val.strip
        return val
    except:
        raise CheckError(val)

def check8(val):
    try:
        val.next_cell_first
        return val
    except:
        raise CheckError(val)

def check21(val):
    try:
        val.cells
        return val
    except:
        raise CheckError(val)

def check31(val):
    try:
        val.getvalue
        return val
    except:
        raise CheckError(val)

def check10(val):
    try:
        val.next_cell_min_neighbors
        return val
    except:
        raise CheckError(val)

def check12(val):
    try:
        val.links
        val.pos
        val.id
        return val
    except:
        raise CheckError(val)

def check18(val):
    try:
        val.clone
        return val
    except:
        raise CheckError(val)

def check32(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)

def check33(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check11(val):
    try:
        val.count
        return val
    except:
        raise CheckError(val)

def check4(val):
    try:
        val.links
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.hex
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.get_by_id
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.y
        val.x
        return val
    except:
        raise CheckError(val)

def check27(val):
    try:
        val.get_by_pos
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.FIRST_STRATEGY
        val.MAX_NEIGHBORS_STRATEGY
        val.clone
        val.MIN_NEIGHBORS_STRATEGY
        val.filter_tiles
        val.__getitem__
        val.cells
        val.remove
        val.next_cell_highest_value
        val.MIN_CHOICE_STRATEGY
        val.next_cell_min_choice
        val.MAX_CHOICE_STRATEGY
        val.set_done
        val.HIGHEST_VALUE_STRATEGY
        val.remove_unfixed
        val.remove_all
        val.next_cell_min_neighbors
        val.next_cell_max_choice
        val.next_cell
        val.next_cell_max_neighbors
        val.count
        val.next_cell_first
        val.already_done
        return val
    except:
        raise CheckError(val)

def check28(val):
    try:
        val.id
        return val
    except:
        raise CheckError(val)

def check15(val):
    try:
        val.nodes_by_id
        val.link_nodes
        val.get_by_pos
        val.contains_pos
        val.size
        val.get_by_id
        val.count
        val.nodes_by_pos
        return val
    except:
        raise CheckError(val)

def check13(val):
    try:
        val.nodes_by_pos
        return val
    except:
        raise CheckError(val)

def check29(val):
    try:
        val.splitlines
        return val
    except:
        raise CheckError(val)

def check23(val):
    try:
        val.set_done
        return val
    except:
        raise CheckError(val)

def check24(val):
    try:
        val.next_cell
        return val
    except:
        raise CheckError(val)

def check26(val):
    try:
        val.size
        return val
    except:
        raise CheckError(val)

def check7(val):
    try:
        val.next_cell_max_choice
        return val
    except:
        raise CheckError(val)

def check19(val):
    try:
        val.already_done
        return val
    except:
        raise CheckError(val)

def check9(val):
    try:
        val.next_cell_max_neighbors
        return val
    except:
        raise CheckError(val)

def check16(val):
    try:
        val.tiles
        return val
    except:
        raise CheckError(val)

def check14(val):
    try:
        val.nodes_by_id
        return val
    except:
        raise CheckError(val)

def check17(val):
    try:
        val.done
        return val
    except:
        raise CheckError(val)

def check5(val):
    try:
        val.next_cell_highest_value
        return val
    except:
        raise CheckError(val)

def check20(val):
    try:
        val.remove
        return val
    except:
        raise CheckError(val)
import sys
import time
from compat import StringIO, u_lit, unicode, xrange


class Dir(retic_actual(object)):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    __init__ = check_type_function(__init__)
Dir = check_type_class(Dir, ['__init__'])
DIRS = [check0(Dir(1, 0)), check0(Dir((- 1), 0)), check0(Dir(0, 1)), check0(Dir(0, (- 1))), check0(Dir(1, 1)), check0(Dir((- 1), (- 1)))]
EMPTY = 7


class Done(retic_actual(object)):
    MIN_CHOICE_STRATEGY = 0
    MAX_CHOICE_STRATEGY = 1
    HIGHEST_VALUE_STRATEGY = 2
    FIRST_STRATEGY = 3
    MAX_NEIGHBORS_STRATEGY = 4
    MIN_NEIGHBORS_STRATEGY = 5

    def __init__(self, count, empty=False):
        self.count = count
        self.cells = ([] if empty else check_type_list([[0, 1, 2, 3, 4, 5, 6, EMPTY] for i in check_type_function(xrange)(count)]))
    __init__ = check_type_function(__init__)

    def clone(self):
        check1(self)
        ret = check1(check1(Done(check_type_int(self.count), True)))
        ret.cells = check_type_list([check_type_list(check_type_list(check_type_list(self.cells)[check_type_int(i)])[:]) for i in check_type_function(xrange)(check_type_int(self.count))])
        return check1(ret)
    clone = check_type_function(clone)

    def __getitem__(self, i):
        check1(self)
        check_type_int(i)
        return check_type_list(check_type_list(self.cells)[i])
    __getitem__ = check_type_function(__getitem__)

    def set_done(self, i, v):
        check1(self)
        check_type_int(i)
        check_type_int(v)
        check_type_list(self.cells)[i] = [v]
    set_done = check_type_function(set_done)

    def already_done(self, i):
        check1(self)
        check_type_int(i)
        return (check_type_function(len)(check_type_list(check_type_list(self.cells)[i])) == 1)
    already_done = check_type_function(already_done)

    def remove(self, i, v):
        check1(self)
        check_type_int(i)
        check_type_int(v)
        if (v in check_type_list(check_type_list(self.cells)[i])):
            check_type_function(check_type_list(check_type_list(self.cells)[i]).remove)(v)
            return True
        else:
            return False
    remove = check_type_function(remove)

    def remove_all(self, v):
        check1(self)
        check_type_int(v)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            check_type_bool(check_type_function(self.remove)(check_type_int(i), v))
    remove_all = check_type_function(remove_all)

    def remove_unfixed(self, v):
        check1(self)
        check_type_int(v)
        changed = False
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (not check_type_bool(check_type_function(self.already_done)(check_type_int(i)))):
                if check_type_bool(check_type_function(self.remove)(check_type_int(i), v)):
                    changed = True
        return check_type_bool(changed)
    remove_unfixed = check_type_function(remove_unfixed)

    def filter_tiles(self, tiles):
        check1(self)
        check_type_list(tiles)
        for v in check_type_function(xrange)(8):
            if (check_type_int(tiles[check_type_int(v)]) == 0):
                check_type_function(self.remove_all)(check_type_int(v))
    filter_tiles = check_type_function(filter_tiles)

    def next_cell_min_choice(self):
        check1(self)
        minlen = 10
        mini = (- 1)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (1 < check_type_function(len)(check_type_list(check_type_list(self.cells)[check_type_int(i)])) < minlen):
                minlen = check_type_function(len)(check_type_list(check_type_list(self.cells)[check_type_int(i)]))
                mini = i
        return check_type_int(mini)
    next_cell_min_choice = check_type_function(next_cell_min_choice)

    def next_cell_max_choice(self):
        check1(self)
        maxlen = 1
        maxi = (- 1)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (maxlen < check_type_function(len)(check_type_list(check_type_list(self.cells)[check_type_int(i)]))):
                maxlen = check_type_function(len)(check_type_list(check_type_list(self.cells)[check_type_int(i)]))
                maxi = i
        return check_type_int(maxi)
    next_cell_max_choice = check_type_function(next_cell_max_choice)

    def next_cell_highest_value(self):
        check1(self)
        maxval = (- 1)
        maxi = (- 1)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (not check_type_bool(check_type_function(self.already_done)(check_type_int(i)))):
                maxvali = check_type_function(max)((k for k in check_type_list(check_type_list(self.cells)[check_type_int(i)]) if (k != EMPTY)))
                if (maxval < maxvali):
                    maxval = maxvali
                    maxi = i
        return check_type_int(maxi)
    next_cell_highest_value = check_type_function(next_cell_highest_value)

    def next_cell_first(self):
        check1(self)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (not check_type_bool(check_type_function(self.already_done)(check_type_int(i)))):
                return check_type_int(i)
        return (- 1)
    next_cell_first = check_type_function(next_cell_first)

    def next_cell_max_neighbors(self, pos):
        check1(self)
        maxn = (- 1)
        maxi = (- 1)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (not check_type_bool(check_type_function(self.already_done)(check_type_int(i)))):
                cells_around = check4(check_type_function(check3(check2(pos).hex).get_by_id)(i)).links
                n = check_type_function(sum)(((1 if (check_type_bool(check_type_function(self.already_done)(check_type_int(nid))) and (self[nid][0] != EMPTY)) else 0) for nid in cells_around))
                if (n > maxn):
                    maxn = n
                    maxi = i
        return check_type_int(maxi)
    next_cell_max_neighbors = check_type_function(next_cell_max_neighbors)

    def next_cell_min_neighbors(self, pos):
        check1(self)
        minn = 7
        mini = (- 1)
        for i in check_type_function(xrange)(check_type_int(self.count)):
            if (not check_type_bool(check_type_function(self.already_done)(check_type_int(i)))):
                cells_around = check4(check_type_function(check3(check2(pos).hex).get_by_id)(i)).links
                n = check_type_function(sum)(((1 if (check_type_bool(check_type_function(self.already_done)(check_type_int(nid))) and (self[nid][0] != EMPTY)) else 0) for nid in cells_around))
                if (n < minn):
                    minn = n
                    mini = i
        return check_type_int(mini)
    next_cell_min_neighbors = check_type_function(next_cell_min_neighbors)

    def next_cell(self, pos, strategy=HIGHEST_VALUE_STRATEGY):
        if (strategy == Done.HIGHEST_VALUE_STRATEGY):
            return check_type_int(check_type_function(check5(self).next_cell_highest_value)())
        elif (strategy == Done.MIN_CHOICE_STRATEGY):
            return check_type_int(check_type_function(check6(self).next_cell_min_choice)())
        elif (strategy == Done.MAX_CHOICE_STRATEGY):
            return check_type_int(check_type_function(check7(self).next_cell_max_choice)())
        elif (strategy == Done.FIRST_STRATEGY):
            return check_type_int(check_type_function(check8(self).next_cell_first)())
        elif (strategy == Done.MAX_NEIGHBORS_STRATEGY):
            return check_type_int(check_type_function(check9(self).next_cell_max_neighbors)(pos))
        elif (strategy == Done.MIN_NEIGHBORS_STRATEGY):
            return check_type_int(check_type_function(check10(self).next_cell_min_neighbors)(pos))
        else:
            raise check_type_function(Exception)(('Wrong strategy: %d' % strategy))
    next_cell = check_type_function(next_cell)
Done = check_type_class(Done, ['FIRST_STRATEGY', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'MIN_NEIGHBORS_STRATEGY', 'filter_tiles', '__getitem__', 'remove', 'next_cell_highest_value', 'MIN_CHOICE_STRATEGY', 'next_cell_min_choice', 'MAX_CHOICE_STRATEGY', 'set_done', '__init__', 'HIGHEST_VALUE_STRATEGY', 'remove_unfixed', 'remove_all', 'next_cell_min_neighbors', 'next_cell_max_choice', 'next_cell', 'next_cell_max_neighbors', 'next_cell_first', 'already_done'])


class Node(retic_actual(object)):

    def __init__(self, pos, id, links):
        self.pos = pos
        self.id = id
        self.links = links
    __init__ = check_type_function(__init__)
Node = check_type_class(Node, ['__init__'])


class Hex(retic_actual(object)):

    def __init__(self, size):
        check_type_int(size)
        self.size = size
        self.count = (((3 * size) * (size - 1)) + 1)
        self.nodes_by_id = (check11(self).count * [None])
        self.nodes_by_pos = {}
        id = 0
        for y in check_type_function(xrange)(size):
            for x in check_type_function(xrange)((size + y)):
                pos = (x, y)
                node = check12(Node(pos, id, []))
                check13(self).nodes_by_pos[pos] = node
                check14(self).nodes_by_id[check_type_int(node.id)] = node
                id = (id + 1)
        for y in check_type_function(xrange)(1, size):
            for x in check_type_function(xrange)(y, ((size * 2) - 1)):
                ry = ((size + y) - 1)
                pos = (x, ry)
                node = check12(Node(pos, id, []))
                check13(self).nodes_by_pos[pos] = node
                check14(self).nodes_by_id[check_type_int(node.id)] = node
                id = (id + 1)
    __init__ = check_type_function(__init__)

    def link_nodes(self):
        check15(self)
        for node in check_type_list(self.nodes_by_id):
            check12(node)
            (x, y) = check_type_tuple(node.pos, 2)
            for dir in DIRS:
                check0(dir)
                nx = (x + check_type_int(dir.x))
                ny = (y + check_type_int(dir.y))
                if check_type_bool(check_type_function(self.contains_pos)(check_type_tuple((nx, ny), 2))):
                    check_type_void(check_type_function(check_type_list(node.links).append)(check_type_int(check12(check_type_dict(self.nodes_by_pos)[check_type_tuple((nx, ny), 2)]).id)))
    link_nodes = check_type_function(link_nodes)

    def contains_pos(self, pos):
        check15(self)
        check_type_tuple(pos, 2)
        return (pos in check_type_dict(self.nodes_by_pos))
    contains_pos = check_type_function(contains_pos)

    def get_by_pos(self, pos):
        check15(self)
        check_type_tuple(pos, 2)
        return check12(check_type_dict(self.nodes_by_pos)[pos])
    get_by_pos = check_type_function(get_by_pos)

    def get_by_id(self, id):
        check15(self)
        check_type_int(id)
        return check12(check_type_list(self.nodes_by_id)[id])
    get_by_id = check_type_function(get_by_id)
Hex = check_type_class(Hex, ['get_by_pos', 'link_nodes', 'get_by_id', '__init__', 'contains_pos'])


class Posn(retic_actual(object)):

    def __init__(self, hex, tiles, done=None):
        self.hex = hex
        self.tiles = tiles
        self.done = (check1(Done(check11(hex).count)) if (done is None) else done)
    __init__ = check_type_function(__init__)

    def clone(self):
        return check_type_function(Posn)(check2(self).hex, check16(self).tiles, check_type_function(check18(check17(self).done).clone)())
    clone = check_type_function(clone)
Posn = Posn

def constraint_pass(pos, last_move=None):
    changed = False
    left = check16(pos).tiles[:]
    done = check17(pos).done
    free_cells = (check_type_function(range)(check11(done).count) if (last_move is None) else check4(check_type_function(check3(check2(pos).hex).get_by_id)(last_move)).links)
    for i in free_cells:
        if (not check_type_function(check19(done).already_done)(i)):
            vmax = 0
            vmin = 0
            cells_around = check4(check_type_function(check3(check2(pos).hex).get_by_id)(i)).links
            for nid in cells_around:
                if check_type_function(check19(done).already_done)(nid):
                    if (done[nid][0] != EMPTY):
                        vmin = (vmin + 1)
                        vmax = (vmax + 1)
                else:
                    vmax = (vmax + 1)
            for num in check_type_function(xrange)(7):
                if ((num < vmin) or (num > vmax)):
                    if check_type_function(check20(done).remove)(i, num):
                        changed = True
    for cell in check21(done).cells:
        if (check_type_function(len)(cell) == 1):
            left[cell[0]] = (left[cell[0]] - 1)
    for v in check_type_function(xrange)(8):
        if ((check16(pos).tiles[v] > 0) and (left[v] == 0)):
            if check_type_function(check22(done).remove_unfixed)(v):
                changed = True
        else:
            possible = check_type_function(sum)(((1 if (v in cell) else 0) for cell in check21(done).cells))
            if (check16(pos).tiles[v] == possible):
                for i in check_type_function(xrange)(check11(done).count):
                    cell = check21(done).cells[i]
                    if ((not check_type_function(check19(done).already_done)(i)) and (v in cell)):
                        check_type_function(check23(done).set_done)(i, v)
                        changed = True
    filled_cells = (check_type_function(range)(check11(done).count) if (last_move is None) else [last_move])
    for i in filled_cells:
        if check_type_function(check19(done).already_done)(i):
            num = done[i][0]
            empties = 0
            filled = 0
            unknown = []
            cells_around = check4(check_type_function(check3(check2(pos).hex).get_by_id)(i)).links
            for nid in cells_around:
                if check_type_function(check19(done).already_done)(nid):
                    if (done[nid][0] == EMPTY):
                        empties = (empties + 1)
                    else:
                        filled = (filled + 1)
                else:
                    check_type_void(check_type_function(unknown.append)(nid))
            if (check_type_function(len)(unknown) > 0):
                if (num == filled):
                    for u in unknown:
                        if (EMPTY in done[u]):
                            check_type_function(check23(done).set_done)(u, EMPTY)
                            changed = True
                elif (num == (filled + check_type_function(len)(unknown))):
                    for u in unknown:
                        if check_type_function(check20(done).remove)(u, EMPTY):
                            changed = True
    return check_type_bool(changed)
constraint_pass = check_type_function(constraint_pass)
ASCENDING = 1
DESCENDING = (- 1)

def find_moves(pos, strategy, order):
    check_type_int(strategy)
    check_type_int(order)
    done = check17(pos).done
    cell_id = check_type_function(check24(done).next_cell)(pos, strategy)
    if (cell_id < 0):
        return []
    if (order == ASCENDING):
        return check_type_list([(cell_id, v) for v in done[cell_id]])
    else:
        moves = check_type_function(list)(check_type_function(reversed)(check_type_list([(cell_id, v) for v in done[cell_id] if (v != EMPTY)])))
        if (EMPTY in done[cell_id]):
            check_type_function(check25(moves).append)((cell_id, EMPTY))
        return moves
find_moves = check_type_function(find_moves)

def play_move(pos, move):
    check_type_tuple(move, 2)
    (cell_id, i) = move
    check_type_function(check23(check17(pos).done).set_done)(cell_id, i)
play_move = check_type_function(play_move)

def print_pos(pos, output):
    hex = check2(pos).hex
    done = check17(pos).done
    size = check26(hex).size
    for y in check_type_function(xrange)(size):
        check_type_function(print)((u_lit(' ') * ((size - y) - 1)), end=u_lit(''), file=output)
        for x in check_type_function(xrange)((size + y)):
            pos2 = (x, y)
            id = check28(check_type_function(check27(hex).get_by_pos)(pos2)).id
            if check_type_function(check19(done).already_done)(id):
                c = (check_type_function(unicode)(done[id][0]) if (done[id][0] != EMPTY) else u_lit('.'))
            else:
                c = u_lit('?')
            check_type_function(print)((u_lit('%s ') % c), end=u_lit(''), file=output)
        check_type_function(print)(end=u_lit('\n'), file=output)
    for y in check_type_function(xrange)(1, size):
        check_type_function(print)((u_lit(' ') * y), end=u_lit(''), file=output)
        for x in check_type_function(xrange)(y, ((size * 2) - 1)):
            ry = ((size + y) - 1)
            pos2 = (x, ry)
            id = check28(check_type_function(check27(hex).get_by_pos)(pos2)).id
            if check_type_function(check19(done).already_done)(id):
                c = (check_type_function(unicode)(done[id][0]) if (done[id][0] != EMPTY) else u_lit('.'))
            else:
                c = u_lit('?')
            check_type_function(print)((u_lit('%s ') % c), end=u_lit(''), file=output)
        check_type_function(print)(end=u_lit('\n'), file=output)
print_pos = check_type_function(print_pos)
OPEN = 0
SOLVED = 1
IMPOSSIBLE = (- 1)

def solved(pos, output, verbose=False):
    hex = check2(pos).hex
    tiles = check16(pos).tiles[:]
    done = check17(pos).done
    exact = True
    all_done = True
    for i in check_type_function(xrange)(check11(hex).count):
        if (check_type_function(len)(done[i]) == 0):
            return IMPOSSIBLE
        elif check_type_function(check19(done).already_done)(i):
            num = done[i][0]
            tiles[num] = (tiles[num] - 1)
            if (tiles[num] < 0):
                return IMPOSSIBLE
            vmax = 0
            vmin = 0
            if (num != EMPTY):
                cells_around = check4(check_type_function(check3(hex).get_by_id)(i)).links
                for nid in cells_around:
                    if check_type_function(check19(done).already_done)(nid):
                        if (done[nid][0] != EMPTY):
                            vmin = (vmin + 1)
                            vmax = (vmax + 1)
                    else:
                        vmax = (vmax + 1)
                if ((num < vmin) or (num > vmax)):
                    return IMPOSSIBLE
                if (num != vmin):
                    exact = False
        else:
            all_done = False
    if ((not all_done) or (not exact)):
        return OPEN
    print_pos(pos, output)
    return SOLVED
solved = check_type_function(solved)

def solve_step(prev, strategy, order, output, first=False):
    if first:
        pos = check_type_function(check18(prev).clone)()
        while check_type_bool(constraint_pass(pos)):
            pass
    else:
        pos = prev
    moves = find_moves(pos, check_type_int(strategy), check_type_int(order))
    if (check_type_function(len)(moves) == 0):
        return check_type_int(solved(pos, output))
    else:
        for move in moves:
            ret = OPEN
            new_pos = check_type_function(check18(pos).clone)()
            play_move(new_pos, check_type_tuple(move, 2))
            while check_type_bool(constraint_pass(new_pos, move[0])):
                pass
            cur_status = check_type_int(solved(new_pos, output))
            if (cur_status != OPEN):
                ret = cur_status
            else:
                ret = check_type_int(solve_step(new_pos, strategy, order, output))
            if (ret == SOLVED):
                return SOLVED
    return IMPOSSIBLE
solve_step = check_type_function(solve_step)

def check_valid(pos):
    hex = check2(pos).hex
    tiles = check16(pos).tiles
    done = check17(pos).done
    tot = 0
    for i in check_type_function(xrange)(8):
        if (tiles[i] > 0):
            tot = (tot + tiles[i])
        else:
            tiles[i] = 0
    if (tot != check11(hex).count):
        raise check_type_function(Exception)(('Invalid input. Expected %d tiles, got %d.' % (check11(hex).count, tot)))
check_valid = check_type_function(check_valid)

def solve(pos, strategy, order, output):
    check_type_int(strategy)
    check_type_int(order)
    check_valid(pos)
    return check_type_int(solve_step(pos, strategy, order, output, first=True))
solve = check_type_function(solve)

def read_file(file):
    lines = check_type_list([check_type_function(check30(line).strip)('\r\n') for line in check_type_function(check29(file).splitlines)()])
    size = check_type_function(int)(lines[0])
    hex = check15(check15(Hex(check_type_int(size))))
    linei = 1
    tiles = (8 * [0])
    done = check1(check1(Done(check_type_int(hex.count))))
    for y in check_type_function(xrange)(size):
        line = lines[check_type_int(linei)][((size - y) - 1):]
        p = 0
        for x in check_type_function(xrange)((size + y)):
            tile = line[p:(p + 2)]
            p = (p + 2)
            if (tile[1] == '.'):
                inctile = EMPTY
            else:
                inctile = check_type_function(int)(tile)
            tiles[check_type_int(inctile)] = (check_type_int(tiles[check_type_int(inctile)]) + 1)
            if (tile[0] == '+'):
                check_type_function(print)(('Adding locked tile: %d at pos %d, %d, id=%d' % (inctile, x, y, check_type_int(check12(check_type_function(hex.get_by_pos)(check_type_tuple((x, y), 2))).id))))
                check_type_function(done.set_done)(check_type_int(check12(check_type_function(hex.get_by_pos)(check_type_tuple((x, y), 2))).id), check_type_int(inctile))
        linei = (linei + 1)
    for y in check_type_function(xrange)(1, size):
        ry = ((size - 1) + y)
        line = lines[check_type_int(linei)][y:]
        p = 0
        for x in check_type_function(xrange)(y, ((size * 2) - 1)):
            tile = line[p:(p + 2)]
            p = (p + 2)
            if (tile[1] == '.'):
                inctile = EMPTY
            else:
                inctile = check_type_function(int)(tile)
            tiles[check_type_int(inctile)] = (check_type_int(tiles[check_type_int(inctile)]) + 1)
            if (tile[0] == '+'):
                check_type_function(print)(('Adding locked tile: %d at pos %d, %d, id=%d' % (inctile, x, ry, check_type_int(check12(check_type_function(hex.get_by_pos)(check_type_tuple((x, ry), 2))).id))))
                check_type_function(done.set_done)(check_type_int(check12(check_type_function(hex.get_by_pos)(check_type_tuple((x, ry), 2))).id), check_type_int(inctile))
        linei = (linei + 1)
    check_type_function(hex.link_nodes)()
    check_type_function(done.filter_tiles)(tiles)
    return check_type_function(Posn)(hex, tiles, done)
read_file = check_type_function(read_file)

def solve_file(file, strategy, order, output):
    check_type_int(strategy)
    check_type_int(order)
    pos = read_file(file)
    check_type_int(solve(pos, strategy, order, output))
solve_file = check_type_function(solve_file)

def run_level36():
    f = '4\n    2 1 1 2\n   3 3 3 . .\n  2 3 3 . 4 .\n . 2 . 2 4 3 2\n  2 2 . . . 2\n   4 3 4 . .\n    3 2 3 3\n'
    order = DESCENDING
    strategy = Done.FIRST_STRATEGY
    output = check_type_function(StringIO)()
    solve_file(f, check_type_int(strategy), order, output)
    expected = '   3 4 3 2 \n  3 4 4 . 3 \n 2 . . 3 4 3 \n2 . 1 . 3 . 2 \n 3 3 . 2 . 2 \n  3 . 2 . 2 \n   2 2 . 1 \n'
    if (check_type_function(check31(output).getvalue)() != expected):
        raise check_type_function(AssertionError)(('got a wrong answer:\n%s' % check_type_function(check31(output).getvalue)()))
run_level36 = check_type_function(run_level36)

def main(n, timer):
    l = []
    for i in check_type_function(xrange)(n):
        t0 = check_type_function(timer)()
        run_level36()
        time_elapsed = (check_type_function(timer)() - t0)
        check_type_void(check_type_function(l.append)(time_elapsed))
    return l
main = check_type_function(main)
if (__name__ == '__main__'):
    import util, optparse
    parser = check_type_function(check32(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of the hexiom2 benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check33(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, 1, main)
