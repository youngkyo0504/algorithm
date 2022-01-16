## 다시 풀어보기🐱‍👤

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# 한번더 체크 하는 것이 중요하다!!!
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
            
# 한번더 체크 하는 것이 중요하다!!!
def sortColors(nums: List[int]) -> None:
    zero_point = 0
    two_point = len(nums) - 1

    go_point = 0

    while go_point <= two_point:
        if nums[go_point] == 0:
            nums[go_point], nums[zero_point] = nums[zero_point], nums[go_point]
            zero_point += 1
        elif nums[go_point] == 2:
            nums[go_point], nums[two_point] = nums[two_point], nums[go_point]
            two_point -= 1
            continue
        go_point += 1

sortColors(nums)