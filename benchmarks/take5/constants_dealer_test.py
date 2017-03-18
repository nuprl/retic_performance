from player import Player
from dealer import Dealer


#params
deck_size = 104
stack_size = 5
min_range = 2
max_range = 8
strat = max

player0 = Player(0, [])
player1 = Player(1, [])
player2 = Player(2, [])

dealer1 = Dealer([player0, player1, player2], [0, 0, 0])

dealer2 = Dealer([player0, player1, player2], [66, 0, 0])

dealer3 = Dealer([player0, player1, player2], [0, 0, 0])
