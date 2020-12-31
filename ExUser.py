from Useful_Tools import *
from TaskManager import Task_Manager


def ExUser(file_name=None):
    if file_name is None:
        print(f"\nYou will get {bold('3 total attempts')} when trying to access your existing account"
              f"\nYou will be taken back to Main Menu if run out of attemps")
        attempts = 3
        while True:
            file_name = input("\nWhat is the name of your file?"
                              "\n>>>")
            if file_name[-4:] != ".txt":
                file_name += ".txt"

            try:
                temp = open(file_name)
                temp.close()
                break
            except FileNotFoundError:
                attempts -= 1
                print("\nYou have {} attempts left".format(red_bold(f"{attempts}")))
                if attempts > 0:
                    print("Please try again")
                else:
                    print(f"\n{bold('You Are Out Of Attempts')}"
                          "\nReturing to the Main Menu")
                    waiting(r(2, 3))
                    print("\n")
                    return False

        while True:
            pinNum = input("\nWhat is your 4 digit Pin Number?"
                           "\n>>>")

            while True:
                try:
                    length = len(pinNum)
                    if 3 < length < 5:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    attempts -= 1
                    print("\nYou have {} attempts left".format(red_bold(f"{attempts}")))
                    if attempts > 0:
                        print("Try again")
                    else:
                        print(f"\n{bold('You have exhausted all of your attempts')}"
                              f"\nYou will now be taken back to the Main Menu")
                        waiting(r(2, 3))
                        print("\n")
                        return False

                    pinNum = input(f"Please enter your {red_bold('4')} digit Pin Number"
                                   f"\n>>>")

            print("\nAlright let me check if that Pin Number matches the Pin on the file")
            waiting(r(2, 3))

            # open the file for reading and read the second line

            file = open(file_name)
            name = file.readline()[11:]
            pin = file.readline()[12:]

            if Search(pinNum, pin):
                print(f"\nHey, welcome back {name}")
                return ExUser(file_name)
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"\nThe 4 digit Pin Number you entered {red_bold('does not')} match the file"
                          f"\nYou have {red_bold(attempts)} left"
                          "\nPlease try again")
                else:
                    print(f"\n{bold('You are fresh out of attempts')}"
                          "\nNow taking you back to the Main Menu")
                    waiting(r(2, 3))
                    print("\n")
                    return False

    while True:
        menu = input(f"\n   {under_bold('Menu')}"
                     f"\n1. {bold('Daily Check-In')}"
                     f"\n2. {bold('Configure Tasks')}"
                     f"\n3. {bold('Reset Bi-Weekly Period')}"
                     f"\n4. {bold('Exit To the Main Menu')}"
                     "\n>>>")

        while True:
            try:
                menu = int(menu)
                if 0 < menu < 5:
                    break
                else:
                    raise ValueError
            except ValueError:
                menu = input(f"Please Enter {bold(1)}, "
                             f"{bold(2)}, "
                             f"{bold(3)}, or "
                             f"{bold(4)}")

        if menu == 1:
            # CHeck-in
            print("\nWork In Progress")

            file = open(file_name + "_Tasks".replace(".txt", '') + ".txt")
            for i in range(0,4):
                file.readline()

            task = ''
            total = 0
            while not Search("#", task):
                task = file.readline()
                completed = input("\nDid you complete this task?"
                                  f"\n{task}"
                                  ""
                                  "\n1. Yes"
                                  "\n2. No"
                                  ">>>")
                while True:
                    try:
                        completed = int(completed)
                        if completed == 1:
                            temp = ''
                            enter = 0
                            for numbers in task:
                                if numbers == ':' or 0 < enter:
                                    enter += 1
                                    temp = numbers
                            print(temp)
                            temp = temp.strip().replace(':','')
                            try:
                                temp = int(temp)
                                total += temp
                            except ValueError:
                                print("\nSomething went wrong"
                                      "\nTry again and contact the Admin if problem persists")
                                ExUser(file_name)

                        elif completed == 2:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        completed = input("\nEnter {} for {}".format(bold('1'),bold('Yes')) +
                                          "\nEnter {} for {}".format(bold('2'),bold('No')) +
                                          "\n>>")
            file.close()
            print(f"\nYour total points for today is: {total}"
                  f"\n")


        elif menu == 2:
            # Task manager
            file_name += "_Tasks.txt"
            print(file_name)
            Task_Manager(file_name)
            print("\nI will now take you back to the Menu")

        elif menu == 3:
            # Reset 2 week period
            new = open(f"{file_name}")
            name = new.readline()
            first_name = name[11:17].strip()
            last_name = name[17:].strip()
            pin = new.readline()[12:]
            new.close()

            new = open(file_name, "w")
            new.write("User Name: " + first_name + " " + last_name +
                      "\nPin Number: " + str(pin) +
                      "Start Date: " + getDate() +  # [12:14] [15:17] [18:]
                      "\nCurrent Date: " + getDate() +  # [14:16] [17:19] [20:]
                      ""
                      "\n\nWEEK 1:"
                      "\nWeek 1 Total: "  # [14:]
                      ""
                      "\n\nWEEK 2:"
                      "\nWeek 2 total: "  # [14:]
                      "\n#")
            new.close()

            print("\nYour file has been reset"
                  "\nI will now take you back to the Menu")

        elif menu == 4:
            print()
            return


ExUser("sirJack.txt")
