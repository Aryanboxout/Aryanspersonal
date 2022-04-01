
from week0 import swap
from week0 import ship
from week0 import pattern
from week1 import data
from week1 import fib
from week2 import factorial
from lcm import *
from week2 import Palindrome


# Main list of [Prompts, Actions]
# Two styles are supported3

# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
   ["swap", "week0/swap.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0sub_menu = [
    ["Swap", "week0/swap.py"],
    ["Pattern", "week0/pattern.py"],
    ["Fun Math", "week0/ship.py"]
]

week1sub_menu = [
    ["Data", "week1/data.py"],
    ["Fib", "week1/fib.py"]
]

week2sub_menu = [
    ["Factorial", "week2/factorial.py"],
    ["Palindrome", "week2/Palindrome.py"],
    ["Least Commmon Factor", "lcm.py"]
]



# Menu banner is typically defined by menu owner
border = "" * 25
banner = f"\n{border}\n Select Option\n{border}"


def menu():
    title = "Aryan's menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["week 0",week0submenu])
    menu_list.append(["week 1",week1submenu])
    menu_list.append(["week 2",week2submenu])
    buildMenu(title, menu_list)

def week0submenu():
    title = "Week0" + banner
    buildMenu(title, week0sub_menu)
def week1submenu():
    title = "Week1" + banner
    buildMenu(title, week1sub_menu)
def week2submenu():
    title = "Week2" + banner
    buildMenu(title, week2sub_menu)


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
