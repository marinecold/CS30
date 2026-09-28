#Loreno Clarke
#203245@gscs.ca
#Assignment 6 The Robot!

def setup():
    size(255,255)
    #set canvas size to 255x255
    background(0,0,255)
    #makes the background blue
    draw_the_robot(200, 255, 255, 0)
    #draws the robot
    
def draw_the_robot(pc,sc1,sc2,sc3):
    draw_head(pc)
    draw_arms(pc,sc1,sc2,sc3)
    draw_legs(pc,sc1,sc2,sc3)
    draw_body(pc)
    #calls functions to draw all of the body parts
    
def draw_head(pc):

    fill(pc)
    ellipse(108,60,30,30)
    #draws left ear using the primary color
    ellipse(148,60,30,30)
    #draws right ear using the primary color
    ellipse(128,80,50,50)
    #draws the face using the primary color
    
    fill(0)
    ellipse(118,80,5,5)
    #draws left eye in black
    ellipse(138,80,5,5)
    #draws right eye in black
    
def draw_arms(pc,sc1,sc2,sc3):
    
    fill(pc)
    rect(68,130,120,8)
    #draws the arms using the primary color
    
    fill(sc1,sc2,sc3)
    ellipse(68,133,20,20)
    #draws the left hand using the secondary color
    ellipse(188,133,20,20)
    #draws the right hand using the secondary color
    
def draw_legs(pc,sc1,sc2,sc3):
    
    fill(pc)
    rect(108,155,8,80)
    #draws the left leg using the primary color
    rect(140,155,8,80)
    #draws the right leg using the primary color
    
    fill(sc1,sc2,sc3)
    ellipse(112,235,20,20)
    #draws the left foot using the secondary color
    ellipse(144,235,20,20)
    #draws the right foot using the secondary color
    
def draw_body(pc):
    
    fill(pc)
    ellipse(128,155,55,100)
    #draws the torso using the primary color
    
    fill(255,0,0)
    ellipse(128,155,5,5)
    #draws the middle button in red
    
    fill(0,255,0)
    ellipse(138,155,5,5)
    #draws the right button in green
    
    fill(0,0,255)
    ellipse(118,155,5,5)
    #draws the left button in blue
    
def mouse_clicked():
    
    fill(mouse_y,mouse_x,0)
    #turns the mouse x and y coordinates into usable values up to 255 and uses it as the color of the hands and feet
    ellipse(112,235,20,20)
    #draws the left foot using the color value of the mouse x and y coordinates
    ellipse(144,235,20,20)
    #draws the right foot using the color value of the mouse x and y coordinates
    ellipse(68,133,20,20)
    #draws the left hand using the color value of the mouse x and y coordinates
    ellipse(188,133,20,20)
    #draws the right hand using the color value of the mouse x and y coordinates
    
def draw():
    return