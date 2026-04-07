import unittest

import ttbt


class TestTicTacToe(unittest.TestCase):
    def test_row_win(self):
        board = [
            ["x", "x", "x"],
            [" ", "o", " "],
            ["o", " ", " "],
        ]
        self.assertTrue(ttbt.is_win("x", board))
        self.assertFalse(ttbt.is_win("o", board))

    def test_column_win(self):
        board = [
            ["o", "x", " "],
            ["o", "x", " "],
            [" ", "x", " "],
        ]
        self.assertTrue(ttbt.is_win("x", board))

    def test_diagonal_win(self):
        board = [
            ["o", "x", "x"],
            [" ", "o", " "],
            ["x", " ", "o"],
        ]
        self.assertTrue(ttbt.is_win("o", board))

    def test_no_win(self):
        board = [
            ["x", "o", "x"],
            ["o", "x", "o"],
            ["o", "x", "o"],
        ]
        self.assertFalse(ttbt.is_win("x", board))
        self.assertFalse(ttbt.is_win("o", board))

    def test_tally_wins(self):
        self.assertEqual(ttbt.tally_wins([True, False, True, False]), 2)
        self.assertEqual(ttbt.tally_wins([]), 0)


if __name__ == "__main__":
    unittest.main()