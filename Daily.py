# Jackson J
from NewUser import NewUser
from ExUser import ExUser
from Useful_Tools import *

while True:
    menu = input("   " + under_bold("Main Menu") +
                 f"\n1. {bold('New User')}"
                 f"\n2. {bold('Existing User')}"
                 f"\n3. {bold('About Program')}"
                 f"\n4. {bold('Exit')}"
                 "\n>>>")

    while True:
        try:
            menu = int(menu)
            if 0 < menu < 5:
                break
            else:
                raise ValueError
        except ValueError:
            menu = input(f"\nEnter {bold('1')} if you are a {bold('New User')} and do not have an account"
                         f"\nEnter {bold('2')} if are an {bold('Existing User')} and have an account"
                         f"\nEnter {bold('3')} if you want {bold('Information')} about the program"
                         f"\nEnter {bold('4')} if you wish to {bold('Exit')} the program"
                         "\n>>>")

    if menu == 4:
        print(f"\nI, {cur_comp()}, wish you the best."
              "\nThank you for stopping by"
              "\nHave a good day!")
        quit()

    elif menu == 1:
        NewUser(0)

    elif menu == 2:
        ExUser()

    elif menu == 3:
        # make the program wait for input after each '#'
        info = open("ABOUT.txt").read()
        about = ''
        for a in info:
            if a != "#" and a != ">" and a != "\\":
                about += a

            elif a == "#":
                print(about)
                input(bold("press enter to continue".title()))
                about = ""

            if a == "\\":
                print(about)
                input("\nThat concludes the Information"
                      f"\n{bold('Press Enter To Return To The Main Menu')}\n")
                break
