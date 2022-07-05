import random
k = random.randint(2, 10) 
lis=[]
print("Enter",k,"values:") 
for i in range(k): 
    x=(int(input("Enter value "+str(i+1)+": "))) 
    lis.append(x) 

def collapse(lis):
    new_lis=[] 
    for i in range(0,len(lis),2):
        if(i==len(lis)-1): 
            x=lis[i]
        else: 
            x=lis[i]+lis[i+1]
        new_lis.append(x) 
    return new_lis


print("Old List:",lis) 
print("Collapse List:",collapse(lis)) 
