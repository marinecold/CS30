#Lorenzo Clarke
#203245@gscs.ca
#Assignment 11 - Model View Controller

blueBrightness = 100 #defines and sets the variable for the brightness of the blue circle to start at 100
redBrightness = 150 #defines and sets the variable for the brightness of the red background to start at 150

circlePosX = 150 #defines and sets the x position of the circle to start at 150
circlePosY = 150 #defines and sets the y position of the circle to start at 150


def setup(): #on start the size of the canvas is set to 300x300 pixels, the background colour is set to red with the brightness of a variable, the shape infill colour is set to blue with the brightness of a variable, and a circle is placed at the position from the x and y variables
    
    size(300,300) #the size of the canvas is set to 300x300 pixels
    
    background(redBrightness,0,0) #the background colour is set to red with the brightness of the redBrightness variable
    
    fill(0,0,blueBrightness) #the shape infill colour is set to blue with the brightness of the redBrightness variable
    
    ellipse(circlePosX,circlePosY,50,50) #a circle is drawn at the center of the canvas using the x and y position variables and a diameter of 50 pixels
    
    
def mouse_clicked(): #on mouseclick the global variables for the x and y position of the circle are pulled and set to the position of the mouse pointer, the background is set to red to erase everything and a new blue circle is drawn
    
    global circlePosX, circlePosY #the global variables for the x and y position of the circle are pulled
    
    circlePosX = mouse_x #the x position of the circle is set the the x position of the mouse pointer
    circlePosY = mouse_y #the y position of the circle is set the the y position of the mouse pointer
    
    background(redBrightness,0,0) #the background is set to red with the brightness variable to erase everything
    
    ellipse(circlePosX,circlePosY,50,50) #a new circle is drawn at the new x and y coordinates
    

def key_pressed(): #the global variables for red and blue brightness are pulled, if the key pressed is n it lowers the brightness of blue by 5 as long as it is larger than 0, if the key pressed is b it brightens the brightness of blue by 5 as long as it is smaller than 255, if the key pressed is d it lowers the brightness of red by 5 as long as it is larger than 0, if the key pressed is r it brightens the brightness of red by 5 as long as it is smaller than 255
    
    global blueBrightness, redBrightness #the global variables for red and blue brightness are pulled
    
    if key == 'n': #if the key pressed is n then go on
        
        if blueBrightness > 0: #if the brightness is larger than 0 go on
    
            blueBrightness = blueBrightness - 5 #lower the brightness by 5
        
    if key == 'b': #if the key pressed is b then go on
        
        if blueBrightness < 255: #if the brightness is smaller than 255 go on
    
            blueBrightness = blueBrightness + 5 #up the brightness by 5
            
            
    if key == 'd': #if the key pressed is d then go on
        
        if redBrightness > 0: #if the brightness is larger than 0 go on
    
            redBrightness = redBrightness - 5 #lower the brightness by 5
        
    if key == 'r': #if the key pressed is r then go on
        
        if redBrightness < 255: #if the brightness is smaller than 255 go on
    
            redBrightness = redBrightness + 5 #up the brightness by 5
            
            
def draw(): #refreshes the colours by setting the background to red with the brightness of a variable thus erasing the circle, and creating a new circle at the variabes location with the variable brightness
    
    background(redBrightness,0,0) #sets the background colour to red with the brightness of the variable redBrightness
    
    fill(0,0,blueBrightness) #sets the shape infill colour to blue with the brightness of the variable blueBrightness
    
    ellipse(circlePosX,circlePosY,50,50) #draws a new circle at the x and y variables position and with a diameter of 50px
    