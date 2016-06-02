from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check0(val):
    try:
        val.cards
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.discard
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.index
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.get_index_of_closest_stack
        return val
    except:
        raise CheckError(val)
from retic import List, Tuple, Void, String, Int


class Player:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
    __init__ = check_type_function(__init__)

    def discard(self):
        face_values = check_type_function(list)(check_type_function(map)((lambda card: card[0]), check0(self).cards))
        discarded_index = check_type_function(check1(face_values).index)(check_type_function(max)(face_values))
        return discarded_index
    discard = check_type_function(discard)

    def choose_correct_stack(self, stacks):
        top_cards = check_type_function(list)(check_type_function(map)((lambda stack: stack[(- 1)]), stacks))
        discarded_index = check_type_function(check2(self).discard)()
        discarded = check0(self).cards[discarded_index]
        if (discarded[0] < check_type_function(min)(check_type_function(list)(check_type_function(map)((lambda card: card[0]), top_cards)))):
            sums = []
            for stack in stacks:
                bull_points = check_type_function(list)(check_type_function(map)((lambda card: card[1]), stack))
                check_type_void(check_type_function(sums.append)(check_type_function(sum)(bull_points)))
            return check_type_int(check_type_function(sums.index)(check_type_function(min)(sums)))
        else:
            return check_type_function(check3(self).get_index_of_closest_stack)(top_cards, discarded)
    choose_correct_stack = check_type_function(choose_correct_stack)

    def get_index_of_closest_stack(self, cards, card):
        diffs = []
        for c in cards:
            diff = check_type_function(abs)((card[0] - c[0]))
            check_type_void(check_type_function(diffs.append)(diff))
        return check_type_int(check_type_function(diffs.index)(check_type_function(min)(diffs)))
    get_index_of_closest_stack = check_type_function(get_index_of_closest_stack)
Player = check_type_class(Player, ['choose_correct_stack', 'discard', 'get_index_of_closest_stack', '__init__'])
