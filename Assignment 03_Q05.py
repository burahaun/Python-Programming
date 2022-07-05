import random
even = 0
odd = 0
for i in range(100):
    r = random.Random()
    a= r.randint(1,1000)
    print(a)
    if a % 2 == 1:
        odd = odd +1
    else:
        even = even + 1
    
print("Out of 100 random numbers,",odd,"were odd, and",even,"were even")
