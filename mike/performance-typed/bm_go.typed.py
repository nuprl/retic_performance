from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check3(val):
    try:
        val.neighbours
        return val
    except:
        raise CheckError(val)

def check4(val):
    try:
        val.append
        return val
    except:
        raise CheckError(val)

def check11(val):
    try:
        val.find
        return val
    except:
        raise CheckError(val)

def check25(val):
    try:
        val.set_neighbours
        return val
    except:
        raise CheckError(val)

def check21(val):
    try:
        val.hash
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.pos
        return val
    except:
        raise CheckError(val)

def check16(val):
    try:
        val.removestamp
        return val
    except:
        raise CheckError(val)

def check20(val):
    try:
        val.random
        return val
    except:
        raise CheckError(val)

def check46(val):
    try:
        val.seed
        return val
    except:
        raise CheckError(val)

def check31(val):
    try:
        val.pos_child
        return val
    except:
        raise CheckError(val)

def check22(val):
    try:
        val.hash_set
        return val
    except:
        raise CheckError(val)

def check28(val):
    try:
        val.copy
        return val
    except:
        raise CheckError(val)

def check39(val):
    try:
        val.sqrt
        return val
    except:
        raise CheckError(val)

def check43(val):
    try:
        val.split
        return val
    except:
        raise CheckError(val)

def check19(val):
    try:
        val.empty_pos
        val.add
        val.board
        val.remove
        val.set
        val.random_choice
        val.empties
        return val
    except:
        raise CheckError(val)

def check14(val):
    try:
        val.add
        return val
    except:
        raise CheckError(val)

def check34(val):
    try:
        val.bestchild
        return val
    except:
        raise CheckError(val)

def check44(val):
    try:
        val.random_move
        val.useful_moves
        val.history
        return val
    except:
        raise CheckError(val)

def check7(val):
    try:
        val.zobrist
        return val
    except:
        raise CheckError(val)

def check29(val):
    try:
        val.losses
        val.wins
        val.pos
        val.score
        val.select
        val.best_visited
        val.best_child
        val.update_path
        val.random_playout
        val.play
        return val
    except:
        raise CheckError(val)

