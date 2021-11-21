# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) -1
        while lp <= rp :
            index = int((lp+rp)/2)
            if nums[index] == target :
               return index
            elif nums[index] < target :
                lp = index + 1
            else:  #nums[index] > target
                rp = index - 1
        return -1