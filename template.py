def read_input(filename):
    
    with open(filename, 'r') as file:       # using with closes the file automatically!
        lines = file.readlines()

    return lines

def part1():

    return 0

def part2():

    return 0

def test(part):

    if part == 1:
        assert part1([""]) == 0, "Wrong calculation in test"

    if part == 2:
        assert part2([""]) == 1, "Wrong calculation in test"

######################################################
#
#               START HERE
#
######################################################

filename = "input/01.txt"
lines = read_input(filename)

#PART 1
test(1)
print(f"")

#PART 2
test(2)
print(f"")