def check48(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check13(val):
    try:
        val.remove
        return val
    except:
        raise CheckError(val)

def check36(val):
    try:
        val.best_child
        return val
    except:
        raise CheckError(val)

def check35(val):
    try:
        val.parent
        return val
    except:
        raise CheckError(val)

def check27(val):
    try:
        val.temp_ledges
        return val
    except:
        raise CheckError(val)

def check32(val):
    try:
        val.unexplored
        return val
    except:
        raise CheckError(val)

def check24(val):
    try:
        val.hash
        val.update
        val.add
        val.dupe
        return val
    except:
        raise CheckError(val)

def check37(val):
    try:
        val.wins
        return val
    except:
        raise CheckError(val)

def check26(val):
    try:
        val.timestamp
        return val
    except:
        raise CheckError(val)

def check12(val):
    try:
        val.reference
        return val
    except:
        raise CheckError(val)

def check33(val):
    try:
        val.pop
        return val
    except:
        raise CheckError(val)

def check17(val):
    try:
        val.move
        val.find
        val.timestamp
        val.__repr__
        val.used
        val.remove
        val.reference
        val.pos
        val.set_neighbours
        val.removestamp
        val.board
        val.zobrist_strings
        val.color
        val.ledges
        val.neighbours
        return val
    except:
        raise CheckError(val)

def check18(val):
    try:
        val.useful
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.zobrist
        val.finished
        val.__repr__
        val.black_dead
        val.useful_fast
        val.emptyset
        val.lastmove
        val.squares
        val.color
        val.check
        val.random_move
        val.move
        val.useful_moves
        val.history
        val.white_dead
        val.score
        val.useful
        val.replay
        val.reset
        return val
    except:
        raise CheckError(val)

def check15(val):
    try:
        val.emptyset
        return val
    except:
        raise CheckError(val)

def check8(val):
    try:
        val.update
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.randrange
        return val
    except:
        raise CheckError(val)

def check5(val):
    try:
        val.board
        return val
    except:
        raise CheckError(val)

def check42(val):
    try:
        val.strip
        return val
    except:
        raise CheckError(val)

def check47(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)

def check10(val):
    try:
        val.ledges
        return val
    except:
        raise CheckError(val)

def check23(val):
    try:
        val.clear
        return val
    except:
        raise CheckError(val)

def check49(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check30(val):
    try:
        val.select
        return val
    except:
        raise CheckError(val)

def check6(val):
    try:
        val.squares
        return val
    except:
        raise CheckError(val)

def check41(val):
    try:
        val.score
        return val
    except:
        raise CheckError(val)

def check38(val):
    try:
        val.losses
        return val
    except:
        raise CheckError(val)

def check9(val):
    try:
        val.color
        return val
    except:
        raise CheckError(val)

def check45(val):
    try:
        val.play
        return val
    except:
        raise CheckError(val)

def check40(val):
    try:
        val.log
        return val
    except:
        raise CheckError(val)
import random, math, sys, time
SIZE = 9
GAMES = 200
KOMI = 7.5
(EMPTY, WHITE, BLACK) = (0, 1, 2)
SHOW = check_type_dict({EMPTY: '.', WHITE: 'o', BLACK: 'x', })
PASS = (- 1)
MAXMOVES = ((SIZE * SIZE) * 3)
TIMESTAMP = 0
MOVES = 0

def to_pos(x, y):
    check_type_int(x)
    check_type_int(y)
    return ((y * SIZE) + x)
to_pos = check_type_function(to_pos)

def to_xy(pos):
    check_type_int(pos)
    (y, x) = check_type_tuple(check_type_function(divmod)(pos, SIZE), 2)
    return check_type_tuple((x, y), 2)
to_xy = check_type_function(to_xy)


class Square:

    def __init__(self, board, pos):
        check0(board)
        check_type_int(pos)
        self.board = board
        self.pos = pos
        self.timestamp = TIMESTAMP
        self.removestamp = TIMESTAMP
        self.zobrist_strings = check_type_list([check_type_function(check1(random).randrange)(9223372036854775807) for i in check_type_function(range)(3)])
        self.color = 0
        self.reference = self
        self.ledges = 0
        self.used = False
        self.neighbours = []
    __init__ = check_type_function(__init__)

    def set_neighbours(self):
        (x, y) = ((check2(self).pos % SIZE), (check2(self).pos // SIZE))
        self.neighbours = []
        for (dx, dy) in [((- 1), 0), (1, 0), (0, (- 1)), (0, 1)]:
            check_type_tuple((dx, dy), 2)
            (newx, newy) = ((x + dx), (y + dy))
            if ((0 <= newx < SIZE) and (0 <= newy < SIZE)):
                check_type_function(check4(check3(self).neighbours).append)(check6(check5(self).board).squares[check_type_int(to_pos(check_type_int(newx), check_type_int(newy)))])
    set_neighbours = check_type_function(set_neighbours)

    def move(self, color):
        check_type_int(color)
        global TIMESTAMP, MOVES
        TIMESTAMP = (TIMESTAMP + 1)
        MOVES = (MOVES + 1)
        check_type_function(check8(check7(check5(self).board).zobrist).update)(self, color)
        self.color = color
        self.reference = self
        self.ledges = 0
        self.used = True
        for neighbour in check3(self).neighbours:
            neighcolor = check9(neighbour).color
            if (neighcolor == EMPTY):
                self.ledges = (check10(self).ledges + 1)
            else:
                neighbour_ref = check_type_function(check11(neighbour).find)(update=True)
                if (neighcolor == color):
                    if (check2(check12(neighbour_ref).reference).pos != check2(self).pos):
                        self.ledges = (check10(self).ledges + check10(neighbour_ref).ledges)
                        neighbour_ref.reference = self
                    self.ledges = (check10(self).ledges - 1)
                else:
                    neighbour_ref.ledges = (check10(neighbour_ref).ledges - 1)
                    if (check10(neighbour_ref).ledges == 0):
                        check_type_function(check13(neighbour).remove)(neighbour_ref)
        check_type_function(check14(check7(check5(self).board).zobrist).add)()
    move = check_type_function(move)

    def remove(self, reference, update=True):
        check_type_function(check8(check7(check5(self).board).zobrist).update)(self, EMPTY)
        self.removestamp = TIMESTAMP
        if update:
            self.color = EMPTY
            check_type_function(check14(check15(check5(self).board).emptyset).add)(check2(self).pos)
        for neighbour in check3(self).neighbours:
            if ((check9(neighbour).color != EMPTY) and (check16(neighbour).removestamp != TIMESTAMP)):
                neighbour_ref = check_type_function(check11(neighbour).find)(update)
                if (check2(neighbour_ref).pos == check2(reference).pos):
                    check_type_function(check13(neighbour).remove)(reference, update)
                elif update:
                    neighbour_ref.ledges = (check10(neighbour_ref).ledges + 1)
    remove = check_type_function(remove)

    def find(self, update=False):
        reference = check12(self).reference
        if (check2(reference).pos != check2(self).pos):
            reference = check_type_function(check11(reference).find)(update)
            if update:
                self.reference = reference
        return check17(reference)
    find = check_type_function(find)

    def __repr__(self):
        return check_type_function(repr)(check_type_tuple(to_xy(check_type_int(check2(self).pos)), 2))
    __repr__ = check_type_function(__repr__)
Square = check_type_class(Square, ['set_neighbours', 'move', 'find', '__repr__', '__init__', 'remove'])


class EmptySet:

    def __init__(self, board):
        check18(board)
        self.board = board
        self.empties = check_type_function(list)(check_type_function(range)((SIZE * SIZE)))
        self.empty_pos = check_type_function(list)(check_type_function(range)((SIZE * SIZE)))
    __init__ = check_type_function(__init__)

    def random_choice(self):
        check19(self)
        choices = check_type_function(len)(check_type_list(self.empties))
        while choices:
            i = check_type_function(int)((check_type_function(check20(random).random)() * choices))
            pos = check_type_int(check_type_list(self.empties)[check_type_int(i)])
            if check_type_int(check_type_function(check18(self.board).useful)(pos)):
                return pos
            choices = (choices - 1)
            check_type_function(self.set)(check_type_int(i), check_type_int(check_type_list(self.empties)[check_type_int(choices)]))
            check_type_function(self.set)(check_type_int(choices), pos)
        return PASS
    random_choice = check_type_function(random_choice)

    def add(self, pos):
        check19(self)
        check_type_int(pos)
        check_type_list(self.empty_pos)[pos] = check_type_int(check_type_function(len)(check_type_list(self.empties)))
        check_type_void(check_type_function(check_type_list(self.empties).append)(pos))
    add = check_type_function(add)

    def remove(self, pos):
        check19(self)
        check_type_int(pos)
        check_type_function(self.set)(check_type_int(check_type_list(self.empty_pos)[pos]), check_type_int(check_type_list(self.empties)[check_type_int((check_type_function(len)(check_type_list(self.empties)) - 1))]))
        check_type_int(check_type_function(check_type_list(self.empties).pop)())
    remove = check_type_function(remove)

    def set(self, i, pos):
        check19(self)
        check_type_int(i)
        check_type_int(pos)
        check_type_list(self.empties)[i] = pos
        check_type_list(self.empty_pos)[pos] = i
    set = check_type_function(set)
EmptySet = check_type_class(EmptySet, ['remove', 'set', 'add', 'random_choice', '__init__'])


class ZobristHash:

    def __init__(self, board):
        check6(board)
        self.hash_set = check_type_function(set)()
        self.hash = 0
        for square in check_type_list(check_type_list(board.squares)):
            check17(square)
            self.hash = (check21(self).hash ^ check_type_int(check_type_list(square.zobrist_strings)[EMPTY]))
        check_type_function(check23(check22(self).hash_set).clear)()
        check_type_function(check14(check22(self).hash_set).add)(check21(self).hash)
    __init__ = check_type_function(__init__)

    def update(self, square, color):
        check24(self)
        check17(square)
        check_type_int(color)
        self.hash = (check_type_int(self.hash) ^ check_type_int(check_type_list(square.zobrist_strings)[check_type_int(square.color)]))
        self.hash = (check_type_int(self.hash) ^ check_type_int(check_type_list(square.zobrist_strings)[color]))
    update = check_type_function(update)

    def add(self):
        check24(self)
        check_type_function(check14(check22(self).hash_set).add)(check_type_int(self.hash))
    add = check_type_function(add)

    def dupe(self):
        check24(self)
        return (check_type_int(self.hash) in check22(self).hash_set)
    dupe = check_type_function(dupe)
ZobristHash = check_type_class(ZobristHash, ['update', 'add', 'dupe', '__init__'])


class Board:

    def __init__(self):
        self.squares = []
        self.emptyset = check19(EmptySet(check18(self)))
        self.zobrist = check24(ZobristHash(check6(self)))
        self.color = BLACK
        self.finished = False
        self.lastmove = (- 2)
        self.history = []
        self.white_dead = 0
        self.black_dead = 0
        self.squares = check_type_list([check17(Square(check0(self), check_type_int(pos))) for pos in check_type_function(range)((SIZE * SIZE))])
        for square in check6(self).squares:
            check_type_function(check25(square).set_neighbours)()
            square.color = EMPTY
            square.used = False
    __init__ = check_type_function(__init__)

    def reset(self):
        for square in check6(self).squares:
            square.color = EMPTY
            square.used = False
        self.emptyset = check19(EmptySet(check18(self)))
        self.zobrist = check24(ZobristHash(check6(self)))
        self.color = BLACK
        self.finished = False
        self.lastmove = (- 2)
        self.history = []
        self.white_dead = 0
        self.black_dead = 0
    reset = check_type_function(reset)

    def move(self, pos):
        check0(self)
        check_type_int(pos)
        square = check17(check17(check_type_list(self.squares)[pos]))
        if (pos != PASS):
            check_type_function(square.move)(check_type_int(self.color))
            check_type_function(check19(self.emptyset).remove)(check_type_int(square.pos))
        elif (check_type_int(self.lastmove) == PASS):
            self.finished = True
        if (check_type_int(self.color) == BLACK):
            self.color = WHITE
        else:
            self.color = BLACK
        self.lastmove = pos
        check_type_void(check_type_function(check_type_list(self.history).append)(pos))
    move = check_type_function(move)

    def random_move(self):
        check0(self)
        return check_type_int(check_type_function(check19(self.emptyset).random_choice)())
    random_move = check_type_function(random_move)

    def useful_fast(self, square):
        check0(self)
        check17(square)
        if (not check_type_bool(square.used)):
            for neighbour in check_type_list(check_type_list(square.neighbours)):
                check17(neighbour)
                if (check_type_int(neighbour.color) == EMPTY):
                    return True
        return False
    useful_fast = check_type_function(useful_fast)

    def useful(self, pos):
        check0(self)
        check_type_int(pos)
        global TIMESTAMP
        TIMESTAMP = (TIMESTAMP + 1)
        square = check17(check17(check_type_list(self.squares)[pos]))
        if check_type_bool(check_type_function(self.useful_fast)(check17(square))):
            return True
        old_hash = check_type_int(check24(self.zobrist).hash)
        check_type_function(check24(self.zobrist).update)(check17(square), check_type_int(self.color))
        empties = opps = weak_opps = neighs = weak_neighs = 0
        for neighbour in check_type_list(check_type_list(square.neighbours)):
            neighcolor = check9(neighbour).color
            if (neighcolor == EMPTY):
                empties = (empties + 1)
                continue
            neighbour_ref = check_type_function(check11(neighbour).find)()
            if (check26(neighbour_ref).timestamp != TIMESTAMP):
                if (neighcolor == check_type_int(self.color)):
                    neighs = (neighs + 1)
                else:
                    opps = (opps + 1)
                neighbour_ref.timestamp = TIMESTAMP
                neighbour_ref.temp_ledges = check10(neighbour_ref).ledges
            neighbour_ref.temp_ledges = (check27(neighbour_ref).temp_ledges - 1)
            if (check27(neighbour_ref).temp_ledges == 0):
                if (neighcolor == check_type_int(self.color)):
                    weak_neighs = (weak_neighs + 1)
                else:
                    weak_opps = (weak_opps + 1)
                    check_type_function(check13(neighbour_ref).remove)(neighbour_ref, update=False)
        dupe = check_type_bool(check_type_function(check24(self.zobrist).dupe)())
        check24(self.zobrist).hash = old_hash
        strong_neighs = (neighs - weak_neighs)
        strong_opps = (opps - weak_opps)
        return check_type_int(((not dupe) and (empties or weak_opps or (strong_neighs and (strong_opps or weak_neighs)))))
    useful = check_type_function(useful)

    def useful_moves(self):
        check0(self)
        return check_type_list([pos for pos in check_type_list(check19(self.emptyset).empties) if check_type_int(check_type_function(self.useful)(check_type_int(pos)))])
    useful_moves = check_type_function(useful_moves)

    def replay(self, history):
        check0(self)
        check_type_list(history)
        for pos in history:
            check_type_int(pos)
            check_type_function(self.move)(pos)
    replay = check_type_function(replay)

    def score(self, color):
        check0(self)
        check_type_int(color)
        if (color == WHITE):
            count = (KOMI + check_type_int(self.black_dead))
        else:
            count = check_type_int(self.white_dead)
        for square in check_type_list(check_type_list(self.squares)):
            check17(square)
            squarecolor = check_type_int(square.color)
            if (squarecolor == color):
                count = (count + 1)
            elif (squarecolor == EMPTY):
                surround = 0
                for neighbour in check_type_list(check_type_list(square.neighbours)):
                    if (check9(neighbour).color == color):
                        surround = (surround + 1)
                if (surround == check_type_function(len)(check_type_list(square.neighbours))):
                    count = (count + 1)
        return check_type_float(count)
    score = check_type_function(score)

    def check(self):
        check0(self)
        for square in check_type_list(check_type_list(self.squares)):
            check17(square)
            if (check_type_int(square.color) == EMPTY):
                continue
            members1 = check_type_function(set)([square])
            changed = True
            while changed:
                changed = False
                for member in check_type_function(check28(members1).copy)():
                    for neighbour in check3(member).neighbours:
                        if ((check9(neighbour).color == check_type_int(square.color)) and (neighbour not in members1)):
                            changed = True
                            check_type_function(check14(members1).add)(neighbour)
            ledges1 = 0
            for member in members1:
                for neighbour in check3(member).neighbours:
                    if (check9(neighbour).color == EMPTY):
                        ledges1 = (ledges1 + 1)
            root = check17(check_type_function(square.find)())
            members2 = check_type_function(set)()
            for square2 in check_type_list(check_type_list(self.squares)):
                check17(square2)
                if ((check_type_int(square2.color) != EMPTY) and (check17(check_type_function(square2.find)()) == root)):
                    check_type_function(check14(members2).add)(square2)
            ledges2 = check10(root).ledges
            assert (members1 == members2)
            assert (ledges1 == ledges2), ('ledges differ at %r: %d %d' % (square, ledges1, ledges2))
            empties1 = check_type_function(set)(check_type_list(check19(self.emptyset).empties))
            empties2 = check_type_function(set)()
            for square in check_type_list(check_type_list(self.squares)):
                check17(square)
                if (check_type_int(square.color) == EMPTY):
                    check_type_function(check14(empties2).add)(check_type_int(square.pos))
    check = check_type_function(check)

    def __repr__(self):
        check0(self)
        result = []
        for y in check_type_function(range)(SIZE):
            start = check_type_int(to_pos(0, check_type_int(y)))
            check_type_void(check_type_function(result.append)(check_type_function(''.join)(check_type_list([(check_type_string(SHOW[check_type_int(square.color)]) + ' ') for square in check_type_list(check_type_list(self.squares)[start:(start + SIZE)])]))))
        return check_type_function('\n'.join)(result)
    __repr__ = check_type_function(__repr__)
Board = check_type_class(Board, ['random_move', 'move', '__repr__', 'useful_moves', '__init__', 'useful_fast', 'score', 'useful', 'replay', 'reset', 'check'])


class UCTNode:

    def __init__(self):
        self.bestchild = None
        self.pos = (- 1)
        self.wins = 0
        self.losses = 0
        self.pos_child = check_type_list([None for x in check_type_function(range)((SIZE * SIZE))])
        self.parent = None
    __init__ = check_type_function(__init__)

    def play(self, board):
        check29(self)
        check0(board)
        color = check_type_int(board.color)
        node = self
        path = [node]
        while True:
            pos = check_type_function(check30(node).select)(board)
            if (pos == PASS):
                break
            check_type_function(board.move)(check_type_int(pos))
            child = check31(node).pos_child[pos]
            if (not child):
                child = check31(node).pos_child[pos] = check29(UCTNode())
                child.unexplored = check_type_list(check_type_function(board.useful_moves)())
                child.pos = pos
                child.parent = node
                check_type_void(check_type_function(path.append)(child))
                break
            check_type_void(check_type_function(path.append)(child))
            node = child
        check_type_function(self.random_playout)(board)
        check_type_function(self.update_path)(board, color, check_type_list(path))
    play = check_type_function(play)

    def select(self, board):
        check29(self)
        check0(board)
        if check32(self).unexplored:
            i = check_type_function(check1(random).randrange)(check_type_function(len)(check32(self).unexplored))
            pos = check32(self).unexplored[i]
            check32(self).unexplored[i] = check32(self).unexplored[(check_type_function(len)(check32(self).unexplored) - 1)]
            check_type_function(check33(check32(self).unexplored).pop)()
            return check_type_int(pos)
        elif check34(self).bestchild:
            return check_type_int(check2(check34(self).bestchild).pos)
        else:
            return PASS
    select = check_type_function(select)

    def random_playout(self, board):
        check29(self)
        check0(board)
        for x in check_type_function(range)(MAXMOVES):
            if check_type_bool(board.finished):
                break
            check_type_function(board.move)(check_type_int(check_type_function(board.random_move)()))
    random_playout = check_type_function(random_playout)

    def update_path(self, board, color, path):
        check29(self)
        check0(board)
        check_type_int(color)
        check_type_list(path)
        wins = (check_type_float(check_type_function(board.score)(BLACK)) >= check_type_float(check_type_function(board.score)(WHITE)))
        for node in check_type_list(path):
            check29(node)
            if (color == BLACK):
                color = WHITE
            else:
                color = BLACK
            if (wins == (color == BLACK)):
                node.wins = (check_type_int(node.wins) + 1)
            else:
                node.losses = (check_type_int(node.losses) + 1)
            if check35(node).parent:
                check35(node).parent.bestchild = check_type_function(check36(check35(node).parent).best_child)()
    update_path = check_type_function(update_path)

    def score(self):
        check29(self)
        winrate = (check_type_int(self.wins) / check_type_function(float)((check_type_int(self.wins) + check_type_int(self.losses))))
        parentvisits = (check37(check35(self).parent).wins + check38(check35(self).parent).losses)
        if (not parentvisits):
            return check_type_float(winrate)
        nodevisits = (check_type_int(self.wins) + check_type_int(self.losses))
        return check_type_float((winrate + check_type_function(check39(math).sqrt)((check_type_function(check40(math).log)(parentvisits) / (5 * nodevisits)))))
    score = check_type_function(score)

    def best_child(self):
        check29(self)
        maxscore = (- 1)
        maxchild = None
        for child in check31(self).pos_child:
            if (child and (check_type_function(check41(child).score)() > maxscore)):
                maxchild = child
                maxscore = check_type_function(check41(child).score)()
        return check29(maxchild)
    best_child = check_type_function(best_child)

    def best_visited(self):
        check29(self)
        maxvisits = (- 1)
        maxchild = None
        for child in check31(self).pos_child:
            if (child and ((check37(child).wins + check38(child).losses) > maxvisits)):
                (maxvisits, maxchild) = ((check37(child).wins + check38(child).losses), child)
        return check29(maxchild)
    best_visited = check_type_function(best_visited)
UCTNode = check_type_class(UCTNode, ['__init__', 'select', 'score', 'best_visited', 'best_child', 'update_path', 'random_playout', 'play'])

def user_move(board):
    check0(board)
    while True:
        text = check_type_function(check42(check_type_function(raw_input)('?')).strip)()
        if (text == 'p'):
            return PASS
        if (text == 'q'):
            raise EOFError
        try:
            (x, y) = check_type_tuple(check_type_list([check_type_function(int)(i) for i in check_type_function(check43(text).split)()]), 2)
        except ValueError:
            continue
        if (not ((0 <= x < SIZE) and (0 <= y < SIZE))):
            continue
        pos = check_type_int(to_pos(check_type_int(x), check_type_int(y)))
        if check_type_int(check_type_function(board.useful)(pos)):
            return pos
    return (- 1)
user_move = check_type_function(user_move)

def computer_move(board):
    check44(board)
    global MOVES
    pos = check_type_int(check_type_function(board.random_move)())
    if (pos == PASS):
        return PASS
    tree = check29(check29(UCTNode()))
    tree.unexplored = check_type_list(check_type_function(board.useful_moves)())
    nboard = check0(check0(Board()))
    for game in check_type_function(range)(GAMES):
        node = tree
        check_type_function(nboard.reset)()
        check_type_function(nboard.replay)(check_type_list(board.history))
        check_type_function(check45(node).play)(nboard)
    return check_type_int(check29(check_type_function(tree.best_visited)()).pos)
computer_move = check_type_function(computer_move)

def versus_cpu():
    check_type_function(check46(random).seed)(1)
    board = check0(check0(Board()))
    pos = check_type_int(computer_move(check44(board)))
versus_cpu = check_type_function(versus_cpu)

def main(n, timer):
    check_type_int(n)
    times = []
    for i in check_type_function(range)(5):
        versus_cpu()
    for i in check_type_function(range)(n):
        t1 = check_type_function(timer)()
        versus_cpu()
        t2 = check_type_function(timer)()
        check_type_void(check_type_function(times.append)((t2 - t1)))
    return times
main = check_type_function(main)
if (__name__ == '__main__'):
    import util, optparse
    parser = check_type_function(check47(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of the Go benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check48(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check49(options).num_runs, main)
