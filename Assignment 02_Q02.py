def getPentagonalNumber(n):
    for i in range(1,n+1):
        n=int(i*(3*i-1)/2)
        print(n, end=" ")

getPentagonalNumber(10)
