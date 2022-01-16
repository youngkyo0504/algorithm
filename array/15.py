# from collections import Counter
# def twoSum( nums):
#     cnt=Counter(nums)
#     print(cnt)
#     result = []
#     if len(nums) < 3:
#         return result

#     for k in cnt.keys():
#         count = int(cnt[k])
#         if  k != 0 and count > 2 :
#             cnt[k] = 2
#     nums= sorted(cnt.elements())
#     print(nums)
#     previous_answer=[]
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             for k in range(j+1,len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0 :
#                     answer = [nums[i],nums[j],nums[k]]
#                     if previous_answer != answer:
#                         result.append(answer) 
#                         previous_answer = answer
#     return result


def threeSum( nums):
    nums = sorted(nums)
    result = []
    for i in range(len(nums)-1):
        target = nums[i]
        if i>0 and nums[i] == nums[i-1]:
            print(nums[i],nums[i-1],i)
            continue
        if nums[i] > 0:
            break 
        for j in range(i+1,len(nums)-1):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            right = len(nums)-1
            left = j
            while left < right:
                sum_lr= nums[left] + nums[right] 
                if sum_lr == -target :
                    result.append([nums[i],nums[left],nums[right]])
                    break
                elif sum_lr > target:
                    right -=1
                else:
                    break
    return result
                    
                    




            

            



print(threeSum(
[0,0,0,0]))


# [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]
# [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]