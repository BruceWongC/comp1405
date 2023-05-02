# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_04_b.py

import random

num = random.randint(1,100)

flag = True

guess = 0

while flag == True:
    user = int(input("Guess a number in between 1 to 100 (inclusive): "))
    
    guess += 1 # guesses
    
    if user > num: # check if value is greater, lower or equal to user input, then printing message 
        print("The number is lower")
    elif user < num:
        print("The number is higher")
    else: #kicks you out if answer is correct
        print("You are right! The answer is " + str(num))
        break
    
    if guess == 10: # after 10 guess, kick out and print
        print("You lost. The answer is " + str(num))
        break