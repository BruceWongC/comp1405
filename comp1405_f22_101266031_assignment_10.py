# Bruce Wong
# 101266031
# comp1405_f22_101266031_assignment_10.py

import pygame

pygame.init()


areas = [
"bedroom",
"office",
"living room",
"backyard","basement",
"frontyard",
"garage",
"furnace room",
"neighbor",
"sidewalk",
"patch of grass",
"gas station",
"recreation center",
"tech buildings",
"parking lot",
"park",
"beach",
"ocean",
"shopping mall",
"bank"
] # areas that can go

area_desc = [
"You are in your bedroom. It contains a bed that's in a complete mess with your graduation certificate on the wall. You can go to the office or living room",
"You are in your office. It holds your computer and the windows are left open, letting in the cool breeze. You can go to the bedroom",
"You are in the living room. The 2 couches are perpendicular to each other and a remote is laying on the coffee table. You can go to the bedroom, backyard, kitchen or frontyard",
"You are in the backyard. The small rectangular patch of dirt houses a few plants that aren't ready to harvest yet. You can go to the living room",
"You are in the basement. A ping pong table sits next to the punching dumb. It has boxs of items under it, left as storage. You can go to the living room, or furnace room",
"You are in the frontyard. A garden of flowers is place in the middle holding many different kinds of flowers. You can go to the living room, garage, neighbor, or sidewalk",
"You are in the garage. Your car is place here along with a bike and the garbage you forgot to take out. You can go to the frontyard",
"You are in the furnace room. The room is small with wooden walls on the side, no paint was applied. You can go to the basement",
"You visited your neighbor. Your neighbor has a halloween pumpkin on their porch, they probably forgot to remove it. You can go to the frontyard",
"You are on the sidewalk. Some grass can be seen growing on the sides of it and very small ant are travelling on it. You can go to the frontyard, park, or a patch of grass",
"You are on a patch of grass. This area is owned by Algonquin College. The grass is very tall and a green box can be seen on the right side. You can go to the sidewalk, gas station, or tech buildings",
"You are at the gas station. There is 12 stations for people to use and the car wash is over at the back of the convenience store. You can go to the a patch of grass, recreation center or shopping mall",
"You are at the recreation center. A skateboard area, park and water park is located outside the building. A gym and a massive swimming pool is located inside. You can go to the gas station",
"You are at the tech buildings. Several tech buildings were built here. Many are over 20+ stories tall. You can go to a patch of grass, or parking lot",
"You are in the parking lot. This parking lot can hold an immense amount of cars, a guess can be 300 cars? Many lights are placed around the area as well. You can go to the tech buildings",
"You are at the park. 2 different sections were made. One with sand, the other with a red ground. You can go to the sidewalk, or beach",
"You are at the beach. The place is completely filled with sand. The water is pushing and taking away sediment. Seas shells can be collected. You can go to the park or ocean",
"You are at the ocean. The place is completely open. Just water moving along with the wind. You can go to the beach",
"You are at the shopping mall. Many shops are open, selling different goods like grooceries, coffee and alcohol. Even pumpkins are being sold. You can go to the gas station or bank",
"You are at the bank. 3 people at the the counter while there is a line up of 7 people. Some consultants are privately talking to many people. You can go to the shopping mall"
] # desc

area_list = [[1,2],[0],[0,3,4,5],[2],[2,7],[2,6,8,9],[5],[4],[5],[5,10,15],[9,11,13],[10,12,18],[11],[10,14],[13],[9,16],[15,17],[16],[11,19],[18]] # areas that have access to the places

direction = [["north","west"],["south"],["east","north","south","west"],["south"],["north","south"],["east","north","south","west"],["south"],["north"],["north"],["east","north","south"],["south","north","west"],["south","west","east"],["east"],["east","south"],["north"],["north","south"],["north","west"],["east"],["west","north"],["south"]]
# directions it can go correlating from pos in area_list

items = [] # reqiures to display items here and 3 items, can have statement if user is in areas 4 (if user == areas[4]) ask

index = 0 # location
var = 0
track = False

item1 = True
item2 = True
item3 = True

flag = True

img = pygame.image.load("assignment10map.jpg") # the img of the map

display = pygame.display.set_mode((462,349))

display.blit(img,(0,0))

pygame.display.flip()

while flag:
    print(area_desc[index])
    
    user = input("Which way do you want to go? (type 'exit' to quit): ")
    
    if user == "exit":
        flag = False
        
    elif user == "north":
        for i in direction[index]: # looks for north
            if i == "north":
                var = direction[index].index(i) # get it's index which matches that location
                index = area_list[index][var] # set current index 
                track = True # if this location exists
                
                print()
                                    
                break
                
        if track == False:            
            print("You can't go this direction\n")
        track = False
        

    
    elif user == "east":
        for i in direction[index]:
            if i == "east": # look for south
                var = direction[index].index(i)# get it's index which matches that location
                index = area_list[index][var]# set current index 
                track = True# if this location exists
                
                print()

                
                break
                
        if track == False:            
            print("You can't go this direction\n")
        track = False
            
    elif user == "south":
        for i in direction[index]:
            if i == "south": # look for south
                var = direction[index].index(i)# get it's index which matches that location
                index = area_list[index][var]# set current index 
                track = True# if this location exists
                
                print()

                
                break
                
        if track == False:            
            print("You can't go this direction\n")
        track = False
                    
    elif user == "west":
        for i in direction[index]:
            if i == "west": # look for west
                var = direction[index].index(i)# get it's index which matches that location
                index = area_list[index][var]# set current index 
                track = True# if this location exists
                
                print()

                
                break
                
        if track == False:            
            print("You can't go this direction\n")
        track = False
    
    elif user == "take": # if user takes something
        if index == 2 and item1 == True: # living room
            print("You took the remote\n")
            item1 = False
            items.append("remote")
        
        elif index == 16 and item2 == True: # beach
            print("You picked up a sea shell\n")
            item2 = False
            items.append("sea shell")
   
        elif index == 18 and item3 == True: # shopping mall
            print("You picked up a pumpkin\n")
            item3 = False
            items.append("pumpkin")
        
        else:
            print("There is nothing to take\n")
            
    elif user == "inventory": # prints items and if nothing is there, say no items
        if len(items) != 0:
            print("You have:")
            for i in range(len(items)):
                print(items[i])
            
            print()
        else:
            print("You have no items\n")
                
    else:
        print("Input is not valid\n")