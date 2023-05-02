# Bruce Wong
# student ID: 101266031

import pygame

drawing = pygame.display.set_mode((480, 640))

drawing.fill((255, 255, 255))

pygame.draw.polygon(drawing,(82,144,60),((160,106),(0,320),(80,426,),(80,320),(160,320)))

pygame.draw.polygon(drawing, (93,70,50),((160,533),(160,640),(320,640),(400,533),(400,426),(320,426),(320,533)))

pygame.image.save(drawing,"assigned_image_for_101266031.png")
