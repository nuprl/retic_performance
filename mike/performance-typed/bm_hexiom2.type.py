from retic.runtime import *
from retic.transient import *
from retic.typing import *
from __future__ import division, print_function
import sys
import time
from compat import StringIO, u_lit, unicode, xrange


@fields({'x': int, 'y': int, })
class Dir(retic_actual(object)):
    retic_class_type = Class('Dir', {'__init__': Function(NamedParameters([('self', Dyn), ('x', Dyn), ('y', Dyn)]), Dyn), }, {'x': Int, 'y': Int, })

    def __init__(self, x, y):
        self.x = x
        self.y = y
    __init__ = check_type_function(__init__)
Dir = check_type_class(Dir, ['__init__'])
DIRS = [check_type_object(Dir(1, 0), ['x', 'y']), check_type_object(Dir((- 1), 0), ['x', 'y']), check_type_object(Dir(0, 1), ['x', 'y']), check_type_object(Dir(0, (- 1)), ['x', 'y']), check_type_object(Dir(1, 1), ['x', 'y']), check_type_object(Dir((- 1), (- 1)), ['x', 'y'])]
EMPTY = 7


@fields({'count': int, 'cells': List(List(int)), })
class Done(retic_actual(object)):
    retic_class_type = Class('Done', {'next_cell_max_neighbors': Function(NamedParameters([('self', Dyn), ('pos', Dyn)]), Int), 'filter_tiles': Function(NamedParameters([('self', Dyn), ('tiles', List(Int))]), Dyn), 'MIN_CHOICE_STRATEGY': Dyn, 'remove_all': Function(NamedParameters([('self', Dyn), ('v', Int)]), Dyn), 'next_cell_min_choice': Function(NamedParameters([('self', Dyn)]), Int), 'FIRST_STRATEGY': Dyn, '__getitem__': Function(NamedParameters([('self', Dyn), ('i', Int)]), List(Int)), 'HIGHEST_VALUE_STRATEGY': Dyn, '__init__': Function(DynParameters, Dyn), 'next_cell': Function(DynParameters, Int), 'MAX_NEIGHBORS_STRATEGY': Dyn, 'clone': Function(NamedParameters([('self', Dyn)]), TypeVariable('Done')), 'next_cell_highest_value': Function(NamedParameters([('self', Dyn)]), Int), 'set_done': Function(NamedParameters([('self', Dyn), ('i', Int), ('v', Int)]), Dyn), 'next_cell_first': Function(NamedParameters([('self', Dyn)]), Int), 'MIN_NEIGHBORS_STRATEGY': Dyn, 'next_cell_min_neighbors': Function(NamedParameters([('self', Dyn), ('pos', Dyn)]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('self', Dyn), ('i', Int), ('v', Int)]), Bool), 'already_done': Function(NamedParameters([('self', Dyn), ('i', Int)]), Bool), 'remove_unfixed': Function(NamedParameters([('self', Dyn), ('v', Int)]), Bool), 'next_cell_max_choice': Function(NamedParameters([('self', Dyn)]), Int), }, {'cells': List(List(Int)), 'count': Int, })
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
        ret = check_type_object(check_type_object(Done(check_type_object(self, ['count']).count, True), ['cells', 'count', 'next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice']), ['cells', 'count', 'next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice'])
        ret.cells = check_type_list(check_type_list([check_type_object(self, ['cells']).cells[i][:] for i in check_type_function(xrange)(check_type_object(self, ['count']).count)]))
        return check_type_object(ret, ['cells', 'count', 'next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice'])
    clone = check_type_function(clone)

    def __getitem__(self, i):
        check_type_int(i)
        return check_type_list(check_type_object(self, ['cells']).cells[i])
    __getitem__ = check_type_function(__getitem__)

    def set_done(self, i, v):
        check_type_int(i)
        check_type_int(v)
        check_type_object(self, ['cells']).cells[i] = [v]
    set_done = check_type_function(set_done)

    def already_done(self, i):
        check_type_int(i)
        return (check_type_function(len)(check_type_object(self, ['cells']).cells[i]) == 1)
    already_done = check_type_function(already_done)

    def remove(self, i, v):
        check_type_int(i)
        check_type_int(v)
        if (v in check_type_object(self, ['cells']).cells[i]):
            check_type_function(check_type_object(check_type_object(self, ['cells']).cells[i], ['remove']).remove)(v)
            return True
        else:
            return False
    remove = check_type_function(remove)

    def remove_all(self, v):
        check_type_int(v)
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            check_type_function(check_type_object(self, ['remove']).remove)(i, v)
    remove_all = check_type_function(remove_all)

    def remove_unfixed(self, v):
        check_type_int(v)
        changed = False
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (not check_type_function(check_type_object(self, ['already_done']).already_done)(i)):
                if check_type_function(check_type_object(self, ['remove']).remove)(i, v):
                    changed = True
        return check_type_bool(changed)
    remove_unfixed = check_type_function(remove_unfixed)

    def filter_tiles(self, tiles):
        check_type_list(tiles)
        for v in check_type_function(xrange)(8):
            if (check_type_int(tiles[check_type_int(v)]) == 0):
                check_type_function(check_type_object(self, ['remove_all']).remove_all)(v)
    filter_tiles = check_type_function(filter_tiles)

    def next_cell_min_choice(self):
        minlen = 10
        mini = (- 1)
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (1 < check_type_function(len)(check_type_object(self, ['cells']).cells[i]) < minlen):
                minlen = check_type_function(len)(check_type_object(self, ['cells']).cells[i])
                mini = i
        return check_type_int(mini)
    next_cell_min_choice = check_type_function(next_cell_min_choice)

    def next_cell_max_choice(self):
        maxlen = 1
        maxi = (- 1)
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (maxlen < check_type_function(len)(check_type_object(self, ['cells']).cells[i])):
                maxlen = check_type_function(len)(check_type_object(self, ['cells']).cells[i])
                maxi = i
        return check_type_int(maxi)
    next_cell_max_choice = check_type_function(next_cell_max_choice)

    def next_cell_highest_value(self):
        maxval = (- 1)
        maxi = (- 1)
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (not check_type_function(check_type_object(self, ['already_done']).already_done)(i)):
                maxvali = check_type_function(max)((k for k in check_type_object(self, ['cells']).cells[i] if (k != EMPTY)))
                if (maxval < maxvali):
                    maxval = maxvali
                    maxi = i
        return check_type_int(maxi)
    next_cell_highest_value = check_type_function(next_cell_highest_value)

    def next_cell_first(self):
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (not check_type_function(check_type_object(self, ['already_done']).already_done)(i)):
                return check_type_int(i)
        return (- 1)
    next_cell_first = check_type_function(next_cell_first)

    def next_cell_max_neighbors(self, pos):
        maxn = (- 1)
        maxi = (- 1)
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (not check_type_function(check_type_object(self, ['already_done']).already_done)(i)):
                cells_around = check_type_object(check_type_function(check_type_object(check_type_object(pos, ['hex']).hex, ['get_by_id']).get_by_id)(i), ['links']).links
                n = check_type_function(sum)(((1 if (check_type_function(check_type_object(self, ['already_done']).already_done)(nid) and (self[nid][0] != EMPTY)) else 0) for nid in cells_around))
                if (n > maxn):
                    maxn = n
                    maxi = i
        return check_type_int(maxi)
    next_cell_max_neighbors = check_type_function(next_cell_max_neighbors)

    def next_cell_min_neighbors(self, pos):
        minn = 7
        mini = (- 1)
        for i in check_type_function(xrange)(check_type_object(self, ['count']).count):
            if (not check_type_function(check_type_object(self, ['already_done']).already_done)(i)):
                cells_around = check_type_object(check_type_function(check_type_object(check_type_object(pos, ['hex']).hex, ['get_by_id']).get_by_id)(i), ['links']).links
                n = check_type_function(sum)(((1 if (check_type_function(check_type_object(self, ['already_done']).already_done)(nid) and (self[nid][0] != EMPTY)) else 0) for nid in cells_around))
                if (n < minn):
                    minn = n
                    mini = i
        return check_type_int(mini)
    next_cell_min_neighbors = check_type_function(next_cell_min_neighbors)

    def next_cell(self, pos, strategy=HIGHEST_VALUE_STRATEGY):
        if (strategy == Done.HIGHEST_VALUE_STRATEGY):
            return check_type_int(check_type_function(check_type_object(self, ['next_cell_highest_value']).next_cell_highest_value)())
        elif (strategy == Done.MIN_CHOICE_STRATEGY):
            return check_type_int(check_type_function(check_type_object(self, ['next_cell_min_choice']).next_cell_min_choice)())
        elif (strategy == Done.MAX_CHOICE_STRATEGY):
            return check_type_int(check_type_function(check_type_object(self, ['next_cell_max_choice']).next_cell_max_choice)())
        elif (strategy == Done.FIRST_STRATEGY):
            return check_type_int(check_type_function(check_type_object(self, ['next_cell_first']).next_cell_first)())
        elif (strategy == Done.MAX_NEIGHBORS_STRATEGY):
            return check_type_int(check_type_function(check_type_object(self, ['next_cell_max_neighbors']).next_cell_max_neighbors)(pos))
        elif (strategy == Done.MIN_NEIGHBORS_STRATEGY):
            return check_type_int(check_type_function(check_type_object(self, ['next_cell_min_neighbors']).next_cell_min_neighbors)(pos))
        else:
            raise check_type_function(Exception)(('Wrong strategy: %d' % strategy))
    next_cell = check_type_function(next_cell)
