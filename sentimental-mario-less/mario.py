from cs50 import get_int
input = 0
while input < 1 or input > 8:
    input = get_int("Height: ")

counter = input - 1
for i in range (1, input + 1):
    print(counter * " " + i * "#" + " " + i * "#")
    counter -= 1
