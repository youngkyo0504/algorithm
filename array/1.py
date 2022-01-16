def twoSum( nums, target):
    for i in range(nums):
        for j in range(i+1,len[nums]):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                return [nums[i],nums[j]]


        