Done = check_type_class(Done, ['next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', '__init__', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice'])


@fields({'pos': Posn, 'id': int, 'links': List(Node), })
class Node(retic_actual(object)):
    retic_class_type = Class('Node', {'__init__': Function(NamedParameters([('self', Dyn), ('pos', Dyn), ('id', Dyn), ('links', Dyn)]), Dyn), }, {'pos': Dyn, 'id': Int, 'links': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(TypeVariable('Node')), })), })), })

    def __init__(self, pos, id, links):
        self.pos = pos
        self.id = id
        self.links = links
    __init__ = check_type_function(__init__)
Node = check_type_class(Node, ['__init__'])


@fields({'size': int, 'count': int, 'nodes_by_id': List(Node), 'nodes_by_pos': Dict(int, Node), })
class Hex(retic_actual(object)):
    retic_class_type = Class('Hex', {'get_by_id': Function(NamedParameters([('self', Dyn), ('id', Int)]), Object('Node', {'pos': Dyn, 'id': Int, 'links': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(TypeVariable('Node')), })), })), '__init__': Function(NamedParameters([('self', Dyn), ('size', Int)]), Dyn), 'link_nodes': Function(NamedParameters([('self', Dyn)]), Dyn), 'get_by_pos': Function(NamedParameters([('self', Dyn), ('pos', Tuple(Int, Int))]), Object('Node', {'pos': Dyn, 'id': Int, 'links': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(TypeVariable('Node')), })), })), 'contains_pos': Function(NamedParameters([('self', Dyn), ('pos', Int)]), Bool), }, {'nodes_by_id': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(TypeVariable('Node')), })), })), 'count': Int, 'size': Int, 'nodes_by_pos': Dict(Int, Object('Node', {'pos': Dyn, 'id': Int, 'links': List(Object('Node', {'pos': Dyn, 'id': Int, 'links': List(TypeVariable('Node')), })), })), })

    def __init__(self, size):
        check_type_int(size)
        self.size = size
        self.count = (((3 * size) * (size - 1)) + 1)
        self.nodes_by_id = (check_type_object(self, ['count']).count * [None])
        self.nodes_by_pos = {}
        id = 0
        for y in check_type_function(xrange)(size):
            for x in check_type_function(xrange)((size + y)):
                pos = (x, y)
                node = check_type_object(Node(pos, id, []), ['pos', 'id', 'links'])
                check_type_object(self, ['nodes_by_pos']).nodes_by_pos[pos] = node
                check_type_object(self, ['nodes_by_id']).nodes_by_id[check_type_int(node.id)] = node
                id = (id + 1)
        for y in check_type_function(xrange)(1, size):
            for x in check_type_function(xrange)(y, ((size * 2) - 1)):
                ry = ((size + y) - 1)
                pos = (x, ry)
                node = check_type_object(Node(pos, id, []), ['pos', 'id', 'links'])
                check_type_object(self, ['nodes_by_pos']).nodes_by_pos[pos] = node
                check_type_object(self, ['nodes_by_id']).nodes_by_id[check_type_int(node.id)] = node
                id = (id + 1)
    __init__ = check_type_function(__init__)

    def link_nodes(self):
        for node in check_type_object(self, ['nodes_by_id']).nodes_by_id:
            (x, y) = check_type_tuple(check_type_object(node, ['pos']).pos, 2)
            for dir in DIRS:
                check_type_object(dir, ['x', 'y'])
                nx = (x + check_type_int(dir.x))
                ny = (y + check_type_int(dir.y))
                if check_type_function(check_type_object(self, ['contains_pos']).contains_pos)((nx, ny)):
                    check_type_function(check_type_object(check_type_object(node, ['links']).links, ['append']).append)(check_type_object(check_type_object(self, ['nodes_by_pos']).nodes_by_pos[(nx, ny)], ['id']).id)
    link_nodes = check_type_function(link_nodes)

    def contains_pos(self, pos):
        check_type_int(pos)
        return (pos in check_type_object(self, ['nodes_by_pos']).nodes_by_pos)
    contains_pos = check_type_function(contains_pos)

    def get_by_pos(self, pos):
        check_type_tuple(pos, 2)
        return check_type_object(check_type_object(self, ['nodes_by_pos']).nodes_by_pos[pos], ['pos', 'id', 'links'])
    get_by_pos = check_type_function(get_by_pos)

    def get_by_id(self, id):
        check_type_int(id)
        return check_type_object(check_type_object(self, ['nodes_by_id']).nodes_by_id[id], ['pos', 'id', 'links'])
    get_by_id = check_type_function(get_by_id)
