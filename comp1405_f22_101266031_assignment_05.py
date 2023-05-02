# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_assignment_05.py 

import pygame
import sys
import random

pygame.init()

img_give = sys.argv[1] # get file

img = pygame.image.load(img_give) 

#Get x and y values
x = img.get_width() 
y = img.get_height()


#up scaling x and y by 5 for display
x_up = x * 5 
y_up = y * 5

display = pygame.display.set_mode((x_up,y_up))

display.fill((255, 255, 255))

for i in range (0,x): # look for pixel
    for j in range (0,y): 
        (r, g, b, a) = img.get_at((i,j)) # get pixel

        #Get the amount of color and use that to determine the randomness of the art (ratio of r, g and b)
        if r != 0 and b != 0 and g != 0: #Make sure 0/0 doesn't happen
            r_percent = (r / (r + b + g + a)) * 100 #Perecent value of rgb (how much is in the sum)
            g_percent = (g / (r + b + g + a)) * 100
            b_percent = (b / (r + b + g + a)) * 100
            a_percent = (a / (r + b + g + a)) * 100
     
            # x and y coordinates for the pixels in 5x5
            i_min = i * 5 # lower and higher bounds for range function
            i_max = i * 5 + 5
            
            j_min = j * 5
            j_max = j * 5 + 5
                        
            # print the upscaled pixel            
            for a in range (i_min, i_max): 
                for b in range (j_min, j_max): 

                    chance = int(random.randint(1,100))

                    if chance > 0 and chance < r_percent: # draws rect if it hits within the ranges (also, the rates are ~ < 1 lower because of float values in percent, which shouldn't matter much)
                        pygame.draw.rect(display, (255, 0, 0), (a, b, 1, 1))
                        
                    elif chance > r_percent and chance < (r_percent + g_percent):
                        pygame.draw.rect(display, (0, 255, 0), (a, b, 1, 1))

                    elif chance > (r_percent + g_percent) and chance < (r_percent + g_percent + b_percent):
                        pygame.draw.rect(display, (0, 0, 255), (a, b, 1, 1))    
                        
                    elif chance > (r_percent + g_percent + b_percent) and chance <= 100:
                        pygame.draw.rect(display, (0, 0, 0), (a, b, 1, 1))

        else: #If the pixel is (0,0,0), make pixel black
            i_min = i * 5
            i_max = i * 5 + 5
            
            j_min = j * 5
            j_max = j * 5 + 5
                        
            for a in range (i_min, i_max):
                for b in range (j_min, j_max): # print only black on ( 0, 0, 0) pixels
                    pygame.draw.rect(display, (0, 0, 0), (a, b, 1, 1))
                    
pygame.display.flip()

flag = True 

while flag: # loops the display and pauses the screen as it's looking for the window to close
    for p in pygame.event.get():
        if (p.type == pygame.QUIT): # if pyagme quits display = false and closes loop
            flag = False
    
pygame.image.save(display,"assgn5.png") #mostly to look back at the image for myself
pygame.quit()    
