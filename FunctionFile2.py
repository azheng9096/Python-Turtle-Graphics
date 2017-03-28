#function file

def FivePointedStar(t,c,d):
    t.begin_fill()
    for times in range(5):
        t.color(c)
        t.forward(d)
        t.right(144)
    t.end_fill()

def Triangle(t):
    t.forward(20)
    t.right(105)
    t.forward(50)
    t.right(150)
    t.forward(50)
