acc=0
a=2
b=1

print("i\t\t\tm(i)")
print("-------------------------")

for i in range (1,11):
    acc = acc+ (b/a)
    a=a+1
    b=b+1
    print(i,"\t\t\t",acc)
