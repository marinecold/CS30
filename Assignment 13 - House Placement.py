#Lorenzo Clarke
#203245@gscs.ca
#Assignment 13 - House Placement

def setup():
    size(400,400)
    background(0, 101, 0)
    draw_tree(100,100)
    draw_house(200,200)
    
def draw_tree(x,y):
    fill(145, 72, 6)
    rect(x - 5, y + 5, 10, 30)
    fill(1, 255, 0)
    circle(x,y,25)

def draw_house(x,y):
    fill(255,255,255) #sets color to white
    rect(x-35,y-25,70,50) #base
    fill(255,0,0) #sets color to red
    rect(x-10,y-5,20,30) #door
    fill(0,0,255) #sets color to blue
    triangle(x-35,y-25,x+35,y-25,x,y-55) #roof