from Useful_Tools import *
from ResetMainFileFunct import resetMain


def Task_Manager(task_file, location=None):
    try:
        file = open(task_file)
        file.close()
    except FileNotFoundError:
        print("\nSomething went wrong.."
              "\nWe will have to start over")
        return False

    file_name = f"{task_file}".replace("_Tasks", "")

    menu = 0
    while True:
        if location is None:
            menu = input(f"\n   {under_bold('Task Menu')}"
                         f"\n1. {bold('View Tasks')}"
                         f"\n2. {bold('Replace Tasks')}"
                         f"\n3. {bold('Add Tasks')}"
                         f"\n4. {bold('Delete Tasks')}"
                         f"\n5. {bold('Update Goal and Prize')}"
                         f"\n6. {bold('Create New Tasks')}"
                         f"\n7. {bold('EXIT')}"
                         "\n>>>")

            while True:
                try:
                    menu = int(menu)
                    if 0 < menu < 8:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    menu = input("Enter"
                                 f"{bold('1')}, "
                                 f"{bold('2')}, "
                                 f"{bold('3')}, "
                                 f"{bold('4')}, "
                                 f"{bold('5')}, "
                                 f"{bold('6')}, or"
                                 f"{bold('7')}"
                                 f"\n>>>")

        if location == 0:
            menu = 6

        if menu == 2 or menu == 3 or menu == 4 or menu == 6:
            stop = input("\nDoing this will reset your current weekly progress"
                         "\nDo you wish to continue?"
                         "\n1. Yes"
                         "\n2. No"
                         "\n>>>")

            while True:
                try:
                    stop = int(stop)
                    if 0 < stop < 3:
                        if stop == 2:
                            print(f"\nOkay, I will take you back to the {bold('Task Menu')}")
                            Task_Manager(task_file)
                        else:
                            print("\nOkay, moving forward")
                            break
                    else:
                        raise ValueError
                except ValueError:
                    stop = input("\nPlease choose whether or not you want to Continue"
                                 "\n1. Continue"
                                 "\n2. Return the the Task Menu"
                                 "\n>>>")

        if menu == 1:  # Reads the task file
            print("View Tasks")
            file = open(task_file)
            print("Here are your tasks:\n"
                  f"\n{file.read()}")
            file.close()

        # Reads the task file then asks the user how many tasks and which number they want to change
         # There will be a loop that will stop at each line and read the contents
         # Afterwards the user can type the change and it will save over and move to the next line
         # When the program reads each line the user wants to change it will take the points and subtract it from the total.
          # When the user creates a new task they will also be prompted to specify the point value of that task
          # That value will then be added to the total
          # The user will also have to set a new goal for themselves since the value is different
        elif menu == 2:
            count = -4
            print("Change Tasks")
            file = open(task_file)
            print("Here is what your task file looks like:\n")
            print(file.read())
            file.close()

            file = open(task_file)
            while True:
                if Search("#", file.readline()):
                    break
                count += 1
            file.close()

            change_tasks = input("You have {} tasks. How many of those tasks, how many do you wish to change?".format(count) +
                                 '\n>>>')

            while True:
                try:
                    change_tasks = int(change_tasks)
                    if 0 < change_tasks < count:
                        break

                    elif change_tasks == count:
                        change = input("\nIt seems as though you would like you change every one of your tasks."
                                       "\nWould you like to:"
                                       f"\n1. {bold('Create New Tasks')} using the Task Menu"
                                       f"\n2. {bold('Continue')}"
                                       f"\n>>>")
                        while True:
                            try:
                                change = int(change)
                                if change == 1:
                                    print("\nUnderstood. I will now take you to the Task Menu")
                                    waiting(r(2,3))
                                    return Task_Manager(task_file)
                                elif change == 2:
                                    print("\nAlright, I will continue."
                                          "\nMaybe you just wanted to tweak the tasks a bit")
                                    break
                                else:
                                    raise ValueError

                            except ValueError:
                                change = input(f"\nPlease enter {bold('1 or 2')}"
                                               f"\n>>>")
                        break

                    else:
                        raise ValueError

                except ValueError:
                    change_tasks = input("\nYou entered a number greater than {}.".format(count) +
                                         "\nPlease enter a lower number, one that is greater than 0"
                                         "\n>>>")

            input("\nI will now ask you recite the number of the tasks you wish to change"
                  "\nPress Enter to continue")

            taskNum = []
            num = 0
            changing = change_tasks
            while 0 < changing:
                if changing == 1 and num == 0:
                    adding = input("\nWhat is the number of the task you would you like change?"
                                   "\n>>>")
                elif num == 0:
                    adding = input("\nWhat is the number of the first task you would you like change?"
                                   "\n>>>")
                    num += 1
                else:
                    adding = input("\nWhat is the number of the next task you would you like change?"
                                   "\n>>>")
                    num += 1

                changing -= 1

                while True:
                    try:
                        adding = int(adding)
                        if adding <= count and adding not in taskNum:
                            taskNum.append(adding)
                            break

                        elif adding > count:
                            raise ValueError

                        elif adding in taskNum:
                            raise ZeroDivisionError

                    except ValueError:
                        adding = input("\nYou entered a number over the total number of tasks you have."
                                       "\nEnter a smaller number"
                                       "\n>>>")

                    except ZeroDivisionError:
                        adding = input("\nYou have already entered this number"
                                       "\nEnter a new number"
                                       "\n>>>")
            taskNum.sort()
            taskNum.reverse()

            file = open(task_file)
            update = ""
            prize = ""
            goal = 0
            total = 0
            counting = 0
            sub = 0
            task = ''
            while True:
                counting += 1
                try:
                    task = file.readline()
                    if counting == 1:
                        prize = task[0:19]
                    elif counting == 2:
                        goal = int(task[12:])
                    elif counting == 3:
                        total = int(task[19:])

                    if Search(str(taskNum[-1]), task):
                        print(f"\nYour current task for number {taskNum[-1]} is:"
                              f"\n{task}")
                        change = input("What would you like to change the task description too?"
                                       "\n>>>").capitalize().replace(":", "~")

                        change_amount = input("\nAnd what is the amount for that task?"
                                              "\n>>>")
                        while True:
                            try:
                                change_amount = int(change_amount)
                                break
                            except ValueError:
                                change_amount = input("\nPlease enter the amount for this task"
                                                      "\n>>>")

                        update += f"{taskNum[-1]}. {change}: {change_amount}\n"

                        try:
                            sub = taskNum[-2]
                        except IndexError:
                            sub = taskNum[-1]

                        taskNum.pop()

                        total += change_amount

                        x = 0
                        temp = ''
                        for y in task:
                            if y == ":" or x > 0:
                                x += 1
                                temp += y
                        temp = temp.replace(":", "").replace(" ", "")

                        try:
                            temp = int(temp)
                            total -= temp

                        except ValueError:
                            print("\nSomething went wrong with the calculation.."
                                  "\nYou may have to re-enter your tasks")
                            Task_Manager(task_file)

                    else:
                        if counting > 3:
                            update += task

                except IndexError:
                    sub = count - sub

                    update += task
                    while sub != 0:
                        update += file.readline()
                        sub -= 1

                    input("\nAlright, that does it for the task section."
                          "\nPress Enter to continue")
                    break

            file.close()

            if goal < total:

                happy = input(f"\nYour Point Goal is: {goal}"
                              f"\nThis is {total - goal} points away from your Total Task Points ({total})"
                              f"\nAre you satisfied with the current goal?"
                              f"\n1. Yes (Keep Goal)"
                              f"\n2. No  (Change Goal)"
                              f"\n>>>")
                while True:
                    try:
                        happy = int(happy)
                        if 0 < happy < 3:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        happy = input("\nEnter 1 if you would like to {} this goal".format(bold('keep')) +
                                      f"\nEnter 2 if you would like to {bold('change')} this goal"
                                      f"\n>>>")
            else:
                print(f"\nLooks like your Point Goal is above your new Total Task Point by {goal - total} points"
                      f"\nYou will need to change it")
                # s(2)
                happy = 2

            if happy == 1:
                input("\nOkay, your current goal will remain the same"
                      "\nPress Enter to continue")

            elif happy == 2:
                goal = input("\nWhat do you want your new Point Goal to be?"
                             "\n>>>")
                while True:
                    try:
                        goal = int(goal)
                        if 0 < goal < total:
                            break
                        else:
                            raise ValueError

                    except ValueError:
                        goal = input("Enter a number between 0 and {}".format(total) +
                                     "\n>>>")

            update = f"{prize}" \
                     f"Point Goal: {goal}" \
                     f"\nTotal Task Points: {total}" \
                     f"\n{update}"
            print(f'\n{bold("This is your new task file:")}\n' +
                  update)
            input("Press Enter To Continue\n")
            file = open(task_file, "w")
            file.write(update)
            file.close()
            break

        # Adding Tasks to the file
        elif menu == 3:
            print("Work In Progress")
            # open the file and read the values to a variable
            # show the current tasks and keep a variable of how many there are
            # ask how many to add and the value
            # replace the '#' with the newly created tasks followed by another '#'
            update = ""
            count = 1

            print("\nThese are your current tasks:\n")
            files = open(task_file)
            prize = files.readline().strip()
            goal = int(files.readline()[12:].strip())
            total = int(files.readline()[19:].strip())
            files.readline()

            for file in files.readlines():
                if Search("#", file):
                    break
                print(f"{file.strip()}")
                update += file
                count += 1
            files.close()

            add = input("\nHow many more tasks would you like to add to your file?"
                        "\n>>>")
            while True:
                try:
                    add = int(add)
                    break
                except ValueError:
                    add = input(f"Enter the {bold('number')} of tasks you would like to add to your list"
                                "\n>>>")

            for i in range(0, add):
                if i == 0 and 1 == add:
                    task = input(f"\nWhat is the {bold('new')} task you wish to add?"
                                 "\n>>>").capitalize()
                elif i == 0 and 1 < add:
                    task = input(f"\nWhat is the {bold('first')} task you wish to add?"
                                 "\n>>>").capitalize()
                else:
                    task = input(f"\nWhat is the {bold('next')} task you wish to add?"
                                 "\n>>>").capitalize()

                value = input(f"\nWhat is the {bold('value')} of this new task?"
                              "\n>>>")
                while True:
                    try:
                        value = int(value)
                        total += value
                        break
                    except ValueError:
                        value = input(f"Please enter a {bold('number')}"
                                      f"\n>>>")

                update += f"{count}. {task.replace(':', '~')}: {value}\n"

            new = input(f"\nYour current Point Goal is: {goal}"
                            f"\nYour new Total Task Points is: {total}"
                            f"\nWould you like to change your Point Goal?"
                            f"\n"
                            f"\n1. Yes"
                            f"\n2. No"
                            f"\n>>>")
            while True:
                try:
                    new = int(new)

                    if new == 1:
                        newGoal = input("\nWhat would you like to change your Point Goal to?"
                                        "\n>>>")

                        while True:
                            try:
                                newGoal = int(newGoal)
                                if 0 < newGoal <= total:
                                    goal = newGoal
                                    break
                                else:
                                    raise ValueError

                            except ValueError:
                                newGoal = input(f"\nPlease enter a {bold('number')} between 0 and {total}"
                                                f"\n>>>")

                        break

                    elif new == 2:
                        print("\nOkay, moving on")
                        break

                    else:
                        raise ValueError

                except ValueError:
                    new = input("Please enter:"
                                f"\n{bold('1')} if you would like you change your Point Goal"
                                f"\n{bold('2')} if you would like to keep your current Point Goal")

            update = f"{prize}" \
                     f"\nPoint Goal: {goal}" \
                     f"\nTotal Task Points: {total}" \
                     f"\n{update}"

            print('\nAnd this is what your file looks like at the moment:'
                  '\n\n' + update)

            file = open(task_file, 'w')
            file.write(update + "#")
            file.close()

        # Deleting Tasks from file
        elif menu == 4:
            print("Work In Progress")
            # show the user the tasks and keep a variable of the number of tasks
            # ask the user how many tasks they want to delete
            # store the numbers in a list, the sort and reverse the list for popping
            # have a 2 global counters (both -4 default: count & counters) to keep track of the line number while it iterates,
            #  as well as a means of reseting the task numbers:
            #  each time the loop goes check if the line equals the desired removal
            #   and if the number is equal, the counter will not increase #

            count = 0
            lineNum = 1
            new_count = 1

            files = open(task_file)
            prize = files.readline().strip()
            goal = int(files.readline()[12:].strip())
            total = int(files.readline()[19:].strip())
            files.readline()

            print("\nThese are your current tasks:\n")
            for file in files.readlines():
                if Search("#", file.strip()):
                    break
                count += 1
                print(f"{file.strip()}")
            files.close()

            print(count)

            delete = input("\nHow many of these tasks would you like to remove?"
                           "\n>>>")

            while True:
                try:
                    delete = int(delete)
                    if 0 < delete < count:
                        break
                    else:
                        raise ValueError

                except ValueError:
                    delete = input(f"\nOf the {count} tasks you have, how many do you wish to delete?"
                                   f"\n>>>")

            deleting = []

            for i in range(0, delete):
                while True:
                    if i == 0 and 1 == delete:
                        number = input(f"\nWhat is the {bold('number')} of the task you wish to delete?"
                                       "\n>>>")
                    elif i == 0 and 1 < delete:
                        number = input(f"\nWhat is the {bold('number')} of the {bold('first')} task you wish to delete?"
                                       "\n>>>")
                    elif 1 < delete and i == (delete - 1):
                        number = input(f"\nWhat is the {bold('number')} of the {bold('last')} task you wish to delete?"
                                       "\n>>>")
                    else:
                        number = input(f"\nWhat is the {bold('number')} of the {bold('next')} task you wish to delete?"
                                       "\n>>>")

                    try:
                        number = int(number)
                        if 0 < number <= count and number not in deleting:
                            deleting.append(number)
                            break
                        if number in deleting:
                            raise ZeroDivisionError
                        else:
                            raise ValueError

                    except ValueError:
                        print(f"\nPlease enter a {bold('number')} between {bold('0')} and your total tasks {bold('')}"
                              f"\nTry again"
                              f"\n")

                    except ZeroDivisionError:
                        print(f"\nThe number you just entered: {bold(number)}, has {bold('already')} been entered"
                              f"\nTry again"
                              f"\n")

            deleting.sort()
            deleting.reverse()

            files = open(task_file)
            for i in range(0, 4):
                files.readline()

            update = ''
            sub = ''
            done = False
            for file in files.readlines():
                if done is True:
                    if Search("#", file):
                        break
                    update += f"{new_count}. {file[(int(len(str(lineNum))) + 2):].strip()}\n"
                    new_count += 1
                    lineNum += 1

                elif deleting[-1] == lineNum:
                    deleting.pop()
                    val = 0
                    for value in file:
                        if value == ':' or 0 < val:
                            sub += value
                            val += 1
                    sub = int(sub.replace(":", "").strip())
                    total -= sub
                    sub = ''

                else:
                    update += f"{new_count}. {file[(int(len(str(lineNum))) + 2):].strip()}\n"
                    new_count += 1

                try:
                    done = deleting[-1] + 0
                except IndexError:
                    done = True

                lineNum += 1

            files.close()

            print(f"\nThe desired tasks have been deleted"
                  f"\nYour Total Task Points has been reduced to {bold(total)}")

            if goal > total:
                newGoal = input(f"\nAnd as it stands now, your current Point Goal is {bold(goal)}"
                                f"\nYou must enter a new Point Goal to continue"
                                f"\n>>>")
                while True:
                    try:
                        goal = int(newGoal)
                        if 0 < goal <= total:
                            break
                        else:
                            raise ValueError

                    except ValueError:
                        newGoal = input(f"\nPlease enter a {bold('number')} between {bold('0')} and your Total Task Points of {bold(total)}"
                                        "\n")

            else:
                new = input(f"\nYour current Point Goal is still below this new total, sitting at {bold(goal)}"
                            "\nWould you like to change it?"
                            "\n"
                            "\n1. Yes"
                            "\n2. No"
                            "\n>>>")

                while True:
                    try:
                        new = int(new)

                        if new == 1:
                            newGoal = input("\nWhat would you like to change your Point Goal to?"
                                            "\n>>>")

                            while True:
                                try:
                                    goal = int(newGoal)
                                    if 0 < goal <= total:
                                        break
                                    else:
                                        raise ValueError

                                except ValueError:
                                    newGoal = input(f"\nPlease enter a {bold('number')} between 0 and {total}"
                                                    f"\n>>>")

                            break

                        elif new == 2:
                            print("\nOkay, moving on")
                            break

                        else:
                            raise ValueError

                    except ValueError:
                        new = input("Please enter:"
                                    f"\n{bold('1')} if you would like you change your Point Goal"
                                    f"\n{bold('2')} if you would like to keep your current Point Goal")

            update = f"{prize}" \
                     f"\nPoint Goal: {goal}" \
                     f"\nTotal Task Points: {total}" \
                     f"\n" \
                     f"\n{update}" \
                     f"#"

            print("\nThis is what your file looks like at the moment:"
                  "\n\n" + update)

            file = open(task_file, 'w')
            file.write(update)
            file.close()

        elif menu == 5:  # The task file will be read to display the goal and prize
                         # They can then set a new goal and prize for themselves
                         # The variable will then save the rest of the text in the file
            print("Update Goal and Prize")
            update = ''
            total = 0
            file = open(task_file)
            for pGT in range(1, 4):

                if pGT == 1:
                    print("Your current Prize is: {}".format(file.readline()[7:]).strip())
                elif pGT == 2:
                    print(f"Your current Point Goal is: {file.readline()[12:].strip()}")
                elif pGT == 3:
                    total = int(file.readline()[19:].strip())
                    print(f"Your current Total Task Points are: {total}")

            file.close()

            prize = input("\nWhat is your new Prize going to be?"
                          "\n>>>").capitalize()

            goal = input("\nOkay and of the {} points, what is will be your new point goal".format(total) +
                         "\n>>>")

            while True:
                try:
                    goal = int(goal)
                    if 0 < goal < total:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    goal = input("Enter a number for your goal that is between 0 and {} points".format(total) +
                                 "\n>>>")

            count = 1
            file = open(task_file)
            for task in file.readlines():
                if count == 1:
                    update = "Prize: " + prize
                elif count == 2:
                    update += f"\nPoint Goal:{goal}\n"
                elif count > 2:
                    update += task
                count += 1
            file.close()
            file = open(task_file, 'w')
            file.write(update)
            file.close()

         # A while loop will continue to ask the user these questions:
          # What task do you want to add
          # How many points is it worth?
          # Do you want to add another task?
         # Asks for the goal and the prize
        elif menu == 6:
            print("Create Tasks")

            newTasks = ''
            totalTaskPoints = 0
            numOfTask = 1
            endings = ['st', 'nd', 'rd', 'th']
            end = ''
            while True:
                if '3' < str(numOfTask)[-1] < '9' or 11 <= numOfTask <= 20 or str(numOfTask)[-1] == '0':
                    end = endings[3]

                elif str(numOfTask)[-1] == '1':
                    end = endings[0]

                elif str(numOfTask)[-1] == '2':
                    end = endings[1]

                elif str(numOfTask)[-1] == '3':
                    end = endings[2]

                taskName = input(f"\nWhat is the {numOfTask}{end} task you want to add?"
                                 f"\n(Any ':' characters will be replaced with '~')"
                                 f"\n>>>").strip().replace(":", "~").capitalize()

                taskPoints = input("\nHow many points is it worth?"
                                   "\n>>>")
                while True:
                    try:
                        taskPoints = int(taskPoints)
                        break
                    except ValueError:
                        taskPoints = input("\nHow many {} is this task worth".format(bold('numeric points')) +
                                           "\n>>>")
                totalTaskPoints += taskPoints

                newTasks += f'\n{numOfTask}. {taskName}: {taskPoints}'

                numOfTask += 1

                another = input("\nDo you want to add another task?"
                                "\n1. Yes"
                                "\n2. No"
                                "\n>>>")

                while True:
                    try:
                        another = int(another)
                        if 0 < another < 3:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        another = input(f"\nEnter {bold('1')}"
                                        f"or {bold('2')}"
                                        f"\n>>>")

                if another == 2:
                    break

            print(f"\nOkay, give me a second to calculate your total points")
            waiting(3)
            newGoal = int(totalTaskPoints * .75)
            goal = input(f"\nYour total task points amount to: {totalTaskPoints}"
                         f"\nThe default goal to reach is 75% of that: {newGoal}"
                         f"\nWould you like to keep this as your goal or change it?"
                         f"\n1. Keep"
                         f"\n2. Change"
                         f"\n>>>")

            while True:
                try:
                    goal = int(goal)
                    if 0 < goal < 3:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    goal = input(f"\nEnter {bold('1')} to Keep"
                                 f" and {bold('2')} to Change")
            if goal == 1:
                goal = newGoal
            elif goal == 2:
                goal = input(f"\nOf the {totalTaskPoints} points, what do you want your goal to be?"
                             f"\n>>>")
                while True:
                    try:
                        goal = int(goal)
                        if 0 < goal <= totalTaskPoints:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        goal = input("\nEnter a number {} than 0, but {} that the {} point max".format(bold('greater'),
                                                                                                       bold('less'), totalTaskPoints) +
                                     "\n>>>")

            prize = input("\nWhat is the incentive?"
                          "\nWhat are you working to get as a reward for completing these tasks"
                          "\n>>>").strip()

            newTasks = f"Prize: {prize}" \
                       f"\nPoint Goal: {goal}" \
                       f"\nTotal Task Points: {totalTaskPoints}" \
                       f"\n{newTasks}" \
                       f"\n#"

            file = open(task_file, 'w')
            file.write(newTasks)
            file.close()

            print(f"\nThis is what your Task file looks like at the moment:\n"
                  f"\n{newTasks}")

            print("_" * 50 +
                  "\nYou will now be taken back to the {}".format(bold("Task Menu")) +
                  "\nIf you want to {} the contents of this file you can do so there".format(bold("edit")))

            return Task_Manager(task_file)

        elif menu == 7:
            return True

        if menu == 2 or menu == 3 or menu == 4 or menu == 6:
            resetMain(file_name)
            print("\nYour User File has now been reset"
                  "\nNow taking you beck to the Task Menu")
