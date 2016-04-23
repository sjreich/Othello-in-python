import unittest
from game import Game

class GameTest(unittest.TestCase):
    def test_successful_game_initialization(self):
        game = Game(4)
        expected_state =  [['.','.','.','.'],
                           ['.','X','O','.'],
                           ['.','O','X','.'],
                           ['.','.','.','.']]
        self.assertEqual(game.state, expected_state)

    def test_game_with_odd_rowed_board(self):
        with self.assertRaises(ValueError) as context:
            Game(5)

        self.assertTrue('Number of rows must be even' in context.exception)

    def test_move_in_bounds(self):
        game = Game(4)
        in_bounds_moves = [[2,2], [0,3], [3,0]]
        for move in in_bounds_moves:
            self.assertTrue(game.move_in_bounds(move))

        out_of_bounds_moves = [[2,4], [4,2], [-1,1], [1,-1]]
        for move in out_of_bounds_moves:
            self.assertFalse(game.move_in_bounds(move))

    def test_move_free_spot(self):
        game = Game(4)
        free_spaces = [[0,0], [0,1], [1,0], [3,3]]
        for move in free_spaces:
            self.assertTrue(game.move_free_spot(move))

        taken_spaces = [[1,1], [1,2], [2,1], [1,1]]
        for move in taken_spaces:
            self.assertFalse(game.move_free_spot(move))


if __name__ == '__main__':
    unittest.main()
