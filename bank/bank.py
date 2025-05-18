from cs50 import get_string

Answer = get_string("Greeting : ")
Check = Answer.replace(" ","")
Check = Check[:5]


if Check.lower() == "hello":
    print("$0")
elif Check[0].lower() == "h":
    print("$20")
else:
    print("$100")
