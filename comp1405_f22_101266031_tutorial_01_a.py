# Bruce Wong
# student id: 101266031

# comp1405_f22_101266031_tutorial_01_a.py

import pygame
pi = 3.141592653

drawing = pygame.display.set_mode((600, 600))

pygame.display.flip() # displays image

display = True # variable to change

while display:
    for x in pygame.event.get():
        if (x.type == pygame.QUIT): # if pyagme quits display = false and closes loop
            display = False
    pygame.draw.rect(drawing,(181, 56, 38),[0,0,600,600]) #redish background

    pygame.draw.arc(drawing,(219,209,197),[150,150,300,300],pi/2, 3*pi/2, width=150) #white arc

    pygame.draw.arc(drawing,(81,133,181),[150,150,300,300],3*pi/2, pi/2, width=150) #blue arc

    pygame.draw.arc(drawing,(31,31,31),[200,200,200,200],pi/2, 3*pi/2,width=150) #black arc

    pygame.draw.arc(drawing,(225,182,87),[200,200,200,200],3*pi/2, pi/2,width=150) #yellow arc

    pygame.draw.arc(drawing,(217,142,123),[250,250,100,100],3*pi/2, pi/2,width=150) #lighter red arc

    pygame.draw.polygon(drawing, (157,61,47),((299,295),(299,305),(294,305))) #right side triangle

    pygame.draw.polygon(drawing, (31,31,31),((299,295),(299,305),(304,305))) # left side triangle
    
    pygame.display.update() #displays image for not 1 frame 


pygame.image.save(drawing,"The_Swan.png") # just in case

