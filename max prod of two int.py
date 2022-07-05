L = [1,20,30,44,5,66,89,90,2,1,29,0,9,47]

def maxProduct(array):
    high=0
    counter = 0
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] * L[j] > high:
                high = L[i] * L[j]
                maxPair = str(L[i]),",",str(L[j])
    print(high)
    print(maxPair)


print(maxProduct(L))
        
            
