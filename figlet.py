import sys
from pyfiglet import Figlet

figlet = Figlet()

# figlet.setFont(font=f)
import random
# print(figlet.renderText(s))
def main():
    if(len(sys.argv)==3):
        if sys.argv[1] in ['-f','--font']:

            if sys.argv[2] in figlet.getFonts():

                style = input('Input: ')
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(style))
            else:
                print("Invalid usage")
                sys.exit(1)
        else:
            print("Invalid usage")
            sys.exit(1)

    elif(len(sys.argv)==1):
        num = random.randint(0,len(figlet.getFonts()))
        list = figlet.getFonts()
        style = input('Input: ')
        figlet.setFont(font=list[num])
        print(figlet.renderText(style))


    else:
        print("Invalid usage")
        sys.exit(1)

main()
