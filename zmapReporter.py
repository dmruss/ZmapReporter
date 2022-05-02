# main wrapper for project
# import all src files
# contains argument parsing, error handling, user messaging, script calling
###
import os
import subprocess
import sys
from zscript import runZmap


def runRep():
    p = input("\nInput Port Number: ")
    s = input("Input Sample Size: ")
    runZmap(p, s)


def helpMes():
    print("\nWelcome to ZmapReporter, *insert description of our app*. Start by *insert instructions for operation*. ")
    x = input("Press enter to return to the main menu.\n")


def main():
    exitCode = 0;
    os.system("chmod +x setup.sh")
    subprocess.run("./setup.sh")
    print(
        "Welcome to ZmapReporter, please make a selection from the available options in the main menu and press enter.\n")
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

