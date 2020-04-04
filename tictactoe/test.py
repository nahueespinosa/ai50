import unittest
from tictactoe import O, X, EMPTY, initial_state, player, actions, result, winner, minimax


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
        test_set = set(self.full_set)
        board = initial_state()
        value = X

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                board[i][j] = value
                value = X if value == O else O
                test_set.remove((i, j))
                self.assertEqual(actions(board), test_set)


class TestResult(unittest.TestCase):
    def test_result(self):
        board = initial_state()
        result_board = [[EMPTY, EMPTY, EMPTY],
                        [EMPTY,     X, EMPTY],
                        [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(result(board, (1, 1)), result_board)

        board = result_board
        result_board = [[EMPTY, EMPTY, EMPTY],
                        [EMPTY,     X,     O],
                        [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(result(board, (1, 2)), result_board)

    def test_result_raises(self):
        board = initial_state()
        board[1][1] = X
        with self.assertRaises(ValueError):
            result(board, (1, 1))


class TestWinner(unittest.TestCase):
    def test_winner_none(self):
        board = [[O, O, X],
                 [X, X, O],
                 [O, X, O]]

        self.assertEqual(winner(board), None)

    def test_winner_o(self):
        board = [[X, O, O],
                 [X, O, X],
                 [O, X, O]]

        self.assertEqual(winner(board), O)

    def test_winner_x(self):
        board = [[X, O, X],
                 [X, X, X],
                 [O, X, O]]

        self.assertEqual(winner(board), X)


class TestMinimax(unittest.TestCase):
    def test_minimax(self):
        # Based on page 281 of lecture0.pdf
        board = [[EMPTY, X, O],
                 [O, X, EMPTY],
                 [X, EMPTY, O]]

        self.assertEqual(minimax(board), (2, 1))


if __name__ == '__main__':
    unittest.main()
