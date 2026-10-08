#Lorenzo Clarke
#203245@gscs.ca
#Assignment 12 - Cube of a Number


string = "" #defines and sets the global string to a string

def setup(): #on setup the canvas is set to 20x200 pixels, the background is set to black, and the infill colour for the text is set to white
    size(200,200)
    background(0)
    fill(255)


def key_pressed():
    global string
    
    string = string + key
    
    background(0)
    
    text(string, 0, 10)
    
def mouse_clicked():
    global string
    
    text(str(int(string) ** 3), 0, 20)
    
    string = ""