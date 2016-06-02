import unittest
import constants_player_test as c

class TestPlayer(unittest.TestCase):

    def test_sum_stacks(self):
        self.assertEqual(c.player1.sum_stacks(c.stacks), [5, 6, 6, 12])

    def test_get_index_of_closest_stack(self):
        index = c.player1.get_index_of_closest_stack(c.top_cards, c.card9)
        self.assertEqual(index, 3)

    def test_choose_correct_stack(self):
        index = c.player1.choose_correct_stack(c.stacks1)
        self.assertEqual(index, 0)

    def test_discard(self):
        self.assertEqual(c.player1.discard(), 2)

    def test_pick_smallest_stack(self):
        index = c.player1.pick_smallest_stack(c.stacks)
        self.assertEquals(index, 0)

    def test_get_sum(self):
        bull_points = c.player1.get_sum(c.stack2)
        self.assertEqual(bull_points, 6)

    def test_take_hand(self):
        c.player3.take_hand(c.cards2)
        self.assertEqual(c.player3.cards, c.cards2)

if __name__ == '__main__':
    unittest.main()