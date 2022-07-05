def inCircle(xx,yy,rad):
    if (xx*2) + (yy*2) <= (rad**2):
        print("Point (",xx,",",yy,") is not in circle with radius",rad)
        return(True)
    else:
        print("Point (",xx,",",yy,") is in circle with radius",rad)
        return(False)

inCircle(10,-10,8)
