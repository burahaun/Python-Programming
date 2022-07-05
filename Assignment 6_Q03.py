from cImage import *

def horizontalflip(oldimg):
    oldwidth= oldimg.getWidth()
    oldheight= oldimg.getHeight()

    newIM= EmptyImage(oldwidth, oldheight)
    maxPa= oldheight-1

    for i in range (oldheight):
        for j in range(oldwidth):
            oldPa= oldimg.getPixel(j, maxPa-i)
            newIM.setPixel(j, i, oldPa)

    return newIM

def flip(image):
    oldimg= FileImage(image)
    wi= oldimg.getWidth()
    he= oldimg.getHeight()
    w= ImageWin("Horizontal Flip", wi*2, he)
    oldimg.draw(w)
    newIM= horizontalflip(oldimg)
    newIM.setPosition(wi+1,0)
    newIM.draw(w)
    w.exitOnClick()

flip("butterfly.gif")
