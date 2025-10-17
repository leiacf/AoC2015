def read_input(filename):
    
    with open(filename, 'r') as file:       # using with closes the file automatically!
        lines = file.readlines()

    return lines

def calculate(lines):

    floor = 0

    for line in lines:
        for char in line:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

    return floor

def basement(lines):

    floor = 0

    for line in lines:
        for index, char in enumerate(line):
            if char == "(":
                floor +=1
            elif char == ")":
                floor -=1
            
            if floor == -1:
                return index+1
    return 0

def test(part):

    if part == 1:
        assert calculate(["()()"]) == 0, "Wrong calculation in test 2"
        assert calculate(["((("]) == 3, "Wrong calculation in test 3"
        assert calculate(["(()(()("]) == 3, "Wrong calculation in test 4"
        assert calculate(["))((((("]) == 3, "Wrong calculation in test 5"
        assert calculate(["())"]) == -1, "Wrong calculation in test 6"
        assert calculate(["))("]) == -1, "Wrong calculation in test 7"
        assert calculate([")))"]) == -3, "Wrong calculation in test 8"
        assert calculate([")())())"]) == -3, "Wrong calculation in test 9"
        assert calculate(["(())"]) == 0, "Wrong calculation in test 1"

    if part == 2:
        assert basement([")"]) == 1, "Wrong calculation in test 10"
        assert basement(["()())"]) == 5, "Wrong calculation in test 11"

######################################################
#
#               START HERE
#
######################################################

filename = "input/01.txt"
lines = read_input(filename)

#PART 1
test(1)
print(f"Part 1: Santa is on floor {calculate(lines)}")

#PART 2
test(2)
print(f"Part 2: The first index where Santa finds the basement is {basement(lines)}")