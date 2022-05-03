# main wrapper for project
# import all src files
# contains argument parsing, error handling, user messaging, script calling
###
import os
import sys
from src.zscript import runZmap


def runRep():
    while True:
        try:
            p = int(input("\nInput Port Number between 0 and 65535 \nor (-1) to return to main menu: "))
        except ValueError:
            print("Error: Invalid input")
            print("Enter a port between 0 and 65535")
            continue
        else:
            if p == -1: return
            elif p < 0 and p > 65535:
                print("Error: Invalid input")
                print("Enter a port between 0 and 65535")
            else:
                break
    while True:
        try:
            n = int(input("\nInput Sample Size less than 500 \nor (-1) to return to main menu: "))
        except ValueError:
            print("Error: Invalid input")
            print("Enter a sample size between 1 and 500")
            continue
        else:
            if n == -1: return
            elif n < 1 and n > 500:
                print("Error: Invalid input")
                print("Enter a sample size between 1 and 500")
            else:
                break
    while True:
        try:
            s = int(input("\nInput Scan Size Small (1), Medium (2), or Large (3) \nor (-1) to return to main menu: "))
        except ValueError:
            print("Error: Invalid input")
            print("Enter a scan size Small (1), Medium (2), or Large (3)")
            continue
        else:
            if s == -1: return
            elif s < 1 and p > 3:
                print("Error: Invalid input")
                print("Enter a scan size Small (1), Medium (2), or Large (3)")
            else:
                break

    runZmap(p, n, s)
    
      


def helpMes():
    helpfile=("docs/help.txt")
    os.system('cat docs/help.txt')
    x = input("Press enter to return to the main menu.\n")


def main():
    ex = 0
    os.system('mkdir output')
    print("Welcome to ZmapReporter, please make a selection from the available options in the main menu and press enter.\n")
    while ex == 0:
        print("Main Menu")
        print("Run Reporter (r)")
        print("Help (h)")
        print("Exit (e)")
        inp = input("Selection: ")
        if (inp == 'r'):
            runRep()

        elif (inp == 'h'):
            helpMes()

        elif (inp == 'e'):
            sys.exit(0)
        else:
            print("Error: Invalid input\n")


if __name__ == "__main__":
    main()

