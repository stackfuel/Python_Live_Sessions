import time

def find_empty(board):
    # Return the row,col of the first empty cell (0), or None if full
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, row, col, num):
    # Check if num can be placed at board[row][col]
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for r in range(3):
        for c in range(3):
            if board[start_row + r][start_col + c] == num:
                return False
    return True

def solve(board):
    pos = find_empty(board)
    if not pos:
        return True  # Solved
    row, col = pos
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else "." for x in row))

if __name__ == "__main__":
    board = [
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

    print("Original board:")
    print_board(board)

    start_time = time.time()
    solved = solve(board)
    end_time = time.time()

    if solved:
        print("\nSolved board:")
        print_board(board)
    else:
        print("No solution.")

    print(f"\nSolved in {end_time - start_time:.6f} seconds.")