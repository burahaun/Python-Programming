import math
x = input("Enter numbers: ")
L = x.split()
L2=[]
def mean(x):
    for i in range(len(L)):
        y = int(L[i])
        L2.append(y)
    print("The mean is",sum(L2)/len(L2))

mean(x)

def deviation(x):
    L3 = []
    m = sum(L2)/len(L2)
    for i in range(len(L2)):
        c = (L2[i] - m)**2
        L3.append(c)
    n1 = len(L3)-1
    d = sum(L3)/n1
    dev = math.sqrt(d)
    print("The standard deviation is",dev)
        

deviation(x)
