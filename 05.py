def read_input(filename):
    
    with open(filename, 'r') as file:       # using with closes the file automatically!
        lines = file.readlines()

    return lines

def enoughVowels(check):

    vowels = "aeiou"
    amount = 0

    for char in check:
        if char in vowels:
            amount += 1

    return (amount >= 3)

def doubleLetter(check):

    for index, char in enumerate(check):
        if index == len(check)-2:
            break

        if check[index+1] == char:
            return True
        
    return False

def verdict(check):

    if "ab" in check:
        return "naughty"
    
    if "cd" in check:
        return "naughty"
    
    if "pq" in check:
        return "naughty"
    
    if "xy" in check:
        return "naughty"
    
    if enoughVowels(check) == False:
        return "naughty"

    if doubleLetter(check) == False:
        return "naughty"

    return "nice"

def pairs(check):

    for index in range(len(check)-3):

        pair = check[index:index+2]

        rest = check[index+2:]

        if pair in rest:
            return True

    return False

def repeat(check):

    for index, letter in enumerate(check):

        if index > len(check)-4:
            break
        
        if check[index+2] == letter:
            return True

    return False

def checkAgain(check):

    if pairs(check) == False:
        return "naughty"
    
    if repeat(check) == False:
        return "naughty"

    return "nice"

def part1(lines):

    amount = 0

    for line in lines:
        if verdict(line) == "nice":
            amount += 1

    return amount

def part2(lines):

    amount = 0

    for line in lines:
        if checkAgain(line) == "nice":
            amount +=1

    return amount

def test(part):

    if part == 1:
        assert verdict("ugknbfddgicrmopn") == "nice", "Wrong calculation in test"
        assert verdict("aaa") == "nice", "Wrong calculation in test"
        assert verdict("jchzalrnumimnmhp") == "naughty", "Wrong calculation in test"
        assert verdict("haegwjzuvuyypxyu") == "naughty", "Wrong calculation in test"
        assert verdict("dvszwmarrgswjxmb") == "naughty", "Wrong calculation in test"

    if part == 2:
        assert checkAgain("qjhvhtzxzqqjkmpb") == "nice", "Wrong calculation in test"
        assert checkAgain("xxyxx") == "nice", "Wrong calculation in test"
        assert checkAgain("uurcxstgmygtbstg") == "naughty", "Wrong calculation in test"
        assert checkAgain("ieodomkazucvgmuy") == "naughty", "Wrong calculation in test"

######################################################
#
#               START HERE
#
######################################################

filename = "input/05.txt"
lines = read_input(filename)

#PART 1
test(1)
print(f"Part 1: The number of nice strings are {part1(lines)}")

#PART 2
test(2)
print(f"Part 2: The number of naughty strings are {part2(lines)}")