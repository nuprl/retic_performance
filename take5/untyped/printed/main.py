from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check1(val):
    try:
        val.discard
        val.get_index_of_closest_stack
        val.choose_correct_stack
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.simulate_game
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.update_game
        val.simulate_game
        val.create_stacks
        val.output_scores
        val.replace_card
        val.create_deck
        return val
    except:
        raise CheckError(val)
from retic import Void, List, Int
from benchmark_tools.Timer import Timer
from player import Player
from dealer import Dealer

def generate_dealer(players, cards_per_game):
    points = check_type_list([0 for i in check_type_function(range)(check_type_function(len)(players))])
    return check0(Dealer(players, points, cards_per_game))
generate_dealer = check_type_function(generate_dealer)

def generate_players(num_players):
    players = []
    for i in check_type_function(range)(num_players):
        check_type_void(check_type_function(players.append)(check1(Player(i, []))))
    return players
generate_players = check_type_function(generate_players)

def main():
    num = 3
    cards_per_player = 10
    cards_per_game = 210
    if (num < 2):
        check_type_function(print)('Too few players!')
    if ((cards_per_game / cards_per_player) < num):
        check_type_function(print)('Too many players!')
        check_type_function(exit)()
    players = generate_players(num)
    dealer = generate_dealer(players, cards_per_game)
    check_type_function(check2(dealer).simulate_game)()
main = check_type_function(main)
t = check_type_function(Timer)()
with t:
    for i in check_type_function(range)(1000):
        main()
