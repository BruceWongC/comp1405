# Bruce Wong 
# 101266031
# comp 1405
# comp1405_f22_101266031_tutorial_07_b.py

def matrix_sum(mylist_1, mylist_2):
    sum_list = [] #the return list and empty list
    
    length_1 = len(mylist_1)
    length_2 = len(mylist_2)
    
    if length_1 == length_2: # if the col are the same        
        for i in mylist_1:
            for j in mylist_2:
                if len(i) != len(j): # if the rows aren't the same
                    return sum_list   
        
    else:
        return sum_list
    
    col = length_1 
    row = len(i)
    
    for i in range(col):
        a_list = [] # list to append to sum_list
        for j in range(row):
            a_list.append(mylist_1[i][j] + mylist_2[i][j])
        sum_list.append(a_list)
        
    return sum_list
        



#mylist1 = [[5,3,1],[2,7,8]]
#mylist2 = [[5,3,1],[2,7,9]]

#print(matrix_sum(mylist1, mylist2))
