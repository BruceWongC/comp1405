# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_05_b.py

from random import randint 

def game(x):
    comp = randint(1,3) # 1 rock, 2 paper, 3 scissors
    
    op = 0
    
    if comp == 1: # get str for end
        var = "rock"
        
    elif comp == 2:
        var = "paper"
        
    else:
        var = "scissors"

    # comparisons
    if x == "r": 
        if comp == 1:
            op = 3
        elif comp == 2:
            op = 2
        else:
            op = 1
            
    elif x == "p":
        if comp == 1:
            op = 1
        elif comp == 2:
            op = 3
        else:
            op = 2
               
    else:
        if comp == 1:
            op = 2
        elif comp == 2:
            op = 1
        else:
            op = 3
            
    # printing output        
    if op == 1: # win
        print("\nYou won! The computer chose " + var)
        
    elif op == 2: # lose
        print("\nYou lost! The computer chose " + var)
        
    else: # tie
        print("\nYou tied! The computer chose " + var)



def main():
    flag = True
    while flag:
        user = input("What do you choose? Rock (r), paper (p) or scissors (s)? Type 'q' to quit: ")
        if user == "q": # quit
            quit()
        
        elif user == "r" or user == "p" or user == "s": #inputs r, p, and s are easier to operate program
            game(user)
         
        else:
            print("\nPlease put use a valid input")
            
main()