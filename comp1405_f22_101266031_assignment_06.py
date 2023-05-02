# Bruce Wong
# STD ID: 101266031	
# comp1405_f22_101266031_assignment_06.py

import pygame
import random

display = pygame.display.set_mode((600, 700))

pygame.display.flip() # display the window

b = (0,0,0) # colours for board
w = (255,255,255)
tile_colour = b

p1_total = 0   # dice totals
p2_total = 0

place_x_p1 = 0 # inital cords for players
place_y_p1 = 0
place_x_p2 = 0
place_y_p2 = 50

counter = 0 # counter to take turns

flag = True 
start1 = False
start2 = False

while flag: 
    for p in pygame.event.get(): # if the user closes the window
        if (p.type == pygame.QUIT): 
            flag = False
            
    for i in range (0, 600, 100): # checker board for game
        for j in range (0, 700, 100):
            pygame.draw.rect(display, tile_colour, (i, j, 100, 100))
           
            if tile_colour == b: # switch colours for the pattern
                tile_colour = w
            else:
                tile_colour = b
    
    
    if (counter % 2) == 0: # even turn, player 1

        if start1 == True: # start the movement of the squares    
            diceroll_1 = random.randint(1,6) + random.randint(1,6)

            print("Red Dice Value: " + str(diceroll_1)) 

            p1_total += diceroll_1            
            
            if p1_total <= 41: # wihin range
                row = p1_total // 6
                
                if p1_total == p2_total: # sets player 1 to beginning and the total to 0 if the block lands on a tile with another on it
                    place_x_p1 = 0
                    place_y_p1 = 0   
                    p1_total = 0
                
                else:
                    if (row % 2) == 0: # to deal with the snaking movement of the game, even row goes left to right, odd rows go right to left
                        place_x_p1 = (p1_total - row * 6) * 100

                    else:
                        place_x_p1 = 500 - (p1_total - row * 6) * 100
                    
                    place_y_p1 = row * 100
                        
                pygame.draw.rect(display, (255,0,0),(place_x_p1,place_y_p1,50,50))
                pygame.draw.rect(display, (0,255,0),(place_x_p2,place_y_p2,50,50))

                pygame.display.update()
                pygame.time.delay(2000)    

                if p1_total == 41: # reaches end, exit window
                    pygame.time.delay(5000)    
                    exit()
                    
            elif p1_total > 41: # if goes over the end, go back to the start
                place_x_p1 = 0
                place_y_p1 = 0
                pygame.draw.rect(display, (255,0,0),(place_x_p1,place_y_p1,50,50))
                pygame.draw.rect(display, (0,255,0),(place_x_p2,place_y_p2,50,50))

                pygame.display.update()
                pygame.time.delay(2000)   

                p1_total = 0 # reset the total as the block starts back at the beginning
                
        else: # start the beginning of the game with the blocks at the start
            pygame.draw.rect(display, (255,0,0),(place_x_p1,place_y_p1,50,50))
            pygame.draw.rect(display, (0,255,0),(place_x_p2,place_y_p2,50,50))

            pygame.display.update()
            pygame.time.delay(1000)   
            start1 = True # begins program

        
    if (counter % 2) == 1: # odd number, player 2 turn
    
        if start2 == True: #start the movement
            diceroll_2 = random.randint(1,6) + random.randint(1,6)

            print("Green Dice Value: " + str(diceroll_2))  
            
            p2_total += diceroll_2

            if p2_total <= 41: # within in range
                row = p2_total // 6

                if p2_total == p1_total: # if the block ends on the same tile, go back to start
                    place_x_p2 = 0
                    place_y_p2 = 50     
                    p2_total = 0                

                else:
                    if (row % 2) == 0: # math to deal with the snaking format
                        place_x_p2 = (p2_total - row * 6) * 100

                    else:
                        place_x_p2 = 500 - (p2_total - row * 6) * 100
                    
                    place_y_p2 = row * 100 + 50 # add 50 to be on a different half of the row
                
                
                        
                pygame.draw.rect(display, (255,0,0),(place_x_p1,place_y_p1,50,50))
                pygame.draw.rect(display, (0,255,0),(place_x_p2,place_y_p2,50,50))
                
                pygame.display.update()
                pygame.time.delay(2000)   
                
                if p2_total == 41: # if square lands on last tile, end
                    pygame.time.delay(5000)   
                    exit()


            elif p2_total > 41: # goes over end tile, go to start
                place_x_p2 = 0
                place_y_p2 = 50
                pygame.draw.rect(display, (255,0,0),(place_x_p1,place_y_p1,50,50))
                pygame.draw.rect(display, (0,255,0),(place_x_p2,place_y_p2,50,50))
                
                pygame.display.update()
                pygame.time.delay(2000)   
                
                p2_total = 0 # reset total
        else: # to set the squares at the beginning
            pygame.draw.rect(display, (255,0,0),(place_x_p1,place_y_p1,50,50))
            pygame.draw.rect(display, (0,255,0),(place_x_p2,place_y_p2,50,50))
                
            pygame.display.update()
            pygame.time.delay(1000)  
            start2 = True
    
    counter += 1 # the counter/turns
        

