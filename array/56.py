nums = [[1,5], [3,7], [10,15], [8,16]]

def mergeIntervals(nums):
    nums = sorted(nums)
    result = [nums[0]]
    for i in range(1,len(nums)):
       current = result[len(result)-1]
       next = nums[i]
       if current[1] >= next[0]:
           result[len(result)-1] = [min(current[0],next[0]), max(current[1],next[1])]
       else:
           result.append(next)
    return result     







































def mergeIntervals(nums):
    result = [nums[0]]
    nums=sorted(nums)
    for i in range(1,len(nums)):
        arr = result[len(result)-1]
        next_arr = nums[i]
        if arr[1] >= next_arr[0]:
            mergeInterval= [min(arr[0], next_arr[0]), max(arr[1],next_arr[1])]
            result[len(result)-1] = mergeInterval
        else: 
            result.append(next_arr)
    return result



        
    

print(mergeIntervals(nums))