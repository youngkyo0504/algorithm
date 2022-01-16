def minSubArrayLen( target, nums) :
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum += nums[len(nums)-i-1]
            print(left_sum,right_sum)
            if left_sum >= target or right_sum >= target:
                return i 
    

nums = [1,4,4]
target = 4
print(minSubArrayLen(target,nums))


