import random
k = random.randint(2,10)
print("Enter",k,"values")
L = []
newL = []
for i in range(k):
    p = int(input("Enter value "+str(i+1)+": "))
    L.append(p)

def collapse(L):
    for i in range(0,len(L),2):
        if(i == len(L)-1):
            x=L[i]
        else:
            x=L[i]+L[i+1]
        newL.append(x)
    return newL

        


print("Old List:",L)
print("Collapse List:",collapse(L))
