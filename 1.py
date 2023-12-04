
text = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

total = 0
firstNumber = None
secondNumber = None

for line in text.split('\n'):
    firstNumber = None
    secondNumber = None
    for i, c in enumerate(line):

        if c.isdigit():
            if firstNumber is None:
                firstNumber = int(c)
                secondNumber = int(c)
            else:
                secondNumber = int(c)
        for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                if firstNumber is None:
                    firstNumber = str(j + 1)
                    secondNumber = str(j + 1)
                else:
                    secondNumber = str(j + 1)
    if firstNumber is not None and secondNumber is not None:
        total += int(str(firstNumber) + str(secondNumber))

print(total)

