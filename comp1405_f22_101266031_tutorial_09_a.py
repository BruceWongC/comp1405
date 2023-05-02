# Bruce Wong
# 101266031
# comp1405_f22_101266031_tutorial_09_a.py

#ask if checks are need. If items are in list

from random import randint

def is_sort(mylist):
    length = len(mylist) # get len

    if length == 1:
        return True

    for i in range(length-1): # go through list
        if mylist[i] > mylist[i + 1]: # check if previous num is greater than next
            return False
    return True

def Bogosorting(mylist):

    list_length = len(mylist)

    mylist_copy = mylist[:] # get copy

    while not is_sort(mylist):
        mylist.clear() # remove elements

        mylist.append(mylist_copy[0])# need at least 1 item before appending

        for i in range(1, list_length):
            length = len(mylist)

            num = randint(0, length)

            mylist.insert(num, mylist_copy[i]) # put items in a random index 

def Bozosorting(mylist):

    length = len(mylist)

    while not is_sort(mylist):
        num1 = randint(0, length - 1) 

        while True:

            num2 = randint(0, length - 1) # could be the same number

            if num1 != num2: # if the random nums are equal
                break

        # switch value 1 with value 2 and value 2 with value 1
        value1 = mylist[num1]

        value2 = mylist[num2]

        mylist[num1] = value2

        mylist[num2] = value1 


def main():

    mylist1 = [8,9,5,4,8]

    Bogosorting(mylist1)

    print("Bogo sort")
    print(mylist1)
    print()

    mylist2 = [1,8,4,4,9]

    Bogosorting(mylist2)

    print("Bozo sort")
    print(mylist2)


main()