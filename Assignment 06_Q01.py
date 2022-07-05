from cImage import *

def tint (pic):
    
    red1 = pic.getRed()
    
    if red1 < 255:
        red1 = 255

    green = pic.getGreen()
    
    blue = pic.getBlue()
    
    y = Pixel(red1, green, blue)
    
    return y

def color(red) :
    
    a = FileImage(red)
    
    width = a.getWidth()
    height = a.getHeight()

    z = ImageWin( "Enhanced Red",width *2,height)
    a. draw(z)
    new = EmptyImage(width, height)
    
    for row in range(height):
        
        for col in range(width):
            
            pic = a.getPixel(col,row)
            y = tint (pic)
            new. setPixel(col, row, y)
            
    new.setPosition(width + 1,0)
    new.draw(z)
    z.exitOnClick()
    
color( 'butterfly.gif')
