#Lorenzo Clarke
#203245@gscs.ca
#Assignment 13 - House Placement

def setup(): #on start this function sets the canvas size to 400x400
    size(400,400) #sets the canvas size to 400x400
    
def draw_tree(x,y): #when this function is called it draws a tree with the center of its canopy at the given x and y
    fill(145, 72, 6) #sets shape infill color to brown 
    rect(x - 5, y + 5, 10, 30) #draws a rectangle coming down from the given x and y
    fill(1, 255, 0) #sets shape infill color to green
    circle(x,y,25) #draws a circle  centered on x and y with a diameter of 25

def draw_house(x,y): #when this function is called it draws a house centered on the given x and y coordinates
    fill(255,255,255) #sets shape infill color to white
    rect(x-35,y-25,70,50) #draws the base of the house using relative points from the given x and y and the specified dimensions
    fill(255,0,0) #sets shape infill color to red
    rect(x-10,y-5,20,30) #draws the door of the house using relative points from the given x and y and the specified dimensions
    fill(0,0,255) #sets shape infill color to blue
    triangle(x-35,y-25,x+35,y-25,x,y-55) #draws the roof of the house using relative points from the given x and y and the specified dimensions
    
def draw(): #every frame this function re-draws the scene
    
    background(0, 101, 0) #sets the background colour to dark green
    draw_tree(100,100) #draws a tree centered on 100, 100
    draw_tree(200,50) #draws a tree centered on 200, 50
    draw_tree(150,75) #draws a tree centered on 150, 75
    draw_tree(300,350) #draws a tree centered on 300, 350
    draw_tree(360,200) #draws a tree centered on 360, 200
    draw_tree(40,200) #draws a tree centered on 40, 200
    fill(0,255,255) #sets shape infill color to cyan
    ellipse(200,300,150,100) #draws the a lake at 200,300 with a height of 100 and a width of 150
    draw_house(mouse_x, mouse_y) #draws the house at the mouse's x and y coordinates