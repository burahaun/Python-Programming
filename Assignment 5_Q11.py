import random
def dice_sum():
    x = int(input("Desired dice sum: "))
    while True:
        a = random.randint(1,6)
        b = random.randint(1,6)
        print(a,"and",b,"=",a+b)
        if a + b == x:
            break

dice_sum()
