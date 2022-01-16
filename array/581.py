class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        find_first_index = -1
        find_last_index = -1
        first_index = -1
        last_index = -1

        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                find_first_index = i
                break
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                find_last_index = i
                break

        if find_first_index == -1 or find_last_index == -1:
            return 0
        
        min_value = min(nums[find_first_index:find_last_index+1])
        max_value = max(nums[find_first_index:find_last_index+1])

        for i in range(len(nums)):
            if  nums[i] > min_value:
                first_index = i
                break
        for i in range(len(nums)-1,-1,-1):
            if   nums[i] < max_value:
                last_index = i
                break
       
        return (last_index - first_index +1)

    
# nums = [1,2,3,4,5,6]
nums = [2,6,4,8,10,9,15]
findUnsortedSubarray(nums)
        