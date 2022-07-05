a=1
acc=0

for i in range (1, 625):
    i = a/((i**(1/2))+((i+1)**(1/2)))
    acc = acc + i
print("Sum:",acc)
