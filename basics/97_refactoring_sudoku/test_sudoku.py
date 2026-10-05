import unittest
from copy import deepcopy
import sudoku_after 

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        # An easy sudoku puzzle with ONE solution
        self.puzzle = [
            [5, 1, 7, 6, 0, 0, 0, 3, 4],
            [2, 8, 9, 0, 0, 4, 0, 0, 0],
            [3, 4, 6, 2, 0, 5, 0, 9, 0],
            [6, 0, 2, 0, 0, 0, 0, 1, 0],
            [0, 3, 8, 0, 0, 6, 0, 4, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 7, 8],
            [7, 0, 3, 4, 0, 0, 5, 6, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        # The (expected) solution to the above puzzle:
        self.solution = [
            [5, 1, 7, 6, 9, 8, 2, 3, 4],
            [2, 8, 9, 1, 3, 4, 7, 5, 6],
            [3, 4, 6, 2, 7, 5, 8, 9, 1],
            [6, 7, 2, 8, 4, 9, 3, 1, 5],
            [1, 3, 8, 5, 2, 6, 9, 4, 7],
            [9, 5, 4, 7, 1, 3, 6, 8, 2],
            [4, 9, 5, 3, 6, 2, 1, 7, 8],
            [7, 2, 3, 4, 8, 1, 5, 6, 9],
            [8, 6, 1, 9, 5, 7, 4, 2, 3],
        ]

    def test_find_empty(self):
        # There is at least one empty in initial puzzle
        row, col = sudoku_after.find_empty(self.puzzle)
        self.assertIsInstance(row, int)
        self.assertIsInstance(col, int)

        # The solution has no empties left
        self.assertIsNone(sudoku_after.find_empty(self.solution))

    def test_is_valid(self):
        board = deepcopy(self.puzzle)
        # 5 is already in row 0, so should be invalid in first empty cell
        row, col = sudoku_after.find_empty(board)
        self.assertFalse(sudoku_after.is_valid(board, row, col, 5))
        # 8 does not break any rules in first empty
        self.assertTrue(sudoku_after.is_valid(board, row, col, 8))

    def test_solve(self):
        board = deepcopy(self.puzzle)
        result = sudoku_after.solve(board)
        self.assertTrue(result)
        self.assertEqual(board, self.solution)

    def test_solve_already_solved(self):
        board = deepcopy(self.solution)
        result = sudoku_after.solve(board)
        self.assertTrue(result)
        self.assertEqual(board, self.solution)

    def test_unsolvable(self):
        # A puzzle with a contradiction
        unsolvable = deepcopy(self.puzzle)
        unsolvable[0][1] = 7  # 7 is already in the row
        board = deepcopy(unsolvable)
        result = sudoku_after.solve(board)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()