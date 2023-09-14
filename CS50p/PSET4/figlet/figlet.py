import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    fonts = figlet.getFonts()
    f = random.choice(fonts)
    figlet.setFont(font=f)
    output = print(f"Output:\n{figlet.renderText(text)}")
elif len(sys.argv) == 3:
    fonts = figlet.getFonts()
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            output = print(f"Output:\n{figlet.renderText(text)}")
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")
