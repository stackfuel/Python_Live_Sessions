import numpy as np

def print_sudoku(sudoku_board):
    """
    Prints a Sudoku board in a readable format.

    Args:
        sudoku_board (list of list of int): A 9x9 list representing the Sudoku board,
                                            where 0 represents an empty cell.
    """
    for i in range(9):
        row = ''
        for j in range(9):
            row += str(sudoku_board[i][j]) if sudoku_board[i][j] != 0 else '.'
            row += ' '
            if (j + 1) % 3 == 0 and j < 8:
                row += '| '
        print(row)
        if (i + 1) % 3 == 0 and i < 8:
            print('-' * 21)


def is_valid(sudoku_board, number, position):
    """
    Check if a given number can be placed at a specific position on a Sudoku board.
    Args:
        sudoku_board (numpy.ndarray): A 2D array representing the Sudoku board.
        number (int): The number to be placed on the board.
        position (tuple): A tuple (row, col) representing the position on the board.
    Returns:
        bool: True if the number can be placed at the given position without violating Sudoku rules, False otherwise.
    """
    (row, col) = position
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    if number in sudoku_board[row, :]:
        return False
    if number in sudoku_board[:, col]:
        return False
    if number in sudoku_board[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True


def solve_sudoku(sudoku_board):
    """
    Solves a given Sudoku puzzle using a backtracking algorithm.
    Args:
        sudoku_board (list of list of int): A 9x9 matrix representing the Sudoku board. 
                                            Empty cells are represented by 0.
    Returns:
        list of list of int: A 9x9 matrix representing the solved Sudoku board.
    Raises:
        ValueError: If no solution is found for the given Sudoku puzzle.
    """
    sudoku_board = sudoku_board.copy()
    empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku_board[i][j] == 0]

    current_cell_index = 0
    # go through all empty cells
    while current_cell_index < len(empty_cells):
        row, col = empty_cells[current_cell_index]
        number = sudoku_board[row][col] + 1
        number_found = False
        # go through all numbers
        while number <= 9:
            # check if the number is valid
            if is_valid(sudoku_board, number, (row, col)):
                sudoku_board[row][col] = number 
                current_cell_index += 1
                number_found = True
                break
            number += 1
        # if no number is valid, go back to the
        # previous cell and try another number
        if not number_found:
            sudoku_board[row][col] = 0
            current_cell_index -= 1
            if current_cell_index < 0:
                raise ValueError("No solution found")
    return sudoku_board



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
    print_sudoku(sudoku_board)

    try:
        solved_board = solve_sudoku(sudoku_board)
        print("after")
        print_sudoku(solved_board)
    except ValueError as e:
        print(str(e))
            
