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

    def test_update_with_move_flip(self):
        game = Game(4)
        initial_state =  [['.','.','.','.'],
                          ['.','.','O','.'],
                          ['.','.','X','.'],
                          ['.','.','.','.']]
        game.state = initial_state
        game.update_for_move(0, 2)
        expected_state = [['.','.','X','.'],
                          ['.','.','X','.'],
                          ['.','.','X','.'],
                          ['.','.','.','.']]                   
        self.assertEqual(game.state, expected_state)


    def test_update_with_move_next_to_same_color(self):
        game = Game(4)
        initial_state =  [['.','.','.','.'],
                          ['.','.','X','.'],
                          ['.','.','O','.'],
                          ['.','.','O','.']]
        game.state = initial_state
        game.update_for_move(0, 2)
        expected_state = [['.','.','.','.'],
                          ['.','.','X','.'],
                          ['.','.','O','.'],
                          ['.','.','O','.']]
        self.assertEqual(game.state, expected_state)

    def test_update_with_move_runs_into_edge(self):
        game = Game(4)
        initial_state =  [['.','.','.','.'],
                          ['.','.','O','.'],
                          ['.','.','O','.'],
                          ['.','.','O','.']]
        game.state = initial_state
        game.update_for_move(0, 2)
        expected_state = [['.','.','.','.'],
                          ['.','.','O','.'],
                          ['.','.','O','.'],
                          ['.','.','O','.']]
        self.assertEqual(game.state, expected_state)

    def test_move_out_of_bounds(self):
        game = Game(4)
        in_bounds_moves = [[2,2], [0,3], [3,0]]
        for move in in_bounds_moves:
            self.assertFalse(game.move_out_of_bounds(move[0], move[1]))

        out_of_bounds_moves = [[2,4], [4,2], [-1,1], [1,-1]]
        for move in out_of_bounds_moves:
            self.assertTrue(game.move_out_of_bounds(move[0], move[1]))

    def test_move_spot_empty(self):
        game = Game(4)
        free_spaces = [[0,0], [0,1], [1,0], [3,3]]
        for move in free_spaces:
            self.assertTrue(game.move_spot_empty(move[0], move[1]))

        taken_spaces = [[1,1], [1,2], [2,1], [1,1]]
        for move in taken_spaces:
            self.assertFalse(game.move_spot_empty(move[0], move[1]))


if __name__ == '__main__':
    unittest.main()
