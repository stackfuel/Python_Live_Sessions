#import time

def sudoku(Board):
    for I in range(9):
      for J in range(9):
         if Board[I][J]==0:
             for NUM in range(1,10):
                 ok=1
                 for k in range(9):
                   if Board[I][k]==NUM or Board[k][J]==NUM:
                        ok=0
                 BoxR = I - I%3
                 BoxC = J-J%3
                 for r in range(3):
                     for   c in range(3):
                       if Board[BoxR+r][BoxC+c]==NUM: ok=0
                 if ok:
                      Board[I][J]=NUM
                      if sudoku(Board): return True
                      Board[I][J]=0
             return False
    return True

Board=[
    [5,1,7,6,0,0,0,3,4],
    [2,8,9,0,0,4,0,0,0],
    [3,4,6,2,0,5,0,9,0],
    [6,0,2,0,0,0,0,1,0],
    [0,3,8,0,0,6,0,4,7],
    [0,0,0,0,0,0,0,0,0],
    [0,9,0,0,0,0,0,7,8],
    [7,0,3,4,0,0,5,6,0],
    [0,0,0,0,0,0,0,0,0]
]

sudoku(Board)
for ROW in Board:print(ROW)


# In pseudocode:
# for each empty cell:
#     for number in possible_numbers:
#         if number is valid:
#             place number
#             if solve(board):    # <--- This line!
#                 return True     # Found solution, exit all recursion!
#             remove number       # Backtrack
#     return False                # No valid number found
# return True                     # No empty cell: solved!