def tuition():
    for i in range(1,11):
        n = 10000*1.05**10
    print("Tuition in ten years is:",n)
    sum = 0
    for i in range(0,4):
        sum = sum + n*1.05**i
        print(sum)
    print("The four year tuition in 10 years is", sum)

tuition()
        
