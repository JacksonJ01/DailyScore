from time import sleep
import os
from datetime import datetime
import calendar
from random import randint
import re
import winsound
from socket import gethostname


def r(minimum, maximum):
    return randint(minimum, maximum)


# Shorter way to access the sleep method
def s(seconds):
    sleep(seconds)


def waiting(number_of_dots):
    for dots in range(1, number_of_dots + 1):
        s(1)
        print("." * dots)


def getM_D_Y_H_M():
    return datetime.now().strftime("%x at %H:%M")


def getDay():
    year = int(datetime.now().strftime("%Y"))
    month = int(datetime.now().strftime("%m"))
    day = int(datetime.now().strftime("%d"))
    dayNum = calendar.weekday(year, month, day)
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday[dayNum]


# To delete a file
def removeFile(filename):
    if os.path.exists(f"{filename}.txt"):
        os.remove(f"{filename}.txt")
    else:
        print(f"The file \"{filename}.txt\" does not exist")

# To remove a folder
# os.rmdir("")


class Fonts:
    purple = '\033[95m'
    cyan = '\033[96m'
    dark_cyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


def bold(make_bold):
    return f"{Fonts.bold}{make_bold}{Fonts.end}"


def red_bold(make_bold):
    return f"{Fonts.bold}{Fonts.red}{make_bold}{Fonts.end}"


def under_bold(make_bold):
    return f"{Fonts.bold}{Fonts.underline}{make_bold}{Fonts.end}"


def blue_bold(make_bold):
    return f"{Fonts.bold}{Fonts.blue }{make_bold}{Fonts.end}"


def Search(check, existing):
    return re.search(r'^' + check, existing)


def cur_comp():
    return gethostname()


def audio(sound=None):
    if sound is None:
        sound = 'piano 2 melody.m4r'
    winsound.PlaySound(sound, winsound.SND_FILENAME)
    print("Here")


# audio("Naruto.wav")
