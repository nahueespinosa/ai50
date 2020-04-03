import unittest
from tictactoe import O, X, EMPTY, initial_state, player, actions


class TestPlayer(unittest.TestCase):
    def test_board_empty(self):
        self.assertEqual(player(initial_state()), X)

    def test_board_alternate(self):
        board = initial_state()
        value = X

        # Fill the board testing the alternation of turns
        for row in board:
            for i, cell in enumerate(row):
                row[i] = value
                value = X if value == O else O


class TestActions(unittest.TestCase):
    full_set = set({(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)})

    def test_actions_empty(self):
        self.assertEqual(actions(initial_state()), self.full_set)

    def test_actions_alternate(self):
        result = set(self.full_set)
        board = initial_state()
        value = X

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                board[i][j] = value
                value = X if value == O else O
                result.remove((i, j))
                self.assertEqual(actions(board), result)


if __name__ == '__main__':
    unittest.main()
