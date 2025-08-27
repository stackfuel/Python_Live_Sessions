import pytest
import numpy as np
from sudoku_solver import get_sudoku_string, is_valid, solve_sudoku

def test_get_sudoku_string_valid_input():
    """Test that get_sudoku_string correctly formats a valid sudoku board."""
    test_board = np.array([
        [4, 1, 3, 9, 8, 6, 2, 5, 7],
        [9, 8, 5, 6, 1, 7, 2, 3, 4],
        [2, 6, 7, 5, 3, 4, 7, 9, 1],
        [8, 7, 1, 3, 4, 5, 6, 2, 9],
        [5, 3, 9, 7, 2, 6, 1, 8, 4],
        [4, 2, 6, 8, 9, 1, 3, 7, 5],
        [1, 9, 2, 4, 7, 3, 5, 6, 8],
        [7, 6, 4, 5, 3, 8, 9, 2, 1],
        [3, 5, 8, 1, 6, 2, 4, 7, 3]
    ])
    result = get_sudoku_string(test_board)
    assert isinstance(result, str)
    assert len(result.splitlines()) == 11  # 9 rows + 2 separator lines

def test_get_sudoku_string_invalid_input():
    """Test that get_sudoku_string raises appropriate errors for invalid inputs."""
    # Test non-ndarray input
    with pytest.raises(TypeError):
        get_sudoku_string([1, 2, 3])
    
    # Test wrong shape
    with pytest.raises(ValueError):
        get_sudoku_string(np.array([[1, 2], [3, 4]]))

def test_is_valid_empty_position():
    """Test the is_valid function with an empty position."""
    test_board = np.zeros((9, 9), dtype=int)
    # In an empty board, any number should be valid at any position
    assert is_valid(test_board, 5, (0, 0))
    assert is_valid(test_board, 9, (8, 8))

def test_is_valid_row_conflict():
    """Test that is_valid correctly identifies row conflicts."""
    test_board = np.zeros((9, 9), dtype=int)
    test_board[0, 0] = 5  # Put a 5 in the first position
    # Now 5 should not be valid anywhere else in the first row
    assert not is_valid(test_board, 5, (0, 1))
    assert not is_valid(test_board, 5, (0, 8))
    # But 5 should be valid in other rows
    assert is_valid(test_board, 5, (1, 8))

def test_is_valid_column_conflict():
    """Test that is_valid correctly identifies column conflicts."""
    test_board = np.zeros((9, 9), dtype=int)
    test_board[0, 0] = 5  # Put a 5 in the first position
    # Now 5 should not be valid anywhere else in the first column
    assert not is_valid(test_board, 5, (1, 0))
    assert not is_valid(test_board, 5, (8, 0))
    # But 5 should be valid in other columns
    assert is_valid(test_board, 5, (3, 1))

def test_is_valid_block_conflict():
    """Test that is_valid correctly identifies 3x3 block conflicts."""
    test_board = np.zeros((9, 9), dtype=int)
    test_board[0, 0] = 5  # Put a 5 in the first position
    # Now 5 should not be valid anywhere else in the first 3x3 block
    assert not is_valid(test_board, 5, (0, 2))
    assert not is_valid(test_board, 5, (2, 2))
    # But 5 should be valid in other blocks
    assert is_valid(test_board, 5, (2, 3))
    assert is_valid(test_board, 5, (3, 2))

def test_is_valid_no_conflict():
    """Test that is_valid correctly identifies positions with no conflicts."""
    test_board = np.array([
        [4, 0, 0, 9, 0, 0, 0, 5, 0],
        [0, 0, 5, 6, 0, 7, 2, 0, 4],
        [0, 0, 0, 0, 0, 4, 7, 0, 0],
        [8, 7, 0, 3, 0, 0, 6, 0, 0],
        [0, 0, 9, 7, 2, 0, 1, 8, 0],
        [0, 0, 6, 8, 9, 1, 0, 0, 0],
        [1, 0, 2, 4, 0, 0, 5, 6, 8],
        [7, 6, 0, 5, 3, 8, 0, 0, 1],
        [0, 0, 8, 0, 0, 2, 0, 7, 0]
    ])
    # Position (0, 1) should allow 1, 2, 3, 6, 7, 8
    assert is_valid(test_board, 1, (0, 1))
    assert is_valid(test_board, 3, (0, 1))
    # But not 4, 5, 9 (already in row, column, or block)
    assert not is_valid(test_board, 4, (0, 1))  # 4 is in row
    assert not is_valid(test_board, 5, (0, 1))  # 5 is in block (adjacent block)
    assert not is_valid(test_board, 9, (0, 1))  # 9 is in row

