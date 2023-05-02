# Bruce Wong 
# 101266031
# comp1405_f22_101266031_tutorial_06_b.py

from random import randint

def str_count(var): 
    counter = 0
    
    for i in range(0, user):
        if mylist[i] == str(var):
            counter += 1
    return counter

mylist = [] 

user = int(input("How many items do you want in the list?: ")) 

for i in range (0, user): # get a list with n random integers of 1-9
    mylist.append(randint(1,9))
    
while True:
    user_int = input("\nType an integer (from 1-9) to replace with a string or type 's' to search for a string (type 'q' to quit): ")
    
    if str(user_int) == "q": # quit
        break
    
    elif str(user_int) == "s": # get string and search for that string using str_count from mylist
        var = str(input("What str do you want to search?: "))
        print(var + " appears " + str(str_count(var)) + " times")
        
    elif int(user_int) > 9 or int(user_int) < 1: # if user input is > 9 or < 1, don't allow as they don't exist in the list
        print("Please enter an integer from 1-9\n")
    
    else: # replace the int with the str if the user input was equal to the contents of list at i
        user_str = str(input("What string do you want to replace it with?: "))

        for i in range (0, user):
            if mylist[i] == int(user_int):
                mylist[i] = user_str
                

# print(mylist)