STACKS = {
    1: ['T', 'R', 'D', 'H', 'Q', 'N', 'P', 'B'],
    2: ['V', 'T', 'J', 'B', 'G', 'W'],
    3: ['Q', 'M', 'V', 'S', 'D', 'H', 'R', 'N'],
    4: ['C', 'M', 'N', 'Z', 'P'],
    5: ['B', 'Z', 'D'],
    6: ['Z', 'W', 'C', 'V'],
    7: ['S', 'L', 'Q', 'V', 'C', 'N', 'Z', 'G'],
    8: ['V', 'N', 'D', 'M', 'J', 'G', 'L'],
    9: ['G', 'C', 'Z', 'F', 'M', 'P', 'T']
}
with open("../inputs/day5.txt", "r") as file:
    instructions = [[int(s) for s in line.split() if s.isdigit()] for line in file.readlines()] # 'move 3 from 2 to 9'

def crane_mover(storage, version="9000"):
    for instruction in instructions:
        quantity, origin, destination = instruction[0], instruction[1], instruction[2]
        if version=="9000":
            move = list(reversed(storage[origin][-quantity:]))  # select boxes to move
        elif version=="9001":
            move = storage[origin][-quantity:]  # select boxes to move
        del storage[origin][-quantity:]  # delete boxes from origin
        storage[destination].extend(move)
    return storage

def get_last_boxes(storage):
    last_result = ""
    for k, v in storage.items():
        last_result += v[-1]
    return last_result

# Part 1
storage = {k: list(reversed(v)) for k,v in STACKS.items()}
sorted_storage = crane_mover(storage, version="9000")
print(get_last_boxes(sorted_storage))

# Part 2 (same but without reverse)
storage = {k: list(reversed(v)) for k,v in STACKS.items()}
sorted_storage = crane_mover(storage, version="9001")
print(get_last_boxes(sorted_storage))
