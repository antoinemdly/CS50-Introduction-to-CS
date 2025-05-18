def is_valid(card_number):
    length = len(card_number)
    sum = 0
    parity = length % 2

    for i in range(length):
        if i % 2 != parity:
            sum += int(card_number[i])
        elif int(card_number[i]) > 4:
            sum += 2 * int(card_number[i]) - 9
        else:
            sum += 2 * int(card_number[i])

    return int(card_number[length - 1]) == (10 - (sum % 10))

# Example usage
card_number = input("Enter a card number: ")
if is_valid(card_number):
    print("Valid card number")
else:
    print("Invalid card number")