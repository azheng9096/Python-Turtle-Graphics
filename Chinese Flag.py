#Chinese Flag Challenge
#Anna Zheng Pd7
#Main Program
import turtle
bob = turtle.Turtle()
turtle.bgcolor('black')
bob.speed(0)
bob.hideturtle()
from FunctionFile2 import*
from myFunctionFile import*

jump(bob,-500,240)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(900)
    bob.right(90)
    bob.forward(510)
    bob.right(90)
bob.end_fill()

jump(bob,-450,160)
FivePointedStar(bob,'yellow',100)

jump(bob,-280,115)
FivePointedStar(bob,'yellow',25)

jump(bob,-320,200)
bob.left(50)
FivePointedStar(bob,'yellow',25)

jump(bob,-270,155)
bob.left(60)
FivePointedStar(bob,'yellow',25)

jump(bob,-315,60)
bob.left(10)
FivePointedStar(bob,'yellow',25)
