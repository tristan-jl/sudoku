import numpy as np


def print_grid(grid):
    grid = grid.astype(str)
    grid = np.where(grid == "0", " ", grid)

    for i in range(len(grid)):
        line = []

        if i != 0 and i % 3 == 0:
            print("---------+-----------+---------")

        for j in range(len(grid[i])):
            if j != 0 and j % 3 == 0:
                line.append("|")

            line.append(grid[i][j])

        print("  ".join(line))


def get_empty_cell(grid, start=(0, 0)):
    if grid[start] == 0:
        return start

    if start[1] == 8:
        start = (start[0] + 1, 0)

    for i in range(start[0], len(grid)):
        for j in range(start[1], len(grid[i])):
            if grid[i][j] == 0:
                return i, j

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return i, j

    return -1, -1


def get_box_cells(index, grid):
    i, j = index[0] // 3, index[1] // 3
    bi, bj = index[0] - 3 * i, index[1] - 3 * j
    return np.delete(grid[i * 3 : (i + 1) * 3, j * 3 : (j + 1) * 3], bi * 3 + bj)


def is_cell_valid(n, index, grid):
    compare_cells = np.concatenate(
        [
            np.delete(grid[index[0]], [index[1]]),
            np.delete(grid[:, index[1]], index[0]),
            get_box_cells(index, grid),
        ],
        axis=None,
    )

    return np.all(compare_cells != n)


def solve(grid, start=(0, 0)):
    i, j = get_empty_cell(grid, start)
    if i == -1:
        return True

    for n in range(1, len(grid) + 1):
        if is_cell_valid(n, (i, j), grid):
            grid[i][j] = n
            if solve(grid, (i, j)):
                return True

            grid[i][j] = 0

    return False
