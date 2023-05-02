# Bruce Wong
# Std ID: 101266031
# comp1405_f22_101266031_tutorial_01_b.py

import pygame
pi = 3.141592653


drawing = pygame.display.set_mode((300, 300))

drawing.fill((255, 255, 255)) #fill background

pygame.display.flip() # displays image

display = True # variable to change

while display: # loops the display
    for x in pygame.event.get():
        if (x.type == pygame.QUIT): # if pyagme quits display = false and closes loop
            display = False

    pygame.draw.polygon(drawing,(0,0,0),((100,100),(130,100),(130,150),(100,150))) # body
    
    pygame.draw.circle(drawing, (0,0,0), (116,65), 15) #head
    
    pygame.draw.circle(drawing, (0,0,0), (116,100), 15) #neck

    pygame.draw.arc(drawing,(0,0,0),[80,100,50,40],pi/6,7*pi/6,width=3) #left arm

    pygame.draw.arc(drawing,(0,0,0),[85,140,30,30,],pi/2,3*pi/2,width=3) #left leg

    pygame.draw.line(drawing,(0,0,0),(98,169),(83,169),width=2) #left foot

    pygame.draw.arc(drawing,(0,0,0),[125,95,40,30],pi,7*pi/4,width=3) #right arm

    pygame.draw.arc(drawing,(0,0,0),[120,140,30,30],3*pi/4,7*pi/4,width=3) # right leg

    pygame.draw.line(drawing,(0,0,0),(144,165),(144,180),width=2) #left foot
    
    pygame.draw.arc(drawing, (255,255,255), [68,35,50,50], 3*pi/2, 15*pi/8, width=3) #mouth

    pygame.draw.arc(drawing, (0,0,0), [70,175,25,25], 0, 2*pi) #soccer ball

    pygame.draw.circle(drawing, (255,255,255), (112, 58), 2) # inner eye

    pygame.draw.circle(drawing, (0,0,0), (100, 55), 2) # outer eye

    pygame.draw.polygon(drawing, (0,0,0), [(80,175), (80,184), (70, 184)]) # ball lines

    pygame.draw.polygon(drawing, (0,0,0), [(93,187), (83,187), (83, 198)]) # ball lines
    
    pygame.draw.circle(drawing, (0,0,0), (82,128), 3) #left hand
    
    pygame.draw.circle(drawing, (0,0,0), (158,120), 3) #Right hand
    
    pygame.draw.line(drawing, (128,128,128), (146,50),(200,30), 2) #the wind
    pygame.draw.line(drawing, (128,128,128), (146,75),(210,70), 2)
    pygame.draw.line(drawing, (128,128,128), (146,95),(210,105), 2)

    pygame.display.update() #so image does stays on for more than 1 frame


pygame.image.save(drawing,"Style_1305.png") #just in case 
