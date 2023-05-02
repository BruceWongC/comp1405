# Bruce Wong
# student ID: 101266031

# comp1405_f22_101266031_assignment_02.py

import sys
num2 = sys.argv[1] # command-line value
num2 = int(num2) #convert to int

print("please input a number:")
num1 = input() # get input  
num1 = int(num1) #convert to int

num1 **= 2       # square num1
print(num1)

num1 %= 3  # divide num1 by 3 and take remainder   
print(num1)

num1 += num2     # add command line value
print(num1)

num1 += num1 - 1 # double value and -1 
print(num1)

num1 *= 2.896552 # multiply num1 with ~3
print(num1)

num1 = int(num1) # convert to int (line before converted it to float)
num1 = str(num1) # convert to str 

print() # empty space  
print("<", num1, ">") # final result with triangle brackets