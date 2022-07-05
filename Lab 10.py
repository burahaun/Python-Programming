myFile = open("numbers.txt","r")
L = []
L2 = []
L3=[]
for i in myFile:
    lines = i.split()
    L.append(lines[1])

       
for i in range(len(L)):
    x = int(L[i])
    L2.append(x)

print("count =",len(L2))
print("sum =",sum(L2))

for i in L2:
    if i % 2 == 0:
        L3.append(i)
print("evens =",len(L3))
print("average =",sum(L2)/len(L2))
    
