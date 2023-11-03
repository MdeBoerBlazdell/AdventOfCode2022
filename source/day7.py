from collections import defaultdict

directories = defaultdict(int)
root_path = []

if __name__ == '__main__':
    with open("../inputs/day7.txt") as file:
        lines = file.readlines()
        for line in lines:
            match line.split():
                case["$", "ls"] | ["dir", _]:
                    pass
                case ["$", "cd", ".."]:
                    root_path.pop()
                case ["$", "cd", next_path]:
                    root_path.append(next_path)
                case [s, f]:
                    directories[tuple(root_path)] += int(s)
                    path = root_path[:-1]
                    while path:
                        directories[tuple(path)] += int(s)
                        path.pop()

    free_space = 70000000 - directories[("/",)]
    print(sum([value for value in directories.values() if value <= 100000]))
    print(min([value for value in directories.values() if value + free_space >= 30000000]))

