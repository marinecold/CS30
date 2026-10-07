string = ""

def setup():
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
    
    