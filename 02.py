def read_input(filename):
    
    with open(filename, 'r') as file:       # using with closes the file automatically!
        lines = file.readlines()

    return lines

def part1(lines):

    total = 0

    for line in lines:

        l, w, h = [int(num) for num in line.split("x")]

        a = l*w
        b = w*h
        c = h*l

        smallest = min(a, b, c)

        total += 2*a + 2*b + 2*c + smallest

    return total

def part2(lines):

    total = 0

    for line in lines:

        numbers = [int(num) for num in line.split("x")]
        numbers.sort()

        first, second, third = numbers

        bow = first*second*third

        total += (first*2) + (second*2) + bow

    return total

def test(part):

    if part == 1:
        assert part1(["2x3x4"]) == 58, "Wrong calculation in test"
        assert part1(["1x10x1"]) == 43, "Wrong calculation in test"

    if part == 2:
        assert part2(["2x3x4"]) == 34, "Wrong calculation in test"
        assert part2(["1x1x10"]) == 14, "Wrong calculation in test"

######################################################
#
#               START HERE
#
######################################################

filename = "input/02.txt"
lines = read_input(filename)

#PART 1
#test(1)
print(f"The total square feet of the wrapping paper is {part1(lines)}")

#PART 2
test(2)
print(f"The total feet of ribbon needed is {part2(lines)}")