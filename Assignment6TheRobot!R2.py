#Loreno Clarke
#203245@gscs.ca
#Assignment 6 The Robot!

size(500,500)
#set canvas size to 500x500

def draw_the_robot(pc,sc1,sc2,sc3):
    draw_head(pc)
    draw_arms(pc,sc1,sc2,sc3)
    draw_legs(pc,sc1,sc2,sc3)
    draw_body(pc)
    #calls functions to draw all of the body parts
    
def draw_head(pc):

    fill(pc)
    ellipse(230,80,30,30)
    #draws left ear using the primary color
    ellipse(270,80,30,30)
    #draws right ear using the primary color
    ellipse(250,100,50,50)
    #draws the face using the primary color
    
    fill(0)
    ellipse(240,100,5,5)
    #draws left eye in black
    ellipse(260,100,5,5)
    #draws right eye in black
    
def draw_arms(pc,sc1,sc2,sc3):
    
    fill(pc)
    rect(190,150,120,8)
    #draws the arms using the primary color
    
    fill(sc1,sc2,sc3)
    ellipse(190,153,20,20)
    #draws the left hand using the secondary color
    ellipse(310,153,20,20)
    #draws the right hand using the secondary color
    
def draw_legs(pc,sc1,sc2,sc3):
    
    fill(pc)
    rect(230,175,8,80)
    #draws the left leg using the primary color
    rect(262,175,8,80)
    #draws the right leg using the primary color
    
    fill(sc1,sc2,sc3)
    ellipse(234,255,20,20)
    #draws the left foot using the secondary color
    ellipse(266,255,20,20)
    #draws the right foot using the secondary color
    
def draw_body(pc):
    
    fill(pc)
    ellipse(250,175,55,100)
    #draws the torso using the primary color
    
    fill(255,0,0)
    ellipse(250,175,5,5)
    #draws the middle button in red
    
    fill(0,255,0)
    ellipse(260,175,5,5)
    #draws the right button in green
    
    fill(0,0,255)
    ellipse(240,175,5,5)
    #draws the left button in blue
    
draw_the_robot(200, 200, 160, 0)
#draws the robot