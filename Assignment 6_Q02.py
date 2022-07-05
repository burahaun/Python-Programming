import math
from cImage import *

whitePix= Pixel(0,0,0)
blackPix=Pixel(255,255,255)

def wandB (oldImg, whitePix, blackPix):
    oldWid= oldImg.getWidth()
    oldHei=oldImg.getHeight()
    New= EmptyImage(oldWid, oldHei)

    for i in range(New.getHeight()):
        for j in range (New.getWidth()):
            oldP= oldImg.getPixel(j,i)
            r= oldP.getRed()
            b=oldP.getBlue()
            g=oldP.getGreen()
            Avg=(r+g+b)//3
            if Avg <= 127:
                New.setPixel(j, i, whitePix)
            else:
                New.setPixel(j, i, blackPix)
    return New



def convert(FilP):
    oldImg= FileImage(FilP)
    height= oldImg.getHeight()
    width= oldImg.getWidth()
    win= ImageWin("Black and White", width* 2, height)
    oldImg.draw(win)

    newP= wandB(oldImg, whitePix, blackPix)
    newP.setPosition(oldImg.getWidth() + 1, 0)
    newP.draw(win)
    win.exitOnClick()
convert("butterfly.gif")
    
    
