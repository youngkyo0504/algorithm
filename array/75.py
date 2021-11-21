nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


def sortColors( nums) -> None:
        left = 0
        right = len(nums) -1 
        i = 0
        while i <= right:
            print(i,left,right)
            if nums[right] == 2 : 
                if i == right:
                    i+=1
                right -=1
                continue
            if nums[left] == 0:
                if i == left:
                    i+=1
                left += 1 
                continue
            if nums[i] == 2 : 
                print(nums[left],nums[right],nums[i])
                nums[right], nums[i] =  nums[i] ,nums[right]
                right -=1
            elif nums[i] == 0:
                print(nums[left],nums[right],nums[i])
                nums[left], nums[i] = nums[i], nums[left]
                left +=1
            if nums[i] == 1 :
                i+=1
            print(nums)
        return nums
            

sortColors(nums)