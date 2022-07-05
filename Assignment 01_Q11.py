a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

def num11(a,b):
    sum = 0
    for x in range(a,b+1):
        sum = sum + x
        print(x,end=" ")
    print("\n") 
    return sum

print("sum of numbers:",num11(a,b))
