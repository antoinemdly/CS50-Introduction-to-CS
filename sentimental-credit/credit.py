from cs50 import get_string

card = get_string("Number: ")

sum = 0

for i in range (len(card) - 1, -1 , -2):
    sum += int(card[i])
    if i != 0:
        if int(card[i - 1]) > 4:
            sum += 2 * int(card[i - 1]) - 9
        else:
            sum += 2 * int(card[i - 1])

if len(card) == 15 and card[0] == '3' and card[1] in ['4', '7'] and sum % 10 == 0:
    print("Valid American Express Card")
elif len(card) == 16 and card[0] == '5' and card[1] in ['1', '2', '3', '4', '5'] and sum % 10 == 0:
    print("Valid MasterCard Card")
elif len(card) in [13, 16] and card[0] == '4' and sum % 10 == 0:
    print("Valid Visa Card")
else:
    print("Invalid Card")
