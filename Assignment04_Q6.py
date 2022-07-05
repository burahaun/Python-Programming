x = input("Enter the numbers: ")
L = x.split()
L2 = []
L3 = []
for i in range(len(L)):
    y = int(L[i])
    L2.append(y)
for i in L2:
    if i not in L3:
        L3.append(i)

print("The distinct numbers are",L3)
