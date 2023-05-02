# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_assignment_07.py

import pygame
import sys

# This program works by inverting the area you move your cursor on. Also allows right angle triangles after moving in a different direction from the initial direction

def difference(a, b):
    if a >= b:
        result = a - b
    else:
        result = b - a
    return result

def corner(a, b):
    if a >= b:
        result = b 
    else:
        result = a 
    return result


pygame.init()

img_give = sys.argv[1] # get file

img = pygame.image.load(img_give) 

w = img.get_width() 
h = img.get_height()

display = pygame.display.set_mode((w,h))

background = pygame.Surface((w,h))

for i in range(0, w): # create the bg
    for j in range(0, h):
        r, g, b, _ = img.get_at((i, j))
        pygame.draw.rect(background,(r,g,b),(i, j, 1, 1))

display.blit(background, (0,0)) #img blited

pygame.display.flip()

flag = True

#init variables
start_x = 0 # cords of the first pixel clicked
start_y = 0

final_x = 0 # cords of final
final_y = 0

count = False

x = 0
y = 0


while flag: 
    for p in pygame.event.get(): # if the user closes the window
        if (p.type == pygame.QUIT): 
            flag = False
        
    left,_,_ = pygame.mouse.get_pressed()    
       
    if left == False: # if left click is never clicked, don't collect start pos
        count = False
        
    if left == True:
        if count == False:
            start_x, start_y = pygame.mouse.get_pos() # get the position of the mouse at the start
            count = True # don't go into this again
        current_x, current_y = pygame.mouse.get_pos()
        
        dist_x = difference(start_x, current_x) # the w and h of the area being inverted
        dist_y = difference(start_y, current_y) 
        
        for a in range(0, dist_x): # inverts area
            for b in range(0, dist_y):                
                x = corner(start_x, current_x) + a
                y = corner(start_y, current_y) + b
                r, g, b, _ = img.get_at((x, y))
                
                #invert colours
                if r >= 0: # keep the inverted colours inverted, also I don't know what happens when rgb are in negative int
                    r = 255 - r
                
                if g >= 0:
                    g = 255 - g
                
                if b >= 0:
                    b = 255 - b
                
                display.set_at((x,y),(r, g, b)) # change the pixel colour to inverted
        
        pygame.display.update()

