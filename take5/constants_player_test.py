from player import Player

#params
stack_size = 5

card1 = (1, 2)
card2 = (2, 3)
card3 = (3, 2)
card4 = (4, 4)
card5 = (5, 3)
card6 = (6, 3)
card7 = (7, 7)
card8 = (8, 5)
card9 = (9, 2)
card10 = (10, 2)
card11 = (11, 3)
card12 = (12, 4)

cards1 = [card1, card2, card3]
cards2 = [card1, card11, card12]

player1 = Player(1, cards1)
player2 = Player(2, cards2)
player3 = Player(3, [card1])

stack1 = [card1, card2]
stack2 = [card3, card4]
stack3 = [card5, card6]
stack4 = [card7, card8]

stack5 = [card1, card2, card3, card4, card9]

stacks = [stack1, stack2, stack3, stack4]

stacks1 = [stack1, stack2, stack3, stack5]

top_cards = map(lambda stack: stack[-1], stacks)


