class Test:

    def fact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f
def fact():
    
 n = int(input("Enter a number:"))

 obj = Test()
 f = obj.fact(n)
 print("Factorial is:", f)

if __name__ == "__main__":
   fact()