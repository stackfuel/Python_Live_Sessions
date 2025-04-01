import numpy as np


def get_sudoku_string(sudoku):
    """
    Prints a Sudoku board in a readable format.

    Args:
        sudoku (numpy.ndarray): A 2D array representing the Sudoku board, where 0 represents an empty cell.
    """
    if not isinstance(sudoku, np.ndarray):
        raise TypeError("Input must be a numpy ndarray.")
    if sudoku.shape != (9, 9):
        raise ValueError("Input must be a 9x9 array.")

    lines = []
    for i in range(9):
        if i % 3 == 0 and i != 0:
            lines.append("-" * 21)
        
        formatted_row = []
        for j in range(0, 9, 3):
            block = " ".join(str(num) if num != 0 else '.' for num in sudoku[i, j:j+3])
            formatted_row.append(block)

        line = " | ".join(formatted_row)
        lines.append(line)

    return "\n".join(lines)


def is_valid(sudoku, number, position):
    """
    Check if a given number can be placed at a specific position on a Sudoku board.

    Args:
        sudoku (numpy.ndarray): A 2D array representing the Sudoku board, where 0 represents an empty cell.
        number (int): The number to be placed on the board.
        position (tuple): A tuple (row, col) representing the position on the board.
    Returns:
        bool: True if the number can be placed at the given position without violating Sudoku rules, False otherwise.
    """
    
    row, col = position
    row_numbers = set(sudoku[row, :])
    col_numbers = set(sudoku[:, col])
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    tile_numbers = set(sudoku[start_row:start_row+3,
                       start_col:start_col+3].flatten())

    return number not in row_numbers | col_numbers | tile_numbers


def solve_sudoku(sudoku):
    """
    Solves a given Sudoku puzzle using a backtracking algorithm.

    Args:
        sudoku (numpy.ndarray): A 2D array representing the Sudoku board, where 0 represents an empty cell.
    Returns:
        A 2D numpy.ndarray representing the solved Sudoku board.
    Raises:
        ValueError: If no solution is found for the given Sudoku puzzle.
    """

    sudoku = sudoku.copy()
    empty_cells = [(i, j) for i in range(9)
                   for j in range(9) if sudoku[i][j] == 0]
    backtrack_index = 0
    while backtrack_index < len(empty_cells):
        current_empty_cell = empty_cells[backtrack_index]
        for candidate in range(sudoku[current_empty_cell] + 1, 10):
            if is_valid(sudoku, candidate, current_empty_cell):
                sudoku[current_empty_cell] = candidate
                backtrack_index += 1
                break
        else:  # no valid candidate found
            sudoku[current_empty_cell] = 0
            backtrack_index -= 1
            if backtrack_index < 0:
                raise ValueError("No solution found")
    return sudoku


if __name__ == "__main__":

    sudoku_board = np.array([
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
    print("before")
    print(get_sudoku_string(sudoku_board))

    try:
        solved_board = solve_sudoku(sudoku_board)
        print("after")
        print(get_sudoku_string(solved_board))
    except ValueError as e:
        print(str(e))
