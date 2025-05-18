from cs50 import get_float

inputed = get_float("Change owed: ")
outputed = 0

while inputed >= 0.25:
    inputed -= 0.25
    outputed += 1

while inputed >= 0.10:
    inputed -= 0.10
    outputed += 1

while inputed >= 0.05:
    inputed -= 0.05
    outputed += 1

while inputed >= 0.01:
    inputed -= 0.01
    outputed += 1

print(f"{outputed}")