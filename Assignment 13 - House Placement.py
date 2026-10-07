#Lorenzo Clarke
#203245@gscs.ca
#Assignment 13 - House Placement

def setup():
    size(400,400)
    background(0, 101, 0)
    draw_tree(100,100)
    
def draw_tree(x,y):
    fill(145, 72, 6)
    rect(x - 2, y + 2, 4, 8)
    fill(1, 255, 0)
    circle(x,y,10)



def draw_house(x,y):
    return