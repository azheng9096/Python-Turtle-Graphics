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
    polygon(t,4,5)

def LightGrayPixel(t):
    t.color('light gray')
    polygon(t,4,5)

def WhitePixel(t):
    t.color('white')
    polygon(t,4,5)

def GoldPixel(t):
    t.color('gold')
    polygon(t,4,5)

def YellowPixel(t):
    t.color('yellow')
    polygon(t,4,5)

def OrangePixel(t):
    t.color('orangered')
    polygon(t,4,5)

def LightBluePixel(t):
    t.color('light blue')
    polygon(t,4,5)

def BluePixel(t):
    t.color('dark blue')
    polygon(t,4,5)

def PinkPixel(t):
    t.color('fuchsia')
    polygon(t,4,5)

def LightPinkPixel(t):
    t.color('light pink')
    polygon(t,4,5)

def LightBrownPixel(t):
    t.color('peru')
    polygon(t,4,5)

def BrownPixel(t):
    t.color('saddlebrown')
    polygon(t,4,5)
