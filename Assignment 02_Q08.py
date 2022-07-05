import turtle
t=turtle.Turtle()
t.goto(-75,0)

for i in range(0,4):
    t.forward(100)
    t.right(90)  
radius=50

def square(t, sidelength, numberOfSides):
    TurnAngle=360/numberOfSides
    for i in range (numberOfSides):
        t.forward(sidelength)
        t.right(TurnAngle)

def circle (t,radius):
    circum=2*3.14*radius
    sidelength=circum/360
    square(t,sidelength,360)
    
t=turtle.Turtle()
t.up()
t.goto(100,0)
t.down()
circle(t,50)
