# Bruce Wong 
# 101266031
# comp 1405
# comp1405_f22_101266031_tutorial_07_a.py

def valid_matrix(mylist):
    if isinstance(mylist, list) == True: # checks if argument is a list
        for i in mylist:
            if isinstance(i, list) == False: # if the items in list is not a list
                return False

        list_len = len(mylist)
            
        for j in range(list_len): # checking row lengths if they are equal
            row_len_1 = len(mylist[j])
            row_len_2 = len(mylist[j + 1])
            if row_len_1 != row_len_2: # if not
                return False
            
            if list_len == (j + 2):# if the next index will go over the list index
                break

        for k in mylist:
            row_len = len(k) # get row length
            for l in range(row_len):
                if not isinstance(k[l], (int, float)): # checking elements of the rows if they aren't int or float
                    return False
                    
        return True
        
    else:
        return False
        
#mylist = [[1,1],[1],[1,1,1]]

#print(valid_matrix(mylist))