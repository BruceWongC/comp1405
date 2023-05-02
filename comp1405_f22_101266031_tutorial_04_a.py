# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_04_a.py

flag = True

while flag == True:
    num = int(input("Please enter an integer in between 1-9 (inclusive): "))
    
    if num > 0 and num < 10: # make sure "num" can only be values 1-9 (inclusive)
        break
                  
x = 0
    
for i in range(0, num): # to loop amount of rows
    text = "" # in loop to reset for next row       
    x += 1 # counter for amount in row
    for j in range (0, x):
        text += str(x) # concatenate string to get correct amount in row then print after loop finishes
    print(text)