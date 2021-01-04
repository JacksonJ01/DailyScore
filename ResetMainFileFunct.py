from Useful_Tools import *


def resetMain(file_name):
    new = open(f"{file_name}")

    name = new.readline()[11:].strip()
    first_name = ""
    last_name = ""
    fN = True
    for nme in name:
        if name == " ":
            fN = False
        elif fN is True:
            first_name += nme
        else:
            last_name += nme

    pin = new.readline()[12:].strip()
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
              "\n"
              "\nCurrent Date: "  # [14:]
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
