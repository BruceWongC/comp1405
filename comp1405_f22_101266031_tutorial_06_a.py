# Bruce Wong 
# 101266031
# comp1405_f22_101266031_tutorial_06_a.py

# empty list and a counter for contents in list
mylist = []
counter = 0

while True:
	user = str(input("Do you want to add (a), remove last value (r), or quit (q)?: "))
	
	if user == "q": # quit
		break
		
	elif user == "a": # if add, get the user input, append to list and add 1 to counter (as there is 1 more item in)
		value = str(input("Please enter text: "))
		
		mylist.append(value)
		counter += 1
		
	elif len(mylist) == 0: # if r was typed with no contents, don't allow cuz it will bomb
		print("No value to remove\n")
		
	else: # remove last item in list
		mylist.pop(counter)
		counter -= 1
		
print("Length of list is " + str(counter)) # length of list
# print(mylist)