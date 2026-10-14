#Lorenzo Clarke
#203245@gscs.ca
#Assignment 12 - Cube of a Number


string = "" #defines and sets the global string to a string

def setup(): #on setup the canvas is set to 200x200 pixels, the background is set to black, and the infill colour for the text is set to white
    size(200,200) #canvas is set to 200x200 pixels
    background(0) #background is set to black
    fill(255) #infill colour for the text is set to white


def key_pressed(): #when a key is pressed it pulls the global string variable and adds the key that was pressed to the string, it erases all other text on the canvas and displays the string using the text function at 0, 10
    global string #pulls the global string variable
    
    string = string + key #adds the key that was pressed to the string
    
    background(0) #erases all other text on the canvas by setting the bacground to black
    
    text(string, 0, 10) #displays the string using the text function at x0, y10
    
def mouse_clicked(): #when the mouse is clicked it pulls the global string variable and converts the string into an integer which is then multiplied by 3 and turned back into a string who is displayed with the text function at x0, y20, the string is then emptied for re-use
    global string #pulls the global string variable
    
    text(str(int(string) ** 3), 0, 20) #converts the string into an integer which is then multiplied by 3 and turned back into a string which is displayed with the text function at x0, y20
    
    string = "" #empties the string