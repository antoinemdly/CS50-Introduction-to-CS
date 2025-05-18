from cs50 import get_float

inputed = get_float("Change owed: ")
outputed = 0
"""
while inputeded >= 0:

    if inputeded < 0:
        inputeded =
"""
while inputed >= 0.25:
    inputed -= 0.25
    outputed += 1

while inputed >= 0:
    inputed -= 0.10

    if inputed < 0:
        inputed += 0.10
        break
    elif inputed == 0:
        outputed += 1
        break

    outputed += 1

while inputed >= 0:
    inputed -= 0.05

    if inputed < 0:
        inputed += 0.05
        break
    elif inputed == 0:
        outputed += 1
        break

    outputed += 1

while inputed >= 0:
    inputed -= 0.01

    if inputed <= 0:
        inputed += 0.01
        break
    elif inputed == 0:
        outputed += 1
        break

    outputed += 1




print(f"{outputed}")
