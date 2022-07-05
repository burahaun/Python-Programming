
nums = [1,2,0,3]



def findPairs(array,target):
    counter = 0
    for i in range(1,len(nums)):
        if nums[counter] + nums[i] == target:
            return nums.index(nums[counter]),nums.index(nums[i])
        else:
            counter = counter + 1
            nums[counter] + nums[i]

print(findPairs(nums,3))
