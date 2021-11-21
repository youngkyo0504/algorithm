nums = [1,0,1]
# Output: [1,3,12,0,0]
def moveZeroes(nums):
        pivot = 0
        for i in range(len(nums)):
            print(pivot,i)
            while pivot != len(nums)-1 and nums[pivot] and pivot < i == 0 : 
                pivot +=1
            print(pivot,i)
            if nums[i] == 0 and i < pivot :
                nums[i], nums[pivot] = nums[pivot], nums[i]
            print(nums)
        return nums
moveZeroes(nums)

