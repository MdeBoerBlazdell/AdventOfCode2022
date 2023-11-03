def solution_a(input_string):
    for index in range(0, len(input_string) - 4):
        if len(set(input_string[index:index + 4])) == 4:
            return index+4


def solution_b(input_string):
    for index in range(0, len(input_string) - 14):
        if len(set(input_string[index:index + 14])) == 14:
            return index+14


if __name__ == '__main__':
    with open("../inputs/day6.txt") as file:
        input_string = file.readline().strip()
        print(solution_a(input_string))
        print(solution_b(input_string))
