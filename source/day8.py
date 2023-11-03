import numpy as np

if __name__ == '__main__':
    with open("../inputs/day8.txt") as file:
        lines = file.readlines()
        tree_grid = np.array([[int(c) for c in line.strip()] for line in lines])
        width, height = len(tree_grid[0]), len(lines)
        visible_trees = set()

        for x in range(width):
            for y in range(height):
                current_tree = tree_grid[x, y]
                if np.max(tree_grid[0:x, y]) < current_tree:
                    visible_trees.add((x, y))
                elif np.max(tree_grid[x:width, y]) < current_tree:
                    visible_trees.add((x, y))
                elif np.max(tree_grid[x, 0:y]) < current_tree:
                    visible_trees.add((x, y))
                elif np.max(tree_grid[x, y:height]) < current_tree:
                    visible_trees.add((x, y))
        print(len(visible_trees))