# Bruce Wong	
# STD ID: 101266031
# comp1405_f22_101266031_assignment_04.py

#Avengers Endgame - superhero movie, avengers 
#Thor: Love and Thunder - superhero movie, Thor
#Avengers Age of Ultron - superhero movie, avengers 
#Iron Man - superhero movie, cgi, Robert Downey Jr
#Morbius - superhero movie, cgi
#Demon Slayer -Kimetsu no Yaiba - animated, adventure
#Jurassic Park - dinosaurs, cgi
#Mission Impossible - Fallout - Tom Cruise
#Kingsman: The Secret Service - spy, comdey, cgi
#Pirates of the Caribbean - pirates, cgi, disney

#Kung Fu Panada - animated, animals
#TMNT - cgi, animals, turtles
#Lego Ninjago Movie - animated, lego, kids movie
#Mulan - animated, disney
#The Karate Kid - fighting, kung fu
#The Next Karate Kid - fighting, kung fu, sequal (2010)
#Mortal Kombat - arcade game, cgi, fighting
#Ip Man - matrial arts master, real life inspiration 
#Man Of Tai Chi - fight club
#Drunken Master - intoxication, martial arts
#Kill Bill - assassin, fighting

var = input("Would you like to view Instructions? (yes/no): ")

if var == "yes":
    print("Besides picking subgenre, answer either 'yes' or 'no' for any given question.")



var = input("Which subgenre would you like to choose? (Adventure/Material Arts): ")
    
if var == "Adventure":
   response = input("Is the movie a superhero movie?: ")
   if response == "yes":
        response = input("Is it the movie that finished the Infinity Saga?: ")
        
        if response == "yes":
            print("Your movie is Avengers Endgame")
            
        else:
            response = input("Did the movie have the bad CGI floating head?: ")
            
            if response == "yes":
                print("Your movie is Thor: Love and Thunder")
                
            else:
                response = input("Was the movie's main antagonist an super intellegent AI?: ")
                
                if response == "yes":
                    print("Your movie is Avengers Age of Ultron")
                    
                else:
                    response = input("Was it the movie that Robert Downey Jr. played in for the MCU?: ")
                    
                    if response == "yes":
                        print("Your movie is Iron Man")
                        
                    else:
                        print("Your movie is Morbius")

   else:
        response = input("Is the movie an anime?: ")
        
        if response == "yes":
            print("Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train")
            
        else:
            response = input("Does the movie contain active dinosaurs?: ")
            
            if response == "yes":
                print("Your movie is Jurassic Park")
                
            else:
                response = input("Does the movie star Tom Cruise?: ")
                
                if response == "yes":
                    print("Your movie is Mission Impossible - Fallout")
                    
                else:
                    response = input("Is the movie also a spy comedy film?: ")
                    
                    if response == "yes":
                        print("Your movie is Kingsman: The Secret Service")
                        
                    else:
                        print("Your movie is Pirates of the Caribbean")

elif var == "Material Arts":
    response = input("Is the movie animated?: ")
    
    if response == "yes":
        response = input("Does the movie involve animals?: ")
        
        if response == "yes": 
            response = input("Does the movie involve animals with a shell?: ")
            
            if response == "yes":
                print("Your movie is Teenage Mutant Ninja Turtles")
            
            else:
                print("Your movie is Kung Fu Panada")
                
        else: 
            response = input("Does it involve the small blocks?: ")
            
            if response == "yes":
                print("Your movie is The Lego Ninjago Movie")
            
            else:
                print("Your movie is Mulan")
    else:
        response = input("Did the movie have a 2010 remake?: ")
        if response == "yes":
            response = input("Is it the sequal?")
        
            if response == "yes":
                print("Your movie is The Next Karate Kid")
            
            else:
                print("Your movie is The Karate Kid")
            
        else:
            response = input("Was it originally from an arcade game?: ")
            
            if response == "yes":
                print("Your movie is Mortal Kombat")
                
            else:
                response = input("Was the movie inspired by a Grandmaster of the matrial art Wing Chun?: ")
                
                if response == "yes":
                    print("Your movie is Ip Man")
               
                else:
                    response = input("Does the movie take place in a underworld fight club?: ")
                    
                    if response == "yes":
                        print("Your movie is Man Of Tai Chi")
                        
                    else:
                        response = input("Does the movie involve an intoxicated master?: ")
                        
                        if response == "yes":
                            print("Your movie is the Drunken Master")
                        
                        else:
                            print("Your movie is Kill Bill")