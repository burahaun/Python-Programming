nums = [1,2,3,4,5,6,8,9]

def duplicates(array):
    L2 = []
    for i in range(len(array)):
        if L[i] not in L2:
            L2.append(L[i])
            if L[i] in L2:
                return True
        else:
            return False



print(duplicates(nums))
