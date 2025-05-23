import numpy as np

matrix = np.array([
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
lines = []
for i in range(9):
    if i % 3 == 0 and i != 0:
        lines.append("-" * 21)

    formatted_row = []
    for j in range(0, 9, 3):
        block = " ".join(str(num) if num !=
                            0 else '.' for num in matrix[i, j:j+3])
        formatted_row.append(block)

    line = " | ".join(formatted_row)
    lines.append(line)

print("\n".join(lines))

cells = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]
i = 0
while i < len(cells):
    row, col = cells[i]
    x = matrix[row][col] + 1
    found = False

    while x <= 9:
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if (x in matrix[row, :] or
            x in matrix[:, col] or
            x in matrix[start_row:start_row+3, start_col:start_col+3]):
            x += 1
            continue
        else:
            matrix[row][col] = x
            i += 1
            found = True
            break

    if not found:
        matrix[row][col] = 0
        i -= 1
        if i < 0:
            break

print(found)
if found:
    print("after")
    lines = []
    for i in range(9):
        if i % 3 == 0 and i != 0:
            lines.append("-" * 21)

        formatted_row = []
        for j in range(0, 9, 3):
            block = " ".join(str(num) if num !=
                                0 else '.' for num in matrix[i, j:j+3])
            formatted_row.append(block)

        line = " | ".join(formatted_row)
        lines.append(line)
    print("\n".join(lines))
