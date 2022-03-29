# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from week0 import swap
from week0 import ship
from week0 import pattern
from week1 import data
from week1 import fib
from week2 import factorial
from week2 import math
from week2 import palindrom




# Main list of [Prompts, Actions]
# Two styles are supported3

# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
   ["swap", swap.swap]  
    
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0 = [
    ["swap", swap.swap],
    ["pattern", pattern.pattern],
    ["Fun Math", ship.ship]
]
week1 = [
    ["Data", "data.py"],
    ["Fib", fib.fibprint],
   
]
week2 = [
    ["Factorial", factorial.fact],
    ["math", math.mathprint],
    ["palindrom", palindrom.palinprint]
]



# Menu banner is typically defined by menu owner
border = "" * 25
banner = f"\n{border}\n Select Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Aryan's menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["week 0",week0()])
    menu_list.append(["week 1",week1()])
    menu_list.append(["week 2",week2()])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def week0():
    title = "Week0" + banner
    buildMenu(title, week0)
def week1():
    title = "Week1" + banner
    buildMenu(title, week1)
def week2():
    title = "Week2" + banner
    buildMenu(title, week2)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
