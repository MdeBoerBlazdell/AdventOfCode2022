from dataclasses import dataclass

@dataclass()
class Point:
    x: int
    y: int


if __name__ == '__main__':
    lines = open("../inputs/day9.txt").read().strip().splitlines()
    visited = [(0,0)]
    head = Point(0, 0)
    tail = Point(0, 0)

    for line in lines:
        direction, distance = line.split(" ")
        distance = int(distance)
        match direction:
            case "U":
                head.y += distance
                for i in range(tail.y + 1, head.y):
                    visited.append((head.x, i))
            case "D":
                head.y -= distance
                for i in reversed(range(head.y + 1, tail.y)):
                    visited.append((head.x, i))
            case "R":
                head.x += distance
                for i in range(tail.x + 1, head.x):
                    visited.append((i, head.y))
            case "L":
                head.x -= distance
                for i in reversed(range(head.x + 1, tail.x)):
                    visited.append((i, head.y))
        if max(abs(head.x - tail.x), abs(head.y - tail.y)) >= 2:
            tail.x, tail.y = visited[-1:][0]
    print(len(set(visited)))