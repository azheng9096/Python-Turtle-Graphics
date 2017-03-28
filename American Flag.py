#Anna Zheng Pd7
#Main Program
#American Flag

import turtle
bob = turtle.Turtle()
turtle.bgcolor('black')
turtle.screensize(4000, 4000)
bob.speed(0)
from myFunctionFile import*

#Blue Background
jump(bob,-340,240)
bob.begin_fill()
for times in range(2):
    bob.color('dark blue')
    bob.forward(615)
    bob.right(90)
    bob.forward(476)
    bob.right(90)
bob.end_fill()

#Stars
jump(bob,-300,200)
for times in range(6):#Six stars 
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()
    
jump(bob,-250,150)
for times in range(5):#Five Stars
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()
    
jump(bob,-300,100)
for times in range(6):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()
    
jump(bob,-250,50)
for times in range(5):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()
    
jump(bob,-300,0)
for times in range(6):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()

jump(bob,-250,-50)
for times in range(5):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()

jump(bob,-300,-100)
for times in range(6):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()

jump(bob,-250,-150)
for times in range(5):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()

jump(bob,-300,-200)
for times in range(6):
    star(bob,"white",25)
    bob.penup()
    bob.forward(100)
    bob.pendown()

#Stripes
jump(bob,275,240)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,275,172)
bob.begin_fill()
for times in range(2):
    bob.color('white')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,275,104)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,275,36)
bob.begin_fill()
for times in range(2):
    bob.color('white')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,275,-32)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,275,-100)
bob.begin_fill()
for times in range(2):
    bob.color('white')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,275,-168)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(1385)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()


jump(bob,-340,-236)
bob.begin_fill()
for times in range(2):
    bob.color('white')
    bob.forward(2000)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,-340,-304)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(2000)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,-340,-372)
bob.begin_fill()
for times in range(2):
    bob.color('white')
    bob.forward(2000)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,-340,-440)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(2000)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,-340,-508)
bob.begin_fill()
for times in range(2):
    bob.color('white')
    bob.forward(2000)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()

jump(bob,-340,-576)
bob.begin_fill()
for times in range(2):
    bob.color('red')
    bob.forward(2000)
    bob.right(90)
    bob.forward(68)
    bob.right(90)
bob.end_fill()
