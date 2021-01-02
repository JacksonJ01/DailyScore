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
          f", my name is {under_bold(cur_comp())}... "
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
            sdate = getDate()

            month = int(sdate[:2])
            month1 = int(sdate[:2])
            day = int(sdate[3:5])
            day1 = day + 6
            day += 13
            year = int(sdate[6:].strip())
            year1 = int(sdate[6:].strip())
            thirtydays = [2, 4, 6, 9, 11]
            thirtyonedays = [1, 3, 5, 7, 8, 10, 12]

            if month in thirtydays:  # check if 2020, 2024, 2028...
                if day1 >= 30 and month != 2:
                    day1 -= 30
                    day -= 30
                    month += 1
                    month1 += 1

                elif day >= 30 and month != 2:
                    day -= 30
                    month += 1

                elif month == 2:
                    isleap = int(year / 4)
                    if (isleap * 4) == year:
                        if day1 >= 29:
                            day1 -= 29
                            day -= 29
                            month += 1
                            month1 += 1

                        elif day1 >= 29:
                            day -= 29
                            month += 1

                    else:
                        if day1 >= 28:
                            day1 -= 28
                            day -= 28
                            month += 1
                            month1 += 1

                        if day >= 28:
                            day -= 28
                            month += 1

            elif month in thirtyonedays:
                if day1 >= 31:
                    day1 -= 31
                    day -= 31
                    month = 1
                    month1 += 1
                    year += 1
                    year1 += 1

                elif day >= 31:
                    day -= 31
                    month = 1
                    year += 1

            if len(str(month)) == 1:
                month = "0" + str(month)
            if len(str(month1)) == 1:
                month1 = '0' + str(month1)
            if len(str(day)) == 1:
                day = "0" + str(day)
            if len(str(day1)) == 1:
                day1 = "0" + str(day1)

            week1 = str(month1) + "/" + str(day1) + "/" + str(year1)
            edate = str(month) + "/" + str(day) + "/" + str(year)

            new = open(f"{fileName}", 'w')
            new.write("User Name: " + first_name + " " + last_name +
                      "\nPin Number: " + str(pinNum) +
                      "\nStart Date: " + sdate +  # # [12:14] [15:17] [18:]
                      "\nHalfway Point: " + week1 +
                      "\nEnd Date: " + edate +  # [10:12] [13:15] [16:]
                      "\n"
                      "\nWeek 1 Total: "  # [14:]
                      "\n"
                      "\nWeek 2 total: "  # [14:]
                      "\n"
                      "\nWinning Week: "  # [14:]
                      "\n#")
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
        print("\nLooks like you're all set"
              "\nI will now take you to the \"Exisng User's\" menu"
              "\nThe next time you log in your will have to do it manually"
              "\nPlease Hold")
        waiting(r(2,4))
        ExUser(fileName)


# NewUser(0)
