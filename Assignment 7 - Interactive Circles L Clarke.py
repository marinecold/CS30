#Lorenzo Clarke
#203245@gscs.ca
#Assignment 7 - Interactive Circles

def setup():
    
    size(500,500)
#creates the canvas at 500x500 pixels
    
def draw():
    
    background(255)
#erases the last circles
    
    fill(0)
    ellipse(mouse_x,mouse_y,100, 100)
#draws a black circle of 100 pixel diameter
    
    fill(125)
    ellipse(mouse_x,mouse_y,50, 50)
#draws a gray circle of 50 pixel diameter on top of the last one