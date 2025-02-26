import numpy as np

board = np.array([
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

def is_valid(board, num, pos):
    row, col = pos
    # Überprüft die Zeile
    if num in board[row, :]:
        return False
    # Überprüft die Spalte
    if num in board[:, col]:
        return False
    # Überprüft das 3x3-Feld
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    return True


def solve(board):
    # Liste der leeren Felder
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    idx = 0
    while idx < len(empty_cells):
        row, col = empty_cells[idx]
        num = board[row][col] + 1
        found = False
        while num <= 9:
            if is_valid(board, num, (row, col)):
                board[row][col] = num
                idx += 1
                found = True
                break
            num += 1
        if not found:
            board[row][col] = 0
            idx -= 1
            if idx < 0:
                return False  # Keine Lösung gefunden
    return True  # Sudoku gelöst


def print_board(board):
    for i in range(9):
        row = ''
        for j in range(9):
            row += str(board[i][j]) if board[i][j] != 0 else '.'
            row += ' '
            if (j + 1) % 3 == 0 and j < 8:
                row += '| '
        print(row)
        if (i + 1) % 3 == 0 and i < 8:
            print('-' * 21)
            
            
print("before")
print_board(board)

print(solve(board))

print("after")
print_board(board)