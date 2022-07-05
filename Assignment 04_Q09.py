lst = input("Enter numbers: ")
L = lst.split()
L2=[]
for i in range(len(L)):
    y = int(L[i])
    L2.append(y)
def isSorted(lst):
        if sorted(L2) == L2:
            return "The list is already sorted"
        else:
            return "The list not sorted"
    
print(isSorted(lst))
