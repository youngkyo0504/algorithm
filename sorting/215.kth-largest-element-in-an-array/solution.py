from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if (len(nums) == 1):  # 길이가 1이라면
            return nums[0]
        pivot = len(nums) - 1
        left_i, right_i = 0, len(nums) - 2
        while left_i <= right_i:
            print(nums)
            if nums[right_i] <= nums[pivot] and nums[left_i] > nums[pivot]:
                nums[right_i], nums[left_i] = nums[left_i], nums[right_i]
                continue
            if nums[left_i] <= nums[pivot]:
                left_i += 1
            if nums[right_i] > nums[pivot]:
                right_i -= 1

        nums[left_i], nums[pivot] = nums[pivot], nums[left_i]
        print(nums)
        nth_largest = pivot - left_i + 1
        if nth_largest == k:
            return nums[left_i]
        elif nth_largest > k:
            return Solution.findKthLargest(nums[left_i + 1:], k)
        else:
            return Solution.findKthLargest(nums[:left_i], k - nth_largest)

Solution.findKthLargest([3,2,1,5,6,4],2)