# main wrapper for project
# import all src files
# contains argument parsing, error handling, user messaging, script calling
###
import os
import subprocess
import sys
from src.zscript import runZmap


def runRep():
    ex = 0
    while ex == 0:
        p = input("\nInput Port Number: ")
        s = input("Input Sample Size: ")
        if isinstance(p, int) && isinstance(s, int):
            ex = 1
            runZmap(p, s)
        else:
            print("Error: Invalid input\n")


def helpMes():
    helpfile=("docs/help.txt")
    helpMessage = helpfile.read()
    print("\n" + helpMessage)
    x = input("Press enter to return to the main menu.\n")


def main():
    ex = 0;
    mkdir "output"
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

