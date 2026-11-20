#Lorenzo Clarke
#203245@gscs.ca
#Assignment 15 - How Many Hamburgers?

pattiespack = 0 #declares the variable associated with the number of packs of patties
bunspack = 0 #declares the variable associated with the number of packs of buns

def setup(): #changes the size of the canvas at the begining of the program
    
    size(400,300) #changes the size of the canvas
    

def key_pressed(): #when a key that is desired is pressed it increase or decreases either the number of packs of patties or buns

    global pattiespack, bunspack #declares the variables in the function so that we can change them
    
    if key == 'b': #if the key pressed is 'b' it adds 1 to the amount of packs of buns
        bunspack = bunspack + 1
        
    if key == 'p': #if the key pressed is 'p' it adds 1 to the amount of packs of patties
        pattiespack = pattiespack + 1
        
    if key == 'n': #if the key pressed is 'n' and the amount of packs of buns is greater than 0 it subtracts 1 from the amount of packs of buns
        if bunspack > 0:
            bunspack = bunspack - 1
        
    if key == 'o': #if the key pressed is 'o' and the amount of packs of patties is greater than 0 it subtracts 1 from the amount of packs of patties
        if pattiespack > 0:
            pattiespack = pattiespack - 1
        
def draw(): #every frame the maximum amount of hamburgers that can be created with the variable packs of patties and buns is calculated and displayed to the user
    
    hamburgers = 0 #declares a variable for how many hamburgers we can make
    
    if pattiespack * 8 > bunspack * 12: #if the amount of patties is bigger than the amount of buns the max hamburgers = the amount of buns
        hamburgers = bunspack * 12
        
    if bunspack * 12 >= pattiespack * 8: #if the amount of buns is bigger than or equal to the amount of patties the max hamburgers = the amount of patties
        hamburgers = pattiespack * 8
    
    background(0) #clear the last frame by setting the background to black
    
    text("Pack(s) of patties:", 80, 100)
    text("Pack(s) of buns:", 80, 120)
    text("Hamburgers made:", 80, 140)
    
    text(pattiespack, 200, 100)
    text(bunspack, 200, 120)
    text(hamburgers, 200, 140)
    
    
    