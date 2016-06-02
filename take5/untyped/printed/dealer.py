from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check10(val):
    try:
        val.discard
        return val
    except:
        raise CheckError(val)

def check11(val):
    try:
        val.cards
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.deck
        return val
    except:
        raise CheckError(val)

def check9(val):
    try:
        val.name
        return val
    except:
        raise CheckError(val)

def check12(val):
    try:
        val.replace_card
        return val
    except:
        raise CheckError(val)

def check4(val):
    try:
        val.create_stacks
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.create_deck
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.players
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.bull_points
        return val
    except:
        raise CheckError(val)

def check13(val):
    try:
        val.append
        return val
    except:
        raise CheckError(val)

def check6(val):
    try:
        val.update_game
        return val
    except:
        raise CheckError(val)

def check5(val):
    try:
        val.choose_correct_stack
        return val
    except:
        raise CheckError(val)

def check7(val):
    try:
        val.output_scores
        return val
    except:
        raise CheckError(val)

def check8(val):
    try:
        val.pop
        return val
    except:
        raise CheckError(val)
from random import randrange, shuffle, random, seed
from copy import deepcopy
from retic import List, Void, Tuple, Bool, Int, Float
from player import Player
min_val = 2
max_val = 7
turns = 10
stack_size = 5


class Dealer:

    def __init__(self, players, bull_points, cards_per_game):
        self.deck = check_type_function(check0(self).create_deck)(cards_per_game)
        self.players = players
        self.bull_points = bull_points
        self.cards_per_game = cards_per_game
    __init__ = check_type_function(__init__)

    def simulate_game(self):
        while (not (check_type_function(max)(check1(self).bull_points) >= 66)):
            for (i, player) in check_type_function(enumerate)(check2(self).players):
                check_type_tuple((i, player), 2)
                hand = []
                for i in check_type_function(range)(0, (i + (1 * 10))):
                    check_type_void(check_type_function(hand.append)(check3(self).deck[i]))
                player.cards = hand
            stacks = check_type_function(check4(self).create_stacks)()
            for i in check_type_function(range)(turns):
                for j in check_type_function(range)(check_type_function(len)(check2(self).players)):
                    player = check2(self).players[j]
                    chosen_stack_index = check_type_function(check5(player).choose_correct_stack)(stacks)
                    (p, s) = check_type_tuple(check_type_function(check6(self).update_game)(player, chosen_stack_index, stacks), 2)
                    check1(self).bull_points[j] = (check1(self).bull_points[j] + p)
                    stacks = s
        return check_type_function(check7(self).output_scores)()
    simulate_game = check_type_function(simulate_game)

    def create_deck(self, deck_size, bull_points=0.5, order=0.5):
        check_type_function(seed)(bull_points)
        cards = []
        for i in check_type_function(range)(deck_size):
            check_type_void(check_type_function(cards.append)(((i + 1), check_type_function(randrange)(min_val, max_val))))
        s = (order or check_type_function(random)())
        check_type_function(shuffle)(cards, (lambda : s))
        return cards
    create_deck = check_type_function(create_deck)

    def create_stacks(self):
        stacks = []
        for i in check_type_function(range)(4):
            check_type_void(check_type_function(stacks.append)([check_type_function(check8(check3(self).deck).pop)()]))
        return stacks
    create_stacks = check_type_function(create_stacks)

    def output_scores(self):
        res = []
        for i in check_type_function(range)(check_type_function(len)(check2(self).players)):
            player_points = check1(self).bull_points[i]
            player_name = check9(check2(self).players[i]).name
            check_type_void(check_type_function(res.append)((player_name, player_points)))
        return res
    output_scores = check_type_function(output_scores)

    def update_game(self, player, stack_index, stacks):
        top_cards = check_type_function(list)(check_type_function(map)((lambda stack: stack[(- 1)]), stacks))
        discarded_index = check_type_function(check10(player).discard)()
        discarded = check_type_function(check8(check11(player).cards).pop)(discarded_index)
        if (discarded[0] < check_type_function(min)(check_type_function(list)(check_type_function(map)((lambda card: card[0]), top_cards)))):
            bull_points = check_type_function(sum)(check_type_function(list)(check_type_function(map)((lambda card: card[1]), stacks[stack_index])))
            new_stacks = check_type_function(check12(self).replace_card)(discarded, stack_index, stacks)
            return (bull_points, new_stacks)
        else:
            my_stack = stacks[stack_index]
            if (check_type_function(len)(my_stack) == stack_size):
                bull_points = check_type_function(sum)(check_type_function(list)(check_type_function(map)((lambda card: card[1]), my_stack)))
                new_stacks = check_type_function(check12(self).replace_card)(discarded, stack_index, stacks)
                return (bull_points, new_stacks)
            else:
                new_stacks = check_type_function(deepcopy)(stacks)
                check_type_function(check13(new_stacks[stack_index]).append)(discarded)
                return (0, new_stacks)
    update_game = check_type_function(update_game)

    def replace_card(self, card, index, stacks):
        new_stacks = check_type_function(deepcopy)(stacks)
        new_stacks[index] = [card]
        return new_stacks
    replace_card = check_type_function(replace_card)
Dealer = check_type_class(Dealer, ['update_game', 'create_stacks', '__init__', 'replace_card', 'create_deck', 'simulate_game', 'output_scores'])
