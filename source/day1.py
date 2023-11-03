with open("../inputs/day1.txt") as file:
    data = [sum(map(int, x.split('\n'))) for x in file.read().strip().split('\n\n')]

    # part 1
    print(f"Part 1 solution: {max(data)}")
    #part 2
    print(f"Part 2 solution: {sum(sorted(data)[-3:])}")
