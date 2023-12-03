import re
# list digits in letters
n = "one two three four five six seven eight nine".split()
# regex to match the digits
p = "(?=("+ "|".join(n) + "|\\d))"
# list of calibrations
calibrations = []

# function that maps digits in letters to actual digits
def f(x):
    if x in n:
        return str(n.index(x) + 1)
    return x

# applying all this
for line in open('input.txt'):
    digits = [*map(f,re.findall(p,line))]
    calibrations.append(int(digits[0]+digits[-1]))
print(sum(calibrations))
