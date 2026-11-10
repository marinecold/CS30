#Lorenzo Clarke
#203245@gscs.ca
#Assignment 15 - How Many Hamburgers?

def setup()

patties = 0
buns = 0

def key_pressed()

    if key == 'b':
        buns = buns + 12
        
    if key == 'p':
        patties = patties + 8
        
    if key == 'o':
        if buns > 0:
        buns = buns - 12
        
    if key == 'n':
        if patties > 0:
        patties = patties - 8
        
def draw()