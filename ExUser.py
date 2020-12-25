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
                break
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
        menu = input("\nMenu"
                     "\n1. Daily Check-In"
                     "\n2. Configure Tasks"
                     "\n3. Reset Bi-Weekly Period"
                     "\n4. Exit"
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
            print("Work In Progress")

        elif menu == 2:
            # Task manager
            file_name += "_Tasks.txt"
            print(file_name)
            Task_Manager(file_name)

        elif menu == 3:
            # Reset period
            print("Work In Progress")

        elif menu == 4:
            return


# ExUser()
