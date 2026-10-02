#Lorenzo Clarke
#203245@gscs.ca
#Assignment 10 - Pin the Tail on the Donkey

def setup(): #The setup function runs when the code starts. It sets the size of the canvas to 400x400pixels, changes the background colour to gray, and activates the function draw_donkey to draw the donkey
    
    size(400,400) #Sets the size of the canvas to 400x400 pixels
    
    background(125) #Sets the background to gray
    
    draw_donkey() #Activates the function to draw the donkey
    
def mouse_clicked(): #This function activates when the mouse is clicked. It draws a brown rectangle at the location of the mouse and then a red circle on the location of the mouse to act as the tail of the donkey
    
    fill(209, 150, 107) #Sets the shape infill colour to light brown
    
    rect(mouse_x,mouse_y,10,30) #Draws a rectange at the location of the mouse that is 10 pixels wide and 30 pixels long
    
    fill(255,0,0) #Sets the shape infill colour to red
    
    ellipse(mouse_x,mouse_y,10,10) #Draws a circle at the location of the mouse that is 10 pixels in diameter
    
def key_pressed(): #This function activates when any key is pressed. It removes all of the placed tails by setting the background to gray to remove everything, and activating draw_donkey to draw the donkey again
    
    background(125) #Sets the background to gray thus removing all other drawings
    
    draw_donkey() #Activates the function to draw the donkey
    
def draw_donkey(): #When called, this function draws the donkey by setting the infill colour to brown and drawing using shapes
    
    fill(210, 105, 30) #Sets shape infill colour to brown
    
    rect(130, 160, 40, 40) #Draws the neck of the donkey
    
    rect(145, 220, 20, 55) #Draws the front right leg of the donkey
    
    rect(155, 220, 20, 55) #Draws the front left leg of the donkey
    
    rect(220, 220, 20, 55) #Draws the back right leg of the donkey
    
    rect(230, 220, 20, 55) #Draws the back left leg  of the donkey
    
    ellipse(200, 200, 140, 60) #Draws the torso of the donkey
    
    ellipse(150, 125, 15, 55) #Draws the right ear of the donkey
    
    ellipse(160, 125, 15, 55) #Draws the left ear of the donkey
    
    ellipse(130, 155, 80, 40) #Draws the head of the donkey
    
def draw():
    return
