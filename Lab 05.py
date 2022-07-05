import turtle
import random
t=turtle.Turtle()
t.forward(100)
t.right(180)
t.forward(200)
t.right(180)
t.forward(100)
t.right(90)
t.forward(100)
t.right(180)
t.forward(200)
t.penup()
t.position()


for i in range(10):
    y=random.randint(-100,0)
    x=random.randint(0,100)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.dot(3,"red")


for i in range(10):
    y=random.randint(0,100)
    x=random.randint(-100,0)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.dot(3,"blue")

t.penup()
t.setpos(0,0)
