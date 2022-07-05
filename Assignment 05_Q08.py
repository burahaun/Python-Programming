newFile = open("thisFile.txt","r")
newerFile = open("thatFile.txt","w")
acc = 0
for i in newFile:
    if acc % 2 == 0:
        newerFile.write(i)
    acc = acc + 1

newFile.close()
newerFile.close()
    
