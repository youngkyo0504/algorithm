def threeSumClosest(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        left = i+1 
        right = len(num)-1
        while left < right: 
            nums[i] + nums[left] + nums[right]