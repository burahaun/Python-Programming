#Calculate 5 to the power of 2 (5^2)

def powerOfNum(base,n):
    assert int(n)==n,"Number must be a integer"
    if n == 0:
        return 1
    if n == 1:
        return base
    return base * powerOfNum(base,n-1)


print(powerOfNum(5,2))



