def solution_a(inputs):
    priority = 0
    for input in inputs:
        c = next(iter(set(input[len(input) // 2:]) & set(input[:len(input) // 2])))
        priority += calculate_priority(c)
    return priority


def solution_b(inputs):
    priority = 0
    groups = [inputs[i:i + 3] for i in range(0, len(inputs), 3)]
    for group in groups:
        a, b, c = group
        badge = next(iter(set(a) & set(b) & set(c)))
        priority += calculate_priority(badge)
    return priority


def calculate_priority(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38


if __name__ == '__main__':
    with open("../inputs/day3.txt") as file:
        inputs = [line for line in file.read().splitlines()]
        print(solution_a(inputs))
        print(solution_b(inputs))
