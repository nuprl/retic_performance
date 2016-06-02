from random import randrange, shuffle, random, seed
from copy import deepcopy
from retic import List, Void, Tuple, Bool, Int, Float, String
from benchmark_tools.Timer import Timer

min_val = 2
max_val = 7
turns = 10
stack_size = 5

class Player:
    """
    To represent a player in the game
    """

    def __init__(self, name, cards):
        """
        :param name: Int
        :param cards: [Tuple...]
        :param strat: Function, to be called on face values of cards
        :return: Player
        """
        self.name = name
        self.cards = cards

    def discard(self):
        """
        Return index of card to be discarded
        :return: Int
        """
        face_values = list(map(lambda card: card[0], self.cards))
        discarded_index = face_values.index(max(face_values))
        return discarded_index

    def choose_correct_stack(self, stacks):
        """
        Returns the index of the correct stack
        :param stacks: [[Tuple ...]...]
        :return: Int
        """
        top_cards = list(map(lambda stack: stack[-1], stacks))
        discarded_index = self.discard()
        discarded = self.cards[discarded_index]
        if discarded[0] < min(list(map(lambda card: card[0], top_cards))):
            sums = []
            for stack in stacks:
                bull_points = list(map(lambda card: card[1], stack))
                sums.append(sum(bull_points))
            return sums.index(min(sums))
        else:
            return self.get_index_of_closest_stack(top_cards, discarded)

    def get_index_of_closest_stack(self, cards, card):
        """
        gets index of stack closest to card in value
        :param cards: [Tuple ...]
        :return: Int
        """
        diffs = []
        for c in cards:
            diff = abs(card[0] - c[0])
            diffs.append(diff)
        return diffs.index(min(diffs))


class Dealer:
    """
    To represent the Dealer for the whole game
    """

    def __init__(self, players, bull_points, cards_per_game):
        """
        :param deck: [Card ...]
        :param players: [Player ...]
        :param bull_points: [Int ...]
        """
        self.deck = self.create_deck(cards_per_game)
        self.players = players
        self.bull_points = bull_points
        self.cards_per_game = cards_per_game

    def simulate_game(self):
        """
        Similulates a game and returns the players' scores
        :return: [Tuple ...]
        """
        while not max(self.bull_points) >= 66:
            for i, player in enumerate(self.players):
                hand = []
                for i in range(0, i + 1 * 10):
                    hand.append(self.deck[i])
                player.cards = hand
            stacks = self.create_stacks()
            for i in range(turns):
                for j in range(len(self.players)):
                    player = self.players[j]
                    chosen_stack_index = player.choose_correct_stack(stacks)
                    p, s = self.update_game(player, chosen_stack_index, stacks)
                    self.bull_points[j] += p
                    stacks = s
        return self.output_scores()

    def create_deck(self, deck_size, bull_points=0.5, order=0.5):
        """
        :param deck_size: Int, number of cards in deck
        :param min: Int, minimum number of bull points
        :param max: Int, maximum number of bull points
        :param bull_points: float, bull points parametrization
        :param order: float, order of cards parametrization
        :return: [Card ...]
        """
        seed(bull_points)
        cards = []
        for i in range(deck_size):
            cards.append((i + 1, randrange(min_val, max_val)))
        s = order or random()
        shuffle(cards, lambda : s)
        return cards

    def create_stacks(self):
        """
        create 4 new stacks each having 1 card from the deck
        at the start of every round
        Initialize all players with that stack
        :return: [[Tuple] ...]
        """
        stacks = []
        for i in range(4):
            stacks.append([self.deck.pop()])
        return stacks

    def output_scores(self):
        """
        Outputs the names of the winning and losing players
        :param players: [Player ...]
        :return: (Player, Player)
        """
        res = []
        for i in range(len(self.players)):
            player_points = self.bull_points[i]
            player_name = self.players[i].name
            res.append((player_name, player_points))
        return res

    def update_game(self, player, stack_index, stacks):
        """
        update playe's bull points based on chosen stack
        :param stack_index: Int
        :param stacks: [[Tuple...]...] where len(stacks)=4
        :return: Tuple
        """
        top_cards = list(map(lambda stack: stack[-1], stacks))
        discarded_index = player.discard()
        discarded = player.cards.pop(discarded_index)
        if discarded[0] < min(list(map(lambda card: card[0], top_cards))):
            bull_points = sum(list(map(lambda card: card[1], stacks[
                stack_index])))
            new_stacks = self.replace_card(discarded, stack_index, stacks)
            return bull_points, new_stacks
        else:
            my_stack = stacks[stack_index]
            if len(my_stack) == stack_size:
                bull_points = sum(list(map(lambda card: card[1], my_stack)))
                new_stacks = self.replace_card(discarded, stack_index, stacks)
                return bull_points, new_stacks
            else:
                new_stacks = deepcopy(stacks)
                new_stacks[stack_index].append(discarded)
                return 0, new_stacks

    def replace_card(self, card, index, stacks):
        """
        Replaces stack with card and returns new stack
        :param card: Tuple
        :param index: Int
        :param stacks: [[Tuples ...] ...]
        :return [[Tuple...]...]
        """
        new_stacks = deepcopy(stacks)
        new_stacks[index] = [card]
        return new_stacks


def generate_dealer(players, cards_per_game):
    """
    Instantiates the dealer which will take over the game
    :return: Dealer
    """
    points = [(0) for i in range(len(players))]
    return Dealer(players, points, cards_per_game)

def generate_players(num_players):
    """
    instantiates n players with an empty list of cards
    :param num_players: int
    :return: [Players...]
    """
    players = []
    for i in range(num_players):
        players.append(Player(i, []))
    return players

def main():
    num = 3
    cards_per_player = 10
    cards_per_game = 210
    if num < 2:
        print('Too few players!')
    if cards_per_game / cards_per_player < num:
        print('Too many players!')
        exit()
    players = generate_players(num)
    dealer = generate_dealer(players, cards_per_game)
    dealer.simulate_game()
    #print('scores: %s' % dealer.simulate_game())
t = Timer()
with t:
    for i in range(1000):
        main()



