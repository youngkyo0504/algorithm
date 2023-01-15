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
        

MAX_NUM = 10**4 +1
MIN_NUM = -(10**4) -1

# 망한 알고리즘 실패하는 코드들... 2023년 1월 16일 어찌 퇴보하는것 같다? 
# 교훈 최대최소 구할 때는 무조건 min, max를 쓰자. 범위를 줄이면된다. 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
            left,right = 0,0
            length = len(nums)
            llmp = nums[0] if nums[0] > nums[1] else MIN_NUM 
            slmp = nums[length-1] if nums[length -1 ]< nums[length-2]  else MAX_NUM

            for i in range(1,len(nums)-1): 

                if ( nums[i-1] < nums[i]) and nums[i] > nums[i+1]:
                    llmp = max(llmp, nums[i])
                if nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                    slmp = min(slmp, nums[i])

            if llmp == MIN_NUM and slmp == MAX_NUM : 
                return 0;

            for i in range(length-1,-1,-1):
                    if  nums[i] < llmp  : 
                        right = i
                        break
                    
           
            for i in range(length):
                    if nums[i] > slmp :
                        left = i
                        break
            return right-left+1


                



            

