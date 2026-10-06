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
    
    global circlePosX, circlePosY
    
    circlePosX = mouse_x
    circlePosY = mouse_y
    
    background(redBrightness,0,0)
    
    fill(0,0,blueBrightness)
    
    ellipse(circlePosX,circlePosY,50,50)

def key_pressed():
    
    global blueBrightness, redBrightness
    
    if key == 'n':
        
        if blueBrightness > 0:
    
            blueBrightness = blueBrightness - 5
        
    if key == 'b':
        
        if blueBrightness < 255:
    
            blueBrightness = blueBrightness + 5
            
            
    if key == 'd':
        
        if redBrightness > 0:
    
            redBrightness = redBrightness - 5
        
    if key == 'r':
        
        if redBrightness < 255:
    
            redBrightness = redBrightness + 5
            
def draw():
    
    background(redBrightness,0,0)
    
    fill(0,0,blueBrightness)
    
    ellipse(circlePosX,circlePosY,50,50)
    