Hex = check_type_class(Hex, ['get_by_id', '__init__', 'link_nodes', 'get_by_pos', 'contains_pos'])


@fields({'hex': Hex, tiles: List(int), })
class Posn(retic_actual(object)):
    retic_class_type = Dyn

    def __init__(self, hex, tiles, done=None):
        self.hex = hex
        self.tiles = tiles
        self.done = (check_type_object(Done(check_type_object(hex, ['count']).count), ['cells', 'count', 'next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice']) if (done is None) else done)
    __init__ = check_type_function(__init__)

    def clone(self):
        return check_type_function(Posn)(check_type_object(self, ['hex']).hex, check_type_object(self, ['tiles']).tiles, check_type_function(check_type_object(check_type_object(self, ['done']).done, ['clone']).clone)())
    clone = check_type_function(clone)
Posn = Posn

def constraint_pass(pos, last_move=None):
    changed = False
    left = check_type_object(pos, ['tiles']).tiles[:]
    done = check_type_object(pos, ['done']).done
    free_cells = (check_type_function(range)(check_type_object(done, ['count']).count) if (last_move is None) else check_type_object(check_type_function(check_type_object(check_type_object(pos, ['hex']).hex, ['get_by_id']).get_by_id)(last_move), ['links']).links)
    for i in free_cells:
        if (not check_type_function(check_type_object(done, ['already_done']).already_done)(i)):
            vmax = 0
            vmin = 0
            cells_around = check_type_object(check_type_function(check_type_object(check_type_object(pos, ['hex']).hex, ['get_by_id']).get_by_id)(i), ['links']).links
            for nid in cells_around:
                if check_type_function(check_type_object(done, ['already_done']).already_done)(nid):
                    if (done[nid][0] != EMPTY):
                        vmin = (vmin + 1)
                        vmax = (vmax + 1)
                else:
                    vmax = (vmax + 1)
            for num in check_type_function(xrange)(7):
                if ((num < vmin) or (num > vmax)):
                    if check_type_function(check_type_object(done, ['remove']).remove)(i, num):
                        changed = True
    for cell in check_type_object(done, ['cells']).cells:
        if (check_type_function(len)(cell) == 1):
            left[cell[0]] = (left[cell[0]] - 1)
    for v in check_type_function(xrange)(8):
        if ((check_type_object(pos, ['tiles']).tiles[v] > 0) and (left[v] == 0)):
            if check_type_function(check_type_object(done, ['remove_unfixed']).remove_unfixed)(v):
                changed = True
        else:
            possible = check_type_function(sum)(((1 if (v in cell) else 0) for cell in check_type_object(done, ['cells']).cells))
            if (check_type_object(pos, ['tiles']).tiles[v] == possible):
                for i in check_type_function(xrange)(check_type_object(done, ['count']).count):
                    cell = check_type_object(done, ['cells']).cells[i]
                    if ((not check_type_function(check_type_object(done, ['already_done']).already_done)(i)) and (v in cell)):
                        check_type_function(check_type_object(done, ['set_done']).set_done)(i, v)
                        changed = True
    filled_cells = (check_type_function(range)(check_type_object(done, ['count']).count) if (last_move is None) else [last_move])
    for i in filled_cells:
        if check_type_function(check_type_object(done, ['already_done']).already_done)(i):
            num = done[i][0]
            empties = 0
            filled = 0
            unknown = []
            cells_around = check_type_object(check_type_function(check_type_object(check_type_object(pos, ['hex']).hex, ['get_by_id']).get_by_id)(i), ['links']).links
            for nid in cells_around:
                if check_type_function(check_type_object(done, ['already_done']).already_done)(nid):
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
                            check_type_function(check_type_object(done, ['set_done']).set_done)(u, EMPTY)
                            changed = True
                elif (num == (filled + check_type_function(len)(unknown))):
                    for u in unknown:
                        if check_type_function(check_type_object(done, ['remove']).remove)(u, EMPTY):
                            changed = True
    return check_type_bool(changed)
