#function file

def polygon(t, sides, distance):
    angle = 360/sides#angle variable is inside the function
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()
    
def BlackPixel(t):
    t.color('black')
    polygon(t,4,4)

def CactuarPixel(t):
    polygon(t,4,4)
