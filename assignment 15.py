#Lorenzo Clarke
#203245@gscs.ca
#Assignment 15 - How Many Hamburgers?

pattiespack = 0
bunspack = 0

def setup():
    
    size(400,300)
    

def key_pressed():

    global pattiespack, bunspack
    
    if key == 'b':
        bunspack = bunspack + 1
        
    if key == 'p':
        pattiespack = pattiespack + 1
        
    if key == 'n':
        if bunspack > 0:
            bunspack = bunspack - 1
        
    if key == 'o':
        if pattiespack > 0:
            pattiespack = pattiespack - 1
        
def draw():
    
    background(125)
    
    text("Pack(s) of patties:", 50, 100)
    text("Pack(s) of buns:", 50, 120)
    text("Hamburger(s) made:", 80, 200)
    
    text(pattiespack, 150, 100)
    text(bunspack, 150, 120)
    text(hamburgers, 200, 200)
    
    if pattiespack x 8 > bunspack x 12:
        hamburgers = bunspack
        
    if bunspack x 12 => pattiespack x 8:
        hamburgers = pattiespack