constraint_pass = check_type_function(constraint_pass)
ASCENDING = 1
DESCENDING = (- 1)

def find_moves(pos, strategy, order):
    check_type_int(strategy)
    check_type_int(order)
    done = check_type_object(pos, ['done']).done
    cell_id = check_type_function(check_type_object(done, ['next_cell']).next_cell)(pos, strategy)
    if (cell_id < 0):
        return []
    if (order == ASCENDING):
        return check_type_list([(cell_id, v) for v in done[cell_id]])
    else:
        moves = check_type_function(list)(check_type_function(reversed)(check_type_list([(cell_id, v) for v in done[cell_id] if (v != EMPTY)])))
        if (EMPTY in done[cell_id]):
            check_type_function(check_type_object(moves, ['append']).append)((cell_id, EMPTY))
        return moves
find_moves = check_type_function(find_moves)

def play_move(pos, move):
    check_type_tuple(move, 2)
    (cell_id, i) = move
    check_type_function(check_type_object(check_type_object(pos, ['done']).done, ['set_done']).set_done)(cell_id, i)
play_move = check_type_function(play_move)

def print_pos(pos, output):
    hex = check_type_object(pos, ['hex']).hex
    done = check_type_object(pos, ['done']).done
    size = check_type_object(hex, ['size']).size
    for y in check_type_function(xrange)(size):
        check_type_function(print)((u_lit(' ') * ((size - y) - 1)), end=u_lit(''), file=output)
        for x in check_type_function(xrange)((size + y)):
            pos2 = (x, y)
            id = check_type_object(check_type_function(check_type_object(hex, ['get_by_pos']).get_by_pos)(pos2), ['id']).id
            if check_type_function(check_type_object(done, ['already_done']).already_done)(id):
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
            id = check_type_object(check_type_function(check_type_object(hex, ['get_by_pos']).get_by_pos)(pos2), ['id']).id
            if check_type_function(check_type_object(done, ['already_done']).already_done)(id):
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
    hex = check_type_object(pos, ['hex']).hex
    tiles = check_type_object(pos, ['tiles']).tiles[:]
    done = check_type_object(pos, ['done']).done
    exact = True
    all_done = True
    for i in check_type_function(xrange)(check_type_object(hex, ['count']).count):
        if (check_type_function(len)(done[i]) == 0):
            return IMPOSSIBLE
        elif check_type_function(check_type_object(done, ['already_done']).already_done)(i):
            num = done[i][0]
            tiles[num] = (tiles[num] - 1)
            if (tiles[num] < 0):
                return IMPOSSIBLE
            vmax = 0
            vmin = 0
            if (num != EMPTY):
                cells_around = check_type_object(check_type_function(check_type_object(hex, ['get_by_id']).get_by_id)(i), ['links']).links
                for nid in cells_around:
                    if check_type_function(check_type_object(done, ['already_done']).already_done)(nid):
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
        pos = check_type_function(check_type_object(prev, ['clone']).clone)()
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
            new_pos = check_type_function(check_type_object(pos, ['clone']).clone)()
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
    hex = check_type_object(pos, ['hex']).hex
    tiles = check_type_object(pos, ['tiles']).tiles
    done = check_type_object(pos, ['done']).done
    tot = 0
    for i in check_type_function(xrange)(8):
        if (tiles[i] > 0):
            tot = (tot + tiles[i])
        else:
            tiles[i] = 0
    if (tot != check_type_object(hex, ['count']).count):
        raise check_type_function(Exception)(('Invalid input. Expected %d tiles, got %d.' % (check_type_object(hex, ['count']).count, tot)))
