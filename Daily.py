# Jackson J

# Tasks:
#  SMAJBLoL                                   10
#  Wake up at 5:30 am                          5
#    if no: wake up at 6 am                    3
#      if no: why                              1
#  Poop                                        2
#  Brush teeth                                 1
#  Workout                                    10
#  Eat breakfast#                              3
#  Shower                                      3
#  Attend all classes for the day             10
#    if no: attend most classes                5
#      if no: why                              0
#  Go to work On Time                          10
#    if no: go to work "on time"               5
#  Brush teeth                                 1
#  Go to bed On Time                          10
# Max Points:                                 65

from NewUser import NewUser
from ExUser import ExUser
from Useful_Tools import *

while True:
    menu = input("   " + under_bold("Main Menu") +
                 "\n1. New User"
                 "\n2. Existing User"
                 "\n3. About Program"
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
            menu = input(f"\nEnter 1 if you are a {bold('new user')} and do not have an account"
                         f"\nEnter 2 if are an {bold('existing user')} and have an account"
                         "\n>>>")

    if menu == 4:
        quit()

    elif menu == 1:
        NewUser(0)

    elif menu == 2:
        if ExUser() is False:
            print("I'll take you back to the Menu")

    elif menu == 3:
        # make the program wait for input after each '#'
        print(open("ABOUT.txt").read())
        input("Press Enter to return to the Menu")
