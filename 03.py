def read_input(filename):
    
    with open(filename, 'r') as file:       # using with closes the file automatically!
        lines = file.readlines()

    return lines

def part1(lines):

    santa = (0,0)
    deliveries = {santa:1}

    for line in lines:

        for char in line:

            x, y = santa

            if char == "^":
                y = y+1

            elif char == ">":
                x = x+1

            elif char == "v":
                y = y-1

            elif char == "<":
                x = x-1
                
            santa = (x, y)

            if santa not in deliveries:
                deliveries[santa] = 1
            else: 
                deliveries[santa] += 1

    return len(deliveries)

def part2(lines):

    santa = (0,0)
    robo = (0, 0)

    deliveries = {santa:1}
    deliveries[robo] += 1

    for line in lines:

        for index, char in enumerate(line):

            if index % 2 == 0:
                x, y = santa
            else:
                x, y = robo

            if char == "^":
                y = y+1

            elif char == ">":
                x = x+1

            elif char == "v":
                y = y-1

            elif char == "<":
                x = x-1

            current = (x, y)

            if current not in deliveries:
                deliveries[current] = 1
            else: 
                deliveries[current] += 1

            if index % 2 == 0:
                santa = current
            else:
                robo = current

    return len(deliveries)

def test(part):

    if part == 1:
        assert part1([">"]) == 2, "Wrong calculation in test"
        assert part1(["^>v<"]) == 4, "Wrong calculation in test"
        assert part1(["^v^v^v^v^v"]) == 2, "Wrong calculation in test"

    if part == 2:
        assert part2(["^v"]) == 3, "Wrong calculation in test"
        assert part2(["^>v<"]) == 3, "Wrong calculation in test"
        assert part2(["^v^v^v^v^v"]) == 11, "Wrong calculation in test"


######################################################
#
#               START HERE
#
######################################################

filename = "input/03.txt"
lines = read_input(filename)

#PART 1
test(1)
print(f"Part 1: The amount of houses getting at least one present is {part1(lines)}")

#PART 2
test(2)
print(f"Part 2: The amount of houses getting at least one present is {part2(lines)}")