check_valid = check_type_function(check_valid)

def solve(pos, strategy, order, output):
    check_type_int(strategy)
    check_type_int(order)
    check_valid(pos)
    return check_type_int(solve_step(pos, strategy, order, output, first=True))
solve = check_type_function(solve)

def read_file(file):
    lines = check_type_list([check_type_function(check_type_object(line, ['strip']).strip)('\r\n') for line in check_type_function(check_type_object(file, ['splitlines']).splitlines)()])
    size = check_type_function(int)(lines[0])
    hex = check_type_object(check_type_object(Hex(check_type_int(size)), ['count', 'contains_pos', 'nodes_by_pos', 'get_by_pos', 'link_nodes', 'nodes_by_id', 'get_by_id', 'size']), ['count', 'contains_pos', 'nodes_by_pos', 'get_by_pos', 'link_nodes', 'get_by_id', 'nodes_by_id', 'size'])
    linei = 1
    tiles = (8 * [0])
    done = check_type_object(check_type_object(Done(check_type_int(hex.count)), ['cells', 'count', 'next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice']), ['cells', 'count', 'next_cell_max_neighbors', 'filter_tiles', 'MIN_CHOICE_STRATEGY', 'remove_all', 'next_cell_min_choice', 'FIRST_STRATEGY', '__getitem__', 'HIGHEST_VALUE_STRATEGY', 'next_cell', 'MAX_NEIGHBORS_STRATEGY', 'clone', 'next_cell_highest_value', 'set_done', 'next_cell_first', 'MIN_NEIGHBORS_STRATEGY', 'next_cell_min_neighbors', 'MAX_CHOICE_STRATEGY', 'remove', 'already_done', 'remove_unfixed', 'next_cell_max_choice'])
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
                check_type_function(print)(('Adding locked tile: %d at pos %d, %d, id=%d' % (inctile, x, y, check_type_int(check_type_object(check_type_function(hex.get_by_pos)(check_type_tuple((x, y), 2)), ['pos', 'id', 'links']).id))))
                check_type_function(done.set_done)(check_type_int(check_type_object(check_type_function(hex.get_by_pos)(check_type_tuple((x, y), 2)), ['pos', 'id', 'links']).id), check_type_int(inctile))
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
                check_type_function(print)(('Adding locked tile: %d at pos %d, %d, id=%d' % (inctile, x, ry, check_type_int(check_type_object(check_type_function(hex.get_by_pos)(check_type_tuple((x, ry), 2)), ['pos', 'id', 'links']).id))))
                check_type_function(done.set_done)(check_type_int(check_type_object(check_type_function(hex.get_by_pos)(check_type_tuple((x, ry), 2)), ['pos', 'id', 'links']).id), check_type_int(inctile))
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
    if (check_type_function(check_type_object(output, ['getvalue']).getvalue)() != expected):
        raise check_type_function(AssertionError)(('got a wrong answer:\n%s' % check_type_function(check_type_object(output, ['getvalue']).getvalue)()))
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
    parser = check_type_function(check_type_object(optparse, ['OptionParser']).OptionParser)(usage='%prog [options]', description='Test the performance of the hexiom2 benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check_type_object(parser, ['parse_args']).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check_type_object(options, ['num_runs']).num_runs, main)
