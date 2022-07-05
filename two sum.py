

nums = [3,2,4]

def pairSum(array, target):
    for i in range(len(array)):
        for j in range(i+1):
            if nums[i] == nums[j]:
                continue
            elif nums[i]+nums[j] == target:
                   return nums.index(nums[i]),nums.index(nums[j])


print(pairSum(nums,6))
