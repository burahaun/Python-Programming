from random import randint

print("The original numbers: ")
L = [randint(10,20) for i in range(50)]

i  = 0
while i < len(L):
    print(L[i],L[i+1],L[i+2],L[i+3],L[i+4])
    i = i + 5
print('')

def eliminateDuplicates(L):
    x = list()
    for num in L:
        if num not in x:
            x.append(num)
    return x


print("The distinct numbers are: ")

newL = eliminateDuplicates(L)

for i in range(0,len(newL),5):
    print(*newL[i:i+5],sep=' ')
