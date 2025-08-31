import numpy as np


def grid_paths(grid_size):

    grid = np.zeros((grid_size + 1, grid_size + 1), dtype=np.uint64)

    grid[0, :] = 1
    grid[:, 0] = 1

    for i in range(1, grid_size + 1):
        for j in range(1, grid_size + 1):
            grid[i, j] = grid[i - 1, j] + grid[i, j - 1]

    return grid


grid_size = 20
grid = grid_paths(grid_size)
print(grid[grid_size, grid_size])
