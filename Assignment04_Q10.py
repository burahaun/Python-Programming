x = input("Enter numbers: ")
L = x.split()
L2 =[]
L3 = []
for i in range(len(L)):
    y = int(L[i])
    L2.append(y)

for i in range(len(L2)-1,-1,-1):
    L3.append(L2[i])

print("Original List:",L2)
print("After reversing the List:",L3)    
    


