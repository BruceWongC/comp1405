# Bruce Wong
# 101266031
# comp1405_f22_101266031_assignment_09.py

def uppercase(x):
    result = ""
    for i in x:
        num = ord(i)
        if num > 96 and num < 123: # checks if the num is lower case then do changes 
            num -= 32
            char = chr(num)
            result += char
        else:
            result += i   
    return result
    
def acronyms(sentence): # splits the line then rejoin with the acronym (spaces in between were from the split)
    mylist = mylist.split("BY THE WAY")
        
    mylist = "BTW".join(mylist)
    
    mylist = mylist.split("OH MY GOD")
    
    mylist = "OMG".join(mylist)
    
    mylist = mylist.split("LAUGHING OUT LOUD")
    
    mylist = "LOL".join(mylist)

    mylist = mylist.split("FOR YOUR INFORMATION")

    mylist = "FYI".join(mylist)
   
    return mylist
    
def homoglyphs(mylist): # splits the line then rejoin with the homoglyph (spaces in between were from the split)
    mylist = mylist.split("A")
        
    mylist = "@".join(mylist)
    
    mylist = mylist.split("C")
    
    mylist = "(".join(mylist)
    
    mylist = mylist.split("E")
    
    mylist = "3".join(mylist)

    mylist = mylist.split("W")

    mylist = "VV".join(mylist)
   
    return mylist

def main():
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' # punctuation to remove
    
    user = input("What sentence do you want to convert?: ")
    
    for i in user: # searches through punctuation and removes all by split then rejoin
        if i in punctuation:
            user = user.split(i)
            user = "".join(user)
            
    
    user_up = uppercase(user)
    
    user_ac = acronyms(user_up)
    
    print(user_ac)
    
    #print(homoglyphs(user_ac))
    
main()