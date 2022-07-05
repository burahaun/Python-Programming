x = input("Enter the numbers: ")
L = x.split()
L2 = []
for i in range(len(L)):
    y = int(L[i])
    L2.append(y)
average = sum(L2) / len(L2)
sAA = 0
sBA = 0
L3 = []
L4 = []
for i in L2:
    if i >= average:
        sAA = sAA + 1
        L3.append(i)
    else:
        sBA = sBA + 1
        L4.append(i)

print("Average is:",average)
print("Number of scores above or equal to the average:",sAA)
print("Scores above or equal to the average:",L3)
print("Number of scores below the average:",sBA)
print("Scores below the average:",L4)




        
    
