#Lorenzo Clarke
#203245@gscs.ca
#Assignment 14 - Circle in a Box

def setup(): #sets the canvas size and removes shape strokes when the program is first run
    
    size(400,300) #sets the canvas to 400x by 300y pixels
    no_stroke() #removes the shape strokes
    
def draw(): #sets the background to black and draws a yellow circle within the border with constrained mouse x and y variables and draws the blue border
    
    background(0) #fills the canvas with black
    fill(255,255,0) #sets the shape infill colour to yellow
    
    circle_x = constrain(mouse_x, 75, 400) #defines the circle x position as the mouse x coordinate only if it is within the specified area not in the border
    circle_y = constrain(mouse_y, 0, 225) #defines the circle y position as the mouse y coordinate only if it is within the specified area not in the border
    
    circle(circle_x,circle_y,50) #draws a circle at the location of the circle x and y variables with a diameter of 50
    
    fill(0,0,255) #sets the shape infill colour to blue
    rect(0,0,50,300) #draws a rectangle covering 50 pixels of width at the left edge of the window
    rect(0,250,400,300) #draws a rectangle covering 50 pixels of height at the bottom edge of the window
    
    