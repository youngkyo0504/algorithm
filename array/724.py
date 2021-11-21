 nums = [1,7,3,6,5,6]
Output: 3


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if(i>0):
                left_sum += nums[i-1]
            right_sum -= nums[i]
            if(left_sum == right_sum):
                return i
        return -1


class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum   - x):
                return i
            leftsum += x
        return -1

# 변하지 않는 것과 변하는 것을 보자!