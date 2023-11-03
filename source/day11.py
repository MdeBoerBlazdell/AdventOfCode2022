import copy
from dataclasses import dataclass


@dataclass()
class Monkey:
    items: list[int]
    operation: str
    divisible_by: int
    yes: int
    no: int
    count: int = 0


def play_rounds(monkeys, part1):
    for monkey in monkeys:
        monkey.count += len(monkey.items)
        while len(monkey.items) > 0:
            item = monkey.items.pop()
            if part1:
                item = monkey.operation(item) // 3
            else:
                item = monkey.operation(item) % 9699690  # LCM of all divisible_by from the monkeys
            if item % monkey.divisible_by == 0:
                monkeys[monkey.yes].items.append(item)
            else:
                monkeys[monkey.no].items.append(item)


def initialise_monkeys():
    monkeys = []
    with open("../inputs/day11.txt") as file:
        monkeys_input = file.read().strip().split("\n\n")
        for monkey in monkeys_input:
            monkey_attributes = monkey.split("\n")
            starting_items = [int(x) for x in monkey_attributes[1].strip("Starting items:").split(", ")]
            operation = eval("lambda old: o" + monkey_attributes[2].strip("Operation: w ="))
            divisible_by = int(monkey_attributes[3].strip("Test: divisible by"))
            yes = int(monkey_attributes[4].strip("If true: throw to monkey"))
            no = int(monkey_attributes[5].strip("If false: throw to monkey"))
            monke = Monkey(starting_items, operation, divisible_by, yes, no)
            monkeys.append(monke)
    return monkeys


if __name__ == '__main__':
    part1_monkeys = initialise_monkeys()
    part2_monkeys = copy.deepcopy(part1_monkeys)
    for _ in range(0, 20):
        play_rounds(part1_monkeys, part1=True)
    for _ in range(0, 10000):
        play_rounds(part2_monkeys, part1=False)

    part1_activity = sorted(list(map(lambda m: m.count, part1_monkeys)))
    part2_activity = sorted(list(map(lambda m: m.count, part2_monkeys)))
    print(part1_activity[-1] * part1_activity[-2])
    print(part2_activity[-1] * part2_activity[-2])
