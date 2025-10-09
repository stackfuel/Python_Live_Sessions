#import time

def sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    ok = True
                    for k in range(9):
                        if board[i][k] == num or board[k][j] == num:
                            ok = False
                    startRow = i - i % 3
                    startCol = j - j % 3
                    for r in range(3):
                        for c in range(3):
                            if board[startRow + r][startCol + c] == num:
                                ok = False
                    if ok:
                        board[i][j] = num
                        if sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Example puzzle (0 denotes empty cell)
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

#start_time = time.time()
sudoku(board)
#end_time = time.time()
print(board)
#print(f"Solved in {end_time - start_time:.6f} seconds")