#Lorenzo Clarke
#203245@gscs.ca
#Assignment 11 - Model View Controller

blueBrightness = 100
redBrightness = 150
circlePosX = 150
circlePosY = 150

def setup():
    size(300,300)
    background(redBrightness,0,0)
    fill(0,0,blueBrightness)
    ellipse(150,150,50,50)
    
def mouse_clicked():
    circlePosX = mouse_x
    circlePosY = mouse_y
    background(redBrightness,0,0)
    ellipse(circlePosX,circlePosY,50,50)

def key_pressed
    
    