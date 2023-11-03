import numpy as np

DIRECTIONS = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

if __name__ == '__main__':
    with open("../inputs/test_22") as file:
        grid, commands = file.read().split("\n\n")
        grid = np.array(grid.splitlines())
        print(grid)
        print(commands)
        start_point = np.argwhere(grid[0] == ".")[0]
        print(start_point)
