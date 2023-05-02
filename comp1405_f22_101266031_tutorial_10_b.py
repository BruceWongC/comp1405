# Bruce Wong
# 101266031
# comp1405_f22_101266031_tutorial_10_b

def non_recursive(mylist):  
    length = len(mylist)
    i = 0

    while i < length:
        if mylist[i] == "a" or mylist[i] == "e" or mylist[i] == "i" or mylist[i] == "o" or mylist[i] == "u":
            var = ord(mylist[i]) - 32 # convert letter to num for ascii
            mylist[i] = chr(var)

        i += 1

    return mylist

def recursive(mylist):
    if not mylist:
        return []

    if mylist[0] == "a" or mylist[0] == "e" or mylist[0] == "i" or mylist[0] == "o" or mylist[0] == "u":
        var = ord(mylist[0]) - 32 # convert letter to num for ascii
        mylist[0] = chr(var)

    return [mylist[0]] + recursive(mylist[1:])

def main():
    mylist = ["a","b","A","e","q"]

    print(non_recursive(mylist))

    mylist = ["s","f","y","e","x","b","i","A"]

    print(recursive(mylist))

main()