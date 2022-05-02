# main wrapper for project
# import all src files
# contains argument parsing, error handling, user messaging, script calling
###
import os
import subprocess
import sys
from src.zscript import runZmap


def runRep():
    p = input("\nInput Port Number: ")
    s = input("Input Sample Size: ")
    runZmap(p, s)


def helpMes():
    helpfile=("helpMan.txt")
    helpMessage = helpfile.read()
    print("\n" + helpMessage)
    x = input("Press enter to return to the main menu.\n")


def main():
    exitCode = 0;
    mkdir "output"
    print("Welcome to ZmapReporter, please make a selection from the available options in the main menu and press enter.\n")
    while exitCode == 0:
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

