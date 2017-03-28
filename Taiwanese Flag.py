#Taiwanese Flag
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
    bob.forward(600)
    bob.right(90)
bob.end_fill()

jump(bob,-500,240)
bob.begin_fill()
for times in range(2):
    bob.color('dark blue')
    bob.forward(450)
    bob.right(90)
    bob.forward(300)
    bob.right(90)
bob.end_fill()

jump(bob,-275,20)
bob.begin_fill()
bob.color('white')
bob.circle(75)
bob.end_fill()

jump(bob,-280,15)
bob.begin_fill()
Triangle(bob)
bob.end_fill()

jump(bob,-268,175)
bob.begin_fill()
bob.left(74)
Triangle(bob)
bob.end_fill()

jump(bob,-355,100)
bob.begin_fill()
bob.right(13)
Triangle(bob)
bob.end_fill()

jump(bob,-195,85)
bob.begin_fill()
bob.left(75)
Triangle(bob)
bob.end_fill()

jump(bob,-310,168)
bob.begin_fill()
bob.left(10)
Triangle(bob)
bob.end_fill()

jump(bob,-342,140)
bob.begin_fill()
bob.right(70)
Triangle(bob)
bob.end_fill()

jump(bob,-347,60)
bob.begin_fill()
bob.right(50)
Triangle(bob)
bob.end_fill()

jump(bob,-320,28)
bob.begin_fill()
bob.right(65)
Triangle(bob)
bob.end_fill()

jump(bob,-240,22)
bob.begin_fill()
bob.right(50)
Triangle(bob)
bob.end_fill()

jump(bob,-210,47)
bob.begin_fill()
bob.right(75)
Triangle(bob)
bob.end_fill()

jump(bob,-200,125)
bob.begin_fill()
bob.right(55)
Triangle(bob)
bob.end_fill()

jump(bob,-225,160)
bob.begin_fill()
bob.right(65)
Triangle(bob)
bob.end_fill()
