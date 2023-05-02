# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_assignment_08.py

def draw_eyes(): # on pos (150,250) 
    black = (0, 0, 0) # because functions are only taken, these variables aren't going to be initialized outside of functions 
    white = (255,255,255)
    red = (255,0,0)
    pi = 3.14159     

    pygame.draw.circle(win_sfc, black, (117, 225), 3) # eye pupil
    pygame.draw.circle(win_sfc, black, (187, 225), 3)
    
    pygame.draw.arc(win_sfc, black, (90, 195, 40, 40), 0, 2*pi, 3) # eye body    
    pygame.draw.arc(win_sfc, black, (170, 195, 40, 40), 0, 2*pi, 3)     
    
    pygame.draw.arc(win_sfc, black, (90, 180, 40, 40), 9*pi/8, 15*pi/8, 3) # eyelid    
    pygame.draw.arc(win_sfc, black, (170, 180, 40, 40), 9*pi/8, 15*pi/8, 3)         
    
def draw_hat(): # on pos (250, 350)
    black = (0, 0, 0)
    white = (255,255,255)
    red = (255,0,0)
    pi = 3.14159     
    
    pygame.draw.arc(win_sfc, black, (185, 230, 130, 80), 0, 2*pi, 500) # base of hat 
    
    pygame.draw.rect(win_sfc, black, (210, 150,80,110)) # the rectangle part of hat
    
    pygame.draw.rect(win_sfc, white, (215, 235,70,10)) # white strip
    
    return "top hat"

def draw_mouth(x, y): # on pos (x, y)
    black = (0, 0, 0)
    white = (255,255,255)
    red = (255,0,0)
    pi = 3.14159     
    
    pygame.draw.arc(win_sfc, black, (x - 50, y + 20, 110, 50), 0, 2*pi, 500) # mouth body      
    
    pygame.draw.arc(win_sfc, red, (x - 40, y + 47, 65, 40), 0, 7*pi/8, 500) # tongue     

    pygame.draw.polygon(win_sfc, white, ((x,y + 15),(x,y + 35),(x - 20, y + 35),(x - 20,y + 20))) # teeth 1
    
    pygame.draw.polygon(win_sfc, white, ((x,y + 15),(x,y + 35),(x + 20, y + 35),(x + 20,y + 20))) # teeth 2
    
    pygame.draw.line(win_sfc, black, (x,y + 17),(x,y + 35)) # the line in between the teeth 