def test_solve_sudoku_solvable():
    """Test that solve_sudoku correctly solves a solvable puzzle."""
    test_board = np.array([
        [4, 0, 0, 9, 0, 0, 0, 5, 0],
        [0, 0, 5, 6, 0, 7, 2, 0, 4],
        [0, 0, 0, 0, 0, 4, 7, 0, 0],
        [8, 7, 0, 3, 0, 0, 6, 0, 0],
        [0, 0, 9, 7, 2, 0, 1, 8, 0],
        [0, 0, 6, 8, 9, 1, 0, 0, 0],
        [1, 0, 2, 4, 0, 0, 5, 6, 8],
        [7, 6, 0, 5, 3, 8, 0, 0, 1],
        [0, 0, 8, 0, 0, 2, 0, 7, 0]
    ])
    solved_board = solve_sudoku(test_board)
    
    # Check that the original board hasn't been modified
    assert np.any(test_board == 0)
    
    # Verify the solved board has no zeros (all filled)
    assert not np.any(solved_board == 0)
    
    # Check all rows contain digits 1-9
    for row in range(9):
        assert set(solved_board[row, :]) == set(range(1, 10))
    
    # Check all columns contain digits 1-9
    for col in range(9):
        assert set(solved_board[:, col]) == set(range(1, 10))
    
    # Check all 3x3 blocks contain digits 1-9
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = solved_board[block_row:block_row+3, block_col:block_col+3].flatten()
            assert set(block) == set(range(1, 10))
    
    # Verify that the original filled positions are preserved
    for i in range(9):
        for j in range(9):
            if test_board[i, j] != 0:
                assert solved_board[i, j] == test_board[i, j]

def test_solve_sudoku_unsolvable():
    """Test that solve_sudoku raises ValueError for an unsolvable puzzle."""
    # Create an unsolvable board
    unsolvable_board = np.array([
        [4, 1, 3, 9, 8, 6, 2, 5, 7],
        [9, 8, 5, 6, 1, 7, 2, 3, 4],
        [2, 6, 7, 5, 3, 4, 7, 9, 1],
        [8, 7, 1, 3, 4, 5, 6, 2, 9],
        [5, 3, 9, 7, 2, 6, 1, 8, 4],
        [4, 2, 6, 8, 9, 1, 3, 7, 5],
        [1, 9, 2, 4, 7, 3, 5, 6, 8],
        [7, 6, 4, 5, 3, 8, 9, 2, 1],
        [3, 4, 8, 1, 6, 2, 0, 0, 0]
    ])
    
    with pytest.raises(ValueError, match="No solution found"):
        solve_sudoku(unsolvable_board)

def test_solve_sudoku_already_solved():
    """Test that solve_sudoku works correctly with an already solved puzzle."""
    # A completed valid sudoku
    solved_board = np.array([
        [4, 3, 5, 2, 6, 9, 7, 8, 1],
        [6, 8, 2, 5, 7, 1, 4, 9, 3],
        [1, 9, 7, 8, 3, 4, 5, 6, 2],
        [8, 2, 6, 1, 9, 5, 3, 4, 7],
        [3, 7, 4, 6, 8, 2, 9, 1, 5],
        [9, 5, 1, 7, 4, 3, 6, 2, 8],
        [5, 1, 9, 3, 2, 6, 8, 7, 4],
        [2, 4, 8, 9, 5, 7, 1, 3, 6],
        [7, 6, 3, 4, 1, 8, 2, 5, 9]
    ])
    
    result = solve_sudoku(solved_board)
    # The result should be the same as the input
    assert np.array_equal(result, solved_board)

def test_solve_sudoku_edge_cases():
    """Test solve_sudoku with edge cases."""
    # Almost empty board (only one clue)
    sparse_board = np.zeros((9, 9), dtype=int)
    sparse_board[0, 0] = 1
    
    # This should still be solvable
    solved = solve_sudoku(sparse_board)
    
    # Check solution validity
    assert not np.any(solved == 0)
    
    # Verify that the original filled position is preserved
    assert solved[0, 0] == 1
    
    # Check all rows, columns, and blocks contain digits 1-9
    for row in range(9):
        assert set(solved[row, :]) == set(range(1, 10))
    
    for col in range(9):
        assert set(solved[:, col]) == set(range(1, 10))
    
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = solved[block_row:block_row+3, block_col:block_col+3].flatten()
            assert set(block) == set(range(1, 10))