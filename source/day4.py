import regex as re


def solution_a(inputs):
    fully_contains = 0
    for left_set, right_set in inputs:
        if left_set.issubset(right_set) | right_set.issubset(left_set):
            fully_contains += 1
    return fully_contains


def solution_b(inputs):
    overlap = 0
    for left_set, right_set in inputs:
        if left_set & right_set:
            overlap += 1
    return overlap


if __name__ == '__main__':
    with open("../inputs/day4.txt") as file:
        inputs = [list(map(int, re.findall(r'\d+', line))) for line in file.read().splitlines()]
        inputs = [({int(i) for i in range(a, b + 1)}, {int(i) for i in range(c, d + 1)}) for a, b, c, d in inputs]
        print(solution_a(inputs))
        print(solution_b(inputs))
