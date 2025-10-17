import hashlib

def read_input(filename):
    
    with open(filename, 'r') as file:       # using with closes the file automatically!
        lines = file.readlines()

    return lines

def part1(lines):

    for line in lines:

        number = 0

        while True:

            test = line + str(number)
            check = hashlib.md5(test.encode()).hexdigest()

            if check.startswith("00000"):
                break
            
            number += 1

    return number

def part2(lines):

    for line in lines:

        number = 0

        while True:

            test = line + str(number)
            check = hashlib.md5(test.encode()).hexdigest()

            if check.startswith("000000"):
                break
            
            number += 1

    return number

def test(part):

    if part == 1:
        assert part1(["abcdef"]) == 609043, "Wrong calculation in test"
        assert part1(["pqrstuv"]) == 1048970, "Wrong calculation in test"

######################################################
#
#               START HERE
#
######################################################

filename = "input/04.txt"
lines = read_input(filename)

#PART 1
test(1)
print(f"Part 1: The first number to give us five leading zeros is {part1(lines)}")

#PART 2
#test(2)
print(f"Part 2: The first number to give us six leading zeros is {part2(lines)}")