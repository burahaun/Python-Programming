x = open('data.txt','r')
y = x.readlines()
L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
for i in y:
    L1.append(i.strip())
for i in L1:
    L2=[]
    L2=i.split()
    for i in range(len(L2)):
        L2[i]=float(L2[i])
    L3.append(L2)
for i in L3:
    L4=[]
    for j in L3:
        xx=pow((pow((j[0]-i[0]),2)+pow((j[1]-i[1]),2)),1/2)
        L4.append("{:.2f}".format(xx))
    L5.append(L4)

print("       P1       P2       P3       P4       P5       P6       P7       P8")
for i in range(len(L5)):
    print("P"+str(i + 1)+"     "+'     '.join(map(str, L5[i])))
