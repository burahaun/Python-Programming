from cImage import *

def horizontalFlip(ogImage):
    
    wid = ogImage.getWidth()
    hei = ogImage.getHeight()
    x = ImageWin( "Mirror", wid *2, hei)
    ogImage.draw(x)
    
    FinalImage = MirroredImage (ogImage)
    FinalImage.setPosition(wid + 1, 0)
    FinalImage.draw(x)
    
def MirroredImage (ogImage):
    
    OGwid = ogImage.getWidth()
    OGhei = ogImage.getHeight()
    NewPicture = EmptyImage(OGwid, OGhei)
    nHeight = int (OGhei / 2)

    for i in range(nHeight):
        
        for j in range (OGwid):
            
            oPix = ogImage.getPixel(j, i)
            NewPicture.setPixel(j,i,oPix)
            NewPicture.setPixel(j, i, oPix)
            
    nHeight = int(OGhei / 2)

    z = OGhei - 1
    
    for i in range(nHeight):

        for j in range(OGwid):

            oPix=ogImage.getPixel(j,i)

            NewPicture.setPixel(j, z - i, oPix)
            
    return NewPicture

ogImage = FileImage("tree.gif")
horizontalFlip(ogImage)
MirroredImage(ogImage)
