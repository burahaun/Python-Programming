x = input("Enter scores separated by spaces from one line: ")
L = x.split()
L2 = []
for i in range(len(L)):
    y = int(L[i])
    L2.append(y)

for i in range(len(L2)):
    if L2[i] >= 90 and L2[i] <= 100:
        grade = "A"
    elif L2[i] >= 80 and L2[i] < 90:
        grade = "B"
    elif L2[i] >= 70 and L2[i] < 80:
        grade = "C"
    elif L2[i] >= 60 and L2[i] < 70:
        grade = "D"
    else:
        grade = "F"
    print("Student",i,"score is",L2[i],"and grade is",grade) 
    

