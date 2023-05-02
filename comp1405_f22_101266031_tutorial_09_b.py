# Bruce Wong
# 101266031
# comp1405_f22_101266031_tutorial_09_b.py

from random import randint
import time

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



def randomlist(num): # make random list of elements
    mylist = []

    for i in range(num):
        value = randint(0,9)

        mylist.append(value)

    return mylist

def main():
    num = 6 # amount of elements in list

    while True:
        avg_time_bogo = 0 # avg times, reset after coming to top

        avg_time_bozo = 0
        
        if num == 12: # only do 11 elements at max, bogo sort is long
            break
        
        for i in range(7): # 7 trials
            # bogo
            mylist = randomlist(num) # make a random list
            
            time_s = time.time()
            Bogosorting(mylist)
            time_e = time.time()

            final_time = time_e - time_s

            avg_time_bogo += final_time 

            # bozo
            mylist = randomlist(num)
            
            time_s = time.time()
            Bozosorting(mylist)
            time_e = time.time()

            final_time = time_e - time_s

            avg_time_bozo += final_time 

        avg_time_bogo = avg_time_bogo/7

        avg_time_bozo = avg_time_bozo/7

        print("Avg time for bogo sort:" , avg_time_bogo , "for" , num , "elements") 
        
        print("Avg time for bozo sort:" , avg_time_bozo , "for" , num , "elements\n") 

        num += 1 # increase amount of elements of list
main()