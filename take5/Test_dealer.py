import unittest
import constants_dealer_test as c
import constants_player_test as p

class TestDealer(unittest.TestCase):

    def test_create_deck(self):
        c.dealer1.create_deck(c.deck_size, c.min_range, c.max_range)
        self.assertEqual(104, len(c.dealer1.deck))

    def test_create_deck_error(self):
        with self.assertRaises(ValueError):
            c.dealer1.create_deck(c.deck_size, c.max_range, c.min_range)

    def test_hand(self):
        c.dealer1.hand()
        self.assertEqual(len(c.player0.cards), 10)
        self.assertEqual(len(c.player1.cards), 10)
        self.assertEqual(len(c.player2.cards), 10)

    def test_create_stacks(self):
        stacks = c.dealer1.create_stacks()
        self.assertEqual(len(stacks), 4)
        self.assertEquals(len(stacks[0]), 1)
        self.assertEquals(len(stacks[1]), 1)
        self.assertEquals(len(stacks[2]), 1)
        self.assertEquals(len(stacks[3]), 1)

    def test_is_over1(self):
        self.assertTrue(c.dealer2.is_over())

    def test_is_over0(self):
        self.assertFalse(c.dealer1.is_over())

    def test_output_scores(self):
        self.assertEqual([(0, 66), (1, 0), (2, 0)],
                         c.dealer2.output_scores())
        self.assertEqual([(0, 0), (1, 0), (2, 0)],
                         c.dealer1.output_scores())

    def test_simulate_round(self):
        c.dealer1.simulate_round(10, c.stack_size, c.deck_size, 1, .5)
        scores = c.dealer1.output_scores()
        self.assertEquals(scores, [(0, 25), (1, 21), (2, 43)])


    def test_simulate_game(self):
        scores = c.dealer3.simulate_game(10,
                                         c.stack_size,
                                         c.deck_size,
                                         None,
                                         1,
                                         .5)
        self.assertEquals(scores, [(0, 50), (1, 42), (2, 86)])



    def test_update_game_gt_0(self):
        (bull_points, new_stacks) = c.dealer1.update_game(p.player2, 3, p.stacks, p.stack_size)
        self.assertEqual(new_stacks, [p.stack1,
                                      p.stack2,
                                      p.stack3,
                                      [p.card7, p.card8, p.card12]])
        self.assertEqual(bull_points, 0)

    def test_update_game_gt_1(self):
        (bull_points, new_stacks) = c.dealer1.update_game(p.player2, 3, p.stacks1, p.stack_size)
        self.assertEqual(new_stacks, [p.stack1,
                                      p.stack2,
                                      p.stack3,
                                      [p.card11]])
        self.assertEqual(bull_points, 13)

    def test_update_game_lt(self):
        (bull_points, new_stacks) =  c.dealer1.update_game(p.player3, 0, p.stacks, p.stack_size)
        self.assertEqual(new_stacks, [[p.card1], p.stack2, p.stack3, p.stack4])
        self.assertEqual(bull_points, 5)

    def test_replace_card(self):
        new_stacks = c.dealer1.replace_card(p.card9, 2, p.stacks)
        self.assertEqual(new_stacks, [p.stack1, p.stack2, [p.card9], p.stack4])

    def test_sum_stacks(self):
        self.assertEqual(c.dealer1.sum_stacks(p.stacks), [5, 6, 6, 12])

    def test_add_card(self):
        new_stacks = c.dealer2.add_card(p.card9, 0, p.stacks)
        self.assertEqual(new_stacks, [[p.card1, p.card2, p.card9],
                                      p.stack2,
                                      p.stack3,
                                      p.stack4])

if __name__ == '__main__':
    unittest.main()

