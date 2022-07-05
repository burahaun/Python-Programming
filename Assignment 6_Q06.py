rows=4 
columns=3 
a=[] 
for i in range(rows):
    a.append([0]*columns)
    
print("Part A:")
for i in range(rows):
    for j in range(columns):
        print(a[i][j],end=" ")
    print("")
for i in range(rows):
    if i == 0:
        a[i]=[1]*columns 
    else:
        a[i]=[3]*columns
        
print("Part B")
for i in range(rows):
    for j in range(columns):
        print(a[i][j],end=" ")
    print("")
for i in range(rows):
    a[i][0]=2 
for i in range(rows):
    a[i][1]=a[i][0]*2 
    a[i][2]=a[i][1]*2
    
print("Part C")
for i in range(rows):
    for j in range(columns):
        print(a[i][j],end=" ")
    print("")
