def twoSum(nums, target):
        target_nums = {}
        for i in range(len(nums)):
            if nums[i] in target_nums:
                result = [target_nums[nums[i]],i]
                return result
            else:
                target_nums[target-nums[i]] = i

print(twoSum([3,3],6))
