# Bruce Wong
# 101266031
# comp1405_f22_101266031_assignment_11.py

import pygame

def main():
    pygame.init()

    flag = True

    text = [] # store the text to be used
    numLines = 0

    f = open("end_credits.txt", "r")
    while True:

        var = f.readline()
        if var == "":
            break
        var = var.strip("\n")
        var = var.strip(" ")

        text.append(var)
        numLines += 1 # amount of line in the file

    f.close()

    try:
        line = 0
        f = open("resume", "r")
        var = f.readline()
        for i in text: # look for which line it's on 
            if i == var:
                break
            line += 1

        y = 600 - line * 40 # the math to figure out position and font size
        size = 40 - line * 1

    except:
        y = 600 # if it doesn't match, go to defult values
        size = 40 

    display = pygame.display.set_mode((800,600))

    background = pygame.Surface((800,600))

    pygame.display.flip()

    y_count = 0
   
    while flag:
        if y == (0 - numLines * 40): # end once credit finishes
            pygame.time.delay(3000)
            flag = False

        for x in pygame.event.get():
            if (x.type == pygame.QUIT): # if pyagme quits display = false and closes loop
                # create file here
                num = 600 - y 

                if num < (600 - numLines * 40): # figure out the line that was at the position and save/create new file
                    num = num // 40

                    text_send = text[num]

                    file = open("resume","w")
                    file.write(text_send)
                    file.close()
                else: # anywhere past the end, saves the last line in file
                    file = open("resume","w")
                    file.write(text[numLines - 1])
                    file.close()

                flag = False

        display.fill((0,0,0)) # fill the screen to remove the text that was shown
        count = 0 # to allow the y value to change for different lines
        size_dec = 0 # so the font size isn't the same at all times

        for i in text: # x doesn't need to change, but y does
            font = pygame.font.SysFont("showcardgothic", size + size_dec)
            img = font.render(i, True, (255,255,0))
            img_r = img.get_rect(center=(400, y + count))

            display.blit(img, img_r)
            count += 40
            size_dec += 1


        pygame.display.update()

        pygame.time.delay(100)

        y -= 5

        y_count += 1
        if y_count == 8: # after moving up 40 pixels, change size
            size -= 1
            y_count = 0




main()


