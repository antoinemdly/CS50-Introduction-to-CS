from pyfiglet import Figlet
import sys
from sys import argv
from cs50 import get_string
import random

figlet = Figlet()
Fonts = figlet.getFonts()


if len(argv) == 1:
    input = get_string("Input : ")
    randomfont = random.choice(Fonts)
    figlet.setFont(font=randomfont)
    print(figlet.renderText(input))
    sys.exit(0)

if argv[1] not in ("-f","--font"):
    print("Invalid usage")
    sys.exit(1)
if argv[2] not in Fonts:
    print("Invalid usage")
    sys.exit(2)

input = get_string("Input : ")
figlet.setFont(font=argv[2])
print(figlet.renderText(input))
sys.exit(0)