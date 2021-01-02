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

            # file = open(file_name.replace(".txt", '_Tasks.txt'))
            # for i in range(0, 4):
            #     file.readline()
            #
            # total = 0
            # while True:
            #     task = file.readline()
            #     if Search("#", task):
            #         break
            #     completed = input("\nDid you complete this task today?"
            #                       f"\n{task}"
            #                       ""
            #                       "\n1. Yes"
            #                       "\n2. No"
            #                       "\n>>>")
            #     while True:
            #         try:
            #             completed = int(completed)
            #             if completed == 1:
            #                 temp = ''
            #                 enter = 0
            #                 for numbers in task:
            #                     if numbers == ':' or 0 < enter:
            #                         enter += 1
            #                         temp += numbers
            #                 temp = temp.replace(':', '').strip()
            #                 try:
            #                     temp = int(temp)
            #                     total += temp
            #                     break
            #                 except ValueError:
            #                     print("\nSomething went wrong"
            #                           "\nTry again and contact the Admin if problem persists")
            #                     ExUser(file_name)
            #
            #             elif completed == 2:
            #                 break
            #             else:
            #                 raise ValueError
            #         except ValueError:
            #             completed = input("\nEnter {} for {}".format(bold('1'), bold('Yes')) +
            #                               "\nEnter {} for {}".format(bold('2'), bold('No')) +
            #                               "\n>>")
            # file.close()
            # print(f"\nYour total points for today is: {total}"
            #       f"\n")

            file = open(file_name)
            count = 1
            while count <= 3:
                file.readline()
                count += 1

            date0 = getDate()
            month = int(date0[:2])
            day = int(date0[3:5])
            year = int(date0[6:].strip())

            # start date
            date = file.readline()
            smonth = int(date[12:14])
            sday = int(date[15:17])
            syear = int(date[18:].strip())

            # halfway point
            date1 = file.readline()
            hmonth = int(date1[15:17])
            hday = int(date1[18:20])
            hyear = int(date1[21:].strip())
            week1 = False

            # end date
            date2 = file.readline()
            emonth = int(date2[10:12])
            eday = int(date2[13:15])
            eyear = int(date2[16:].strip())
            week2 = False

            # check year month day for progress
            # if not year and not next month not access
            if month == hmonth and day <= hday and year == hyear:
                print("Still in week 1")
                # week 1 all
                week1 = True

            elif month == emonth and hday < day <= eday and year == eyear:
                print("Still in week 2")
                # week 2 all
                week2 = True

            elif smonth == month < hmonth and hday < sday < day and year == hyear:
                print("Still in week 1")
                # week 1 year
                week1 = True

            elif hmonth == month < emonth and hday < day and year == eyear:
                print("Still in week 2")
                # week 2 year
                week2 = True

            elif hmonth < smonth == month and hday < sday < day and syear == year < hyear:
                print("Still in week 1")
                # week 1 none
                week1 = True

            elif emonth < emonth == month and hday < day and syear == year < eyear:
                print("Still in week 2")
                # week 2 none
                week2 = True

            #
            else:  # will eventually do this automatically
                print("\nIt seems you have gone past your 2 week interval"
                      "\nYou will have to reset your bi-weekly period"
                      f"\nTo do this, enter 3 on the {bold('previous Menu')}")
                return ExUser(file_name)

            if month == emonth and day == eday and year == eyear:
                week1 = True

            file.close()

            #
            file = open(file_name.replace(".txt", '_Tasks.txt'))
            for i in range(0, 4):
                file.readline()

            total = 0
            while True:
                task = file.readline()
                if Search("#", task):
                    break
                completed = input("\nDid you complete this task today?"
                                  f"\n{task}"
                                  ""
                                  "\n1. Yes"
                                  "\n2. No"
                                  "\n>>>")
                while True:
                    try:
                        completed = int(completed)
                        if completed == 1:
                            temp = ''
                            enter = 0
                            for numbers in task:
                                if numbers == ':' or 0 < enter:
                                    enter += 1
                                    temp += numbers
                            temp = temp.replace(':', '').strip()
                            try:
                                temp = int(temp)
                                total += temp
                                break
                            except ValueError:
                                print("\nSomething went wrong"
                                      "\nTry again and contact the Admin if problem persists")
                                ExUser(file_name)

                        elif completed == 2:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        completed = input("\nEnter {} for {}".format(bold('1'), bold('Yes')) +
                                          "\nEnter {} for {}".format(bold('2'), bold('No')) +
                                          "\n>>")
            file.close()
            print(f"\nYour total points for today is: {total}"
                  f"\n")
            #

            file = open(file_name)
            update = ''
            for x in range(0, 7):
                update += file.readline()

            if week1 is True and week2 is False:
                update += "Week 1 Total: "
                week1total = int(file.readline()[14:].strip()) + total

                update += str(week1total) + \
                          "\n" \
                          "\n" + file.readline() + \
                          "\n" + file.readline() + \
                          "\n" + file.readline() + \
                          "\n" + file.readline() + \
                          "\n#"

            elif week2 is True:
                week1 = file.readline()
                week1total = int(week1[14:])

                update += week1 + \
                          "\n" \
                          "Week 2 Total: "
                week2total = int(file.readline()[14:].strip()) + total

                if week1 is True:
                    winner = ''
                    if week2total < week1total:
                        winner = f"Week 1 by {week1total - week2total}"

                    elif week1total < week2total:
                        winner = f"Week 2 by {week2total - week2total}"

                    update += str(week2total) + \
                              "\n" \
                              "\n" + file.readline().strip() + winner +\
                              "\n#"

                else:
                    update += str(week2total) + \
                              "\n" \
                              "\n" + file.readline() + \
                              "#"

            file.close()

            file = open(file_name, 'w')
            file.write(update)
            file.close()

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

            new = open(f"{file_name}", 'w')
            new.write("User Name: " + first_name + " " + last_name +
                      "\nPin Number: " + str(pin) +
                      "\nStart Date: " + sdate +  # [12:14] [15:17] [18:]
                      "\nHalfway Point: " + week1 +  # [14:16] [17:19] [20:]
                      "\nEnd Date: " + edate +  # [10:12] [13:15] [16:]
                      "\n"
                      "\nWeek 1 Total: "  # [14:]
                      "\n"
                      "\nWeek 2 total: "  # [14:]
                      "\n"
                      "\nWinning Week: "  # [14:]
                      "\n#")
            new.close()

            print("\nYour file has been reset"
                  "\nI will now take you back to the Menu")

        elif menu == 4:
            print()
            return


ExUser("sirJack.txt")
