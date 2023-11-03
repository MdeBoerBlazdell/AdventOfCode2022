def solution_a(inputs):
    scores = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }
    return sum([scores.get(x) for x in inputs])


def solution_b(inputs):

    scores = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }
    return sum([scores.get(x) for x in inputs])


if __name__ == '__main__':
    with open("../inputs/day2.txt") as file:
        inputs = [x for x in file.read().strip().split("\n")]
        print(solution_a(inputs))
        print(solution_b(inputs))
