L = []
for i in range(10):
    x = int(input("Enter a number: "))
    L.append(x)
print("Low:",min(L))
print("High:",max(L))
print("Total:",sum(L))
print("Average:",sum(L)/len(L))
