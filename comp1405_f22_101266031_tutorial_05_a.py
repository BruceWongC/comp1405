# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_05_a.py

def calculator(x):
    if x == 1: # not prime by google
        return False
        
    for i in range (2, x):
        result = x % i
        if result == 0 and x != i:
            return False
    return True
    

flag = True
 
while flag == True:
    user = input("Please enter an integer, to quit type 'q': ")
    
    if user == "q":
        quit()
    else: # under the assumption that the value will always be valid
        num = int(user)
        
    ans = calculator(num)    
    
    if ans == True:
        print(user + " is a prime number!\n")
    else:
        print(user + " is not a prime number!\n")
