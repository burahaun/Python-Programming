b = int(input("Enter number "))


def prob1(b):
    for x in range(1,b + 1):
        print(x, end= " ")
    

prob1(b)

print()

c = int(input("Enter number "))

def prob2(c):
    for x in range (c, 0, -1):
        print(x, end= " ")

prob2(c)

print()


d = int(input("Enter number "))

def prob3(d):
    sum=0
    for x in range(1, d+1, 2):
            sum=sum+x
    return sum

print(prob3(d))

e = int(input("Enter number "))

def prob3(e):
    sum=0
    for x in range(0, d+1, 2):
            sum=sum+x
    return sum

print(prob3(d))
      
