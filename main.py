"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Swap 2 numbers' )
    print('2 -- merge 2 numbers' )
    print('3 -- nothing' )
    print('4 -- Exit' )
    runOptions()


# Menu options as a dictio3nary
menu_options = {
    1: 'Swap 2 numbers',
    2: 'merge numbers',
    3: 'nothing',
    4: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def stringy():
    print('You chose \' 1 -  Swap 2 numbers\'')
    x = input("Enter your first value x: ")
    y = input("Enter your second value y: ")
   
    temp = x
    x = y
    y = temp
    print('The value of x after swapping:     {}'.format(x))
    print('The value of y after swapping:  {}'.format(y))
  

# menu option 2
def numby():
    print('You chose \' 2 - Adding\'')
    a = input("Enter first number: ")
    b = input("Enter your second number: ")
    result = a + b
    print("asnwer:", result)
  

   # menu option 3
def listy():
    print('You chose \'3 - here is a fun pattern\'')
        
   

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            # Exit menu    
            elif option == 4:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()