# Bruce Wong 
# 101266031
# comp1405_f22_101266031_tutorial_08_b.py
import pygame

def main():
    pygame.init()
    
    q = 0
    flag = True
    
    while flag: # loop until a file is valud 
        filename = str(input("What file do you want to open?: "))

        try:

            f = open(filename, "r")

            text = f.read().strip().split() # breaks the text up
            
            f.close()

            if text[1] == "forest" or text[1] == "desert": # end if tile isn't valid
                break                
            else:
                print("Tile name isn't valid")

                q = 1

            
        except:
            print("Please enter a valid file name\n")

    if q == 1: # the try except block bombs with quit() inside
        quit()

    h = len(text) - 2 # get the length of the main values the first 2 places are Tile: and tile type

    line = text[2].strip(",").split(",") # how long is the row
    w = len(line)

    img = pygame.image.load("tutorial_file_" + text[1] + "_0.gif") # get img size
    x = img.get_width()
    y = img.get_height()

    wide = x * w # size of the img in pygame
    high = y * h

    display = pygame.display.set_mode((wide,high))

    for i in range(h): # search for the correct img and blit it to the display
        for j in range(w):
            var = i + 2
            list_of_nums = text[var].strip(",").split(",") # the row of nums used for images
            img = pygame.image.load("tutorial_file_" + text[1] + "_" + list_of_nums[j] + ".gif")
            display.blit(img,(j * x,i * y))

    pygame.display.flip()
    
    flag = True
    
    while flag: 
        for p in pygame.event.get(): # if the user closes the window
            if (p.type == pygame.QUIT): 
                flag = False
        


main()

 

