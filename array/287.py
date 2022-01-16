
def findDuplicate(nums) -> int:
        for i in range(len(nums)):
            find_index  = nums[0]
            if nums[find_index] == find_index:
                return find_index
            else: 
                nums[0],nums[find_index],  = nums[find_index],nums[0] 

print(findDuplicate([1,3,4,2,2]))