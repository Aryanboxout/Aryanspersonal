#Defining fibonacci
def Fibonacci(x):
  
    if x == 0:
        return 0
 
    
    elif x == 1 or x == 2:
        return 1
 
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)

      
def tester():
  try:
      
    num = int(input("Fibonacci: "))
  
    if num < 0:
        print("No there is no negative for fibonacci")
    else:
        # print("The fibonacci of", num, "is",     Fibonacci(num))
      for i in range (0,num):
        print(Fibonacci(i))

  except ValueError:
   print("That value cannot be processed")
  
def fibprint():
  Fibonacci(7)     
  tester()
if __name__ == "__main__":
    fibprint()
