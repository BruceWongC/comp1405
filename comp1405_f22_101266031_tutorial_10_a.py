# Bruce Wong
# 101266031
# comp1405_f22_101266031_tutorial_10_a.py

def non_recursive(mylist):  
    length = len(mylist)
    i = 0

    while i < length: # when i = length, loop reached the end of the list
        if mylist[i] % 2 == 1:
            mylist[i] += 10

        i += 1

    return mylist

def recursive(mylist):
    if not mylist: 
        return []

    if mylist[0] % 2 == 1:
        mylist[0] += 10
    return [mylist[0]] + recursive(mylist[1:]) 

def main():
    mylist = [1,2,5,7,8,76,2,5,4,3,2]

    print(non_recursive(mylist))

    mylist = [4,5,7,8,76,54,3,2,34,567]

    print(recursive(mylist))

main()