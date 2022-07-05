L = [3,2,2,3]


def removeElement(nums, val):
    counter = 0
    for i in range(len(nums)):
        if i == val:
            del nums[i]
            counter = counter +1
    return counter, nums

print(removeElement(L,3))
