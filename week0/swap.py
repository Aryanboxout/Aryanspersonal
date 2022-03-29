def swap():
   print('You chose \' 1 -  Swap 2 numbers\'')
   x = input("Enter your first value x: ")
   y = input("Enter your second value y: ")
   
   temp = x
   x = y
   y = temp
   print('The value of x after swapping:     {}'.format(x))
   print('The value of y after swapping:  {}'.format(y))


if __name__ == "__main__":
    swap()