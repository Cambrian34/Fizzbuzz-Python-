"""
The given code solves the FizzBuzz problem and uses the words "Fizz" and "Buzz". 
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, prints "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, output "FizzBuzz". 

"""

n = int(input("Input:"))

for x in range(1, n):
    
    if x % 3 == 0 and x % 5 == 0:
        print("Fizzbuzz")
        
    elif (x % 3 == 0): ##and x%2 != 0):
        print("Fizz")
    
    elif (x % 5 == 0 ): ## and x%2 != 0):
        print("Buzz")
        
    else:
        ##if(x%2 != 0):
        print(x)
        ##continue