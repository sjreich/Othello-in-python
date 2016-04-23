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


if __name__ == '__main__':
    unittest.main()
