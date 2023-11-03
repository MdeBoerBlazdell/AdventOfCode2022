if __name__ == '__main__':
    with open("../inputs/day10.txt") as file:
        lines = file.readlines()
        register_value, cycle, signal_strength = 1, 1, 0
        output = []
        for line in lines:
            match line.split():
                case ["noop"]:
                    if cycle % 40 == 20:
                        signal_strength += cycle * register_value
                    if -1 <= (cycle - 1) % 40 - register_value <= 1:
                        output.append("#")
                    else:
                        output.append(" ")
                    cycle += 1
                case [_, i]:
                    for j in range(2):
                        if cycle % 40 == 20:
                            signal_strength += cycle * register_value
                        if -1 <= (cycle - 1) % 40 - register_value <= 1:
                            output.append("#")
                        else:
                            output.append(" ")
                        cycle += 1
                    register_value += int(i)
        print(signal_strength)
        for i in range(6):
            print("".join(output[40*i:40*(i+1)]))

