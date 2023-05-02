# Bruce Wong 
# 101266031
# comp1405_f22_101266031_tutorial_08_a.py

# try: except:

from random import randint

def main():
    w = int(input("How wide do you want the map?: "))

    h = int(input("How tall do you want the map?: "))

    while True:
        img_name = str(input("How will the image files be named? ")) # look for tile name
        
        if img_name == "forest" or img_name == "desert": # must be forest or desert
            break
        else:
            print("Please enter 'forest' or 'desert'\n")
            

    filename = str(input("What file do you wnat to open?: ")) # name of file

    f = open(filename, "w")

    f.write("Tile: "+ img_name)

    f.write("\n\n")

    for y in range(h): # writing in the file. Loops the first loop for the next line, not column
        for x in range(w):
            value = str(randint(0,4))
            f.write(value + ",")
            
        f.write("\n")
        
    f.close()
    
    
main()