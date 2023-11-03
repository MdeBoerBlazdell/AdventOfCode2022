import numpy as np
from collections import deque


def bfs(graph, root):
    length, width = graph.shape
    explored = set(root)
    queue = deque(root)

    while queue:
        node = queue.pop()
        x, y = node
        if x - 1 != 0:
            if graph[x - 1, y] + 1 == graph[x, y] | graph[x - 1, y] < graph[x, y]:
                queue.append((x - 1, y))
                explored.add((x - 1, y))
        if x + 1 != width:
            if graph[x + 1, y] + 1 == graph[x, y] | graph[x + 1, y] < graph[x, y]:
                queue.append((x + 1, y))
                explored.add((x - 1, y))
        if y - 1 != 0:
            if graph[x, y - 1] + 1 == graph[x, y] | graph[x, y - 1] < graph[x, y]:
                queue.append((x, y - 1))
                explored.add((x, y - 1))
        if y + 1 != length:
            if graph[x, y + 1] + 1 == graph[x, y] | graph[x, y + 1] < graph[x, y]:
                queue.append((x, y + 1))
                explored.add((x, y + 1))


if __name__ == '__main__':
    with open("../inputs/day12.txt") as file:
        lines = file.readlines()
        graph = np.array([[ord(c) - 96 for c in line.strip()] for line in lines])
        print(graph)
