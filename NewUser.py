from Useful_Tools import *
import TaskManager
from ExUser import ExUser


def NewUser(location):  # The "location" parameter basically shows the user another message their second time aorund
                        #  If their name was wrong I want the program to "remember" them and not say "a new face indeed"
    intro = ""
    if location == 0:
        intro = input("\nA new face indeed; I don't think I've seen you around here"
                      "\nWhat is your first and last name?"
                      "\n>>>").title()

    if location == 1:
        intro = input("\nWhat is your first and last name? (Separate each name with a space)"
                      "\n>>>").title()

    first_name = ""
    last_name = ""
    isLastName = False
    for letter in intro:  # This iteration separates the first name from the last name, checking for a space or if the boolean is true
                           # The bool becomes true once a space is found and it just adds the letters to the last_name variable
        if letter == " " or isLastName is True:
            if letter != " ":
                last_name += letter
            isLastName = True
        if isLastName is False:
            first_name += letter

    correct = input(f"\nSo your first name is: {first_name}"
                    f"\nAnd your last name is: {last_name}"
                    "\nIs this correct?"
                    "\n1. Yes"
                    "\n2. No"
                    "\n>>>").title()  # Asks the user if the first and last name they entered was correct

    while True:
        try:
            correct = int(correct)
            if correct == 1 or correct == 2:
                break
            else:
                raise ValueError
        except ValueError:
            correct = input("\nEnter 1 if the data is {}".format(bold("correct")) +
                            f"\nEnter 2 if the data is {bold('incorrect')}"
                            "\n>>>")

    if correct != 1:
        print("\nAlright, give me a couple seconds")
        how_long = r(2, 4)
        waiting(how_long)
        return NewUser(1)  # this utilizes the location parameter mentioned above

    print("\nNice to meet you {}".format(first_name) +
          ", my name is \"Your Computer\"... "
          "\nYou can call me \"Sir\" though")
    # s(2)

    pinNum = input("What would you like your 4 digit Pin Number to be?"
                   "\n>>>")
    while True:
        try:
            length = len(pinNum)
            pinNum = int(pinNum)
            if 3 < length < 5:
                break
            else:
                raise ValueError
        except ValueError:
            pinNum = input(f"Please enter a {red_bold('4')} digit pin. (That means 4 {red_bold('numbers')})"
                           f"\n>>>")

    print("\nNow that the formalities are out of the way, let us get down to business")

    fh = "FileHolder.txt"  # The file that holds the name of the other files will be held in this variable
    kingFile = ""
    try:
        kingFile = open(fh)  # checks to see if the file exists by trying to read it
    except FileNotFoundError:
        kingFile = open(fh, "w")  # creates the file if it does not exist
        kingFile.write("List of File Names:\n")
    finally:
        kingFile.close()  # closes the file whether it was just created or not

    while True:
        kingFile = open(fh)
        fileName = input("What do you want to name your file?"
                         "\n>>>")

        exists = False
        # The loop below checks the main file for any other files that have the same name as the one the user entered
        # exists is a boolean that starts out false, but if something matches it changes to True
        # The loop then breaks and once the if statement sees exist is not False that while loop above runs again#
        for file in kingFile.readlines():
            if Search(file, fileName):
                kingFile.close()
                print("Sorry, that file name already exists, try again\n")
                exists = True
                break

        if exists is False:  # This creates the main file and the task file then adds it to the list
            new = open(f"{fileName}.txt", 'w')
            new.write("User Name: " + first_name + " " + last_name + "\nPin Number: " + str(pinNum))
            new.close()

            tasks = fileName + "_Tasks.txt"
            task_file = open(tasks, 'w')
            task_file.close()

            kingFile = open(fh, 'a')
            kingFile.write(f"\n{fileName}.txt"
                           f"\n{tasks}\n")
            kingFile.close()
            break

    if TaskManager.Task_Manager(tasks, 0) is False:  # tasks is a variable that has the value of the users task file and passes it in
        return NewUser(1)
    else:
        ExUser(fileName)


# NewUser(0)
