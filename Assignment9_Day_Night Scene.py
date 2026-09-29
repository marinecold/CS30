#Lorenzo Clarke
#203245@gscs.ca
#Assignment 9 Day/Night Scene

def setup():
#runs at the start of the program
    
    size(500,500)
    #sets canvas size to 500 by 500 pixels
    
    background(0, 160, 255)
    #sets the background colour to a light blue colour
    
    no_stroke()
    #removes the black outline on shapes
    
    fill(255,255,0)
    #changes fill colour to yellow
    ellipse(250,50,50,50)
    #draws a yellow circle in the top middle of the canvas
    
    fill(200,100,0)
    #changes fill colour to brown
    rect(0,425,500,75)
    #draws a brown rectancle at the bottom of the screen
    
    fill(255,0,255)
    #changes fill colour to purple
    rect(212,349,76,76)
    #draws the middle square in purple
    
    fill(0,255,0)
    #changes fill colour to green
    rect(337,349,76,76)
    #draws the right square in green
    
    fill(255,150,0)
    #changes fill colour to orange
    rect(87,349,76,76)
    #draws the left square in orange
    
def mouse_clicked():
#this function is tiggered when the user clicks their mouse
    
    background(0, 80, 125)
    #sets the background colour to a dark blue colour
    
    fill(255)
    #changes fill colour to white
    ellipse(250,50,50,50)
    #draws a circle in the top middle of the canvas over the last
    
    fill(100,50,0)
    #changes fill colour to dark brown
    rect(0,425,500,75)
    #draws a dark brown rectancle at the bottom of the screen over the last
    
    fill(125,0,125)
    #changes fill colour to dark purple
    rect(212,349,76,76)
    #draws the new middle square in dark purple over the last
    
    fill(0,125,0)
    #changes fill colour to dark green
    rect(337,349,76,76)
    #draws the new right square in dark green over the last
    
    fill(125,75,0)
    #changes fill colour to dark orange
    rect(87,349,76,76)
    #draws the new left square in dark orange over the last
    
    
def draw():
    return