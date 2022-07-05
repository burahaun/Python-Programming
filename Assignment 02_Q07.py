import turtle

t=turtle.Turtle()

def lattice_16x16():

    for a in range (8):
        t.up()
        t.forward(10)
        t.left(90)
        t.down()
        t.forward(160)
        t.right(90)
        t.up()
        t.forward(10)
        t.right(90)
        t.down()
        t.forward(160)
        t.left(90)
        
    for b in range (8):
        t.up()
        t.left(90)
        t.forward(10)
        t.left(90)
        t.down()
        t.forward(160)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.down()
        t.forward(160)


    for c in range (1):
        t.right(90)
        t.forward(160)
        t.right(90)
        t.forward(160)
        t.right(90)
        t.forward(160)
        
lattice_16x16()
