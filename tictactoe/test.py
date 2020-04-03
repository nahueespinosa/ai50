import unittest
from tictactoe import O, X, EMPTY, initial_state, player


class TestPlayer(unittest.TestCase):
    def test_board_empty(self):
        self.assertEqual(player(initial_state()), X)

    def test_board_alternate(self):
        board = initial_state()
        value = X

        # Fill the board testing the alternation of turns
        for row in board:
            for index in range(len(row)):
                row[index] = value
                value = X if value == O else O


if __name__ == '__main__':
    unittest.main()
