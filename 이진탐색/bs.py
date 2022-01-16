
def bs(nums,target):
    left = 0
    right = len(nums) -1
    while left <= right:
        pivot = int((left+right)/2)
        print(pivot,left,right)
        if nums[pivot] == target: 
            return pivot
        elif nums[pivot] > target:
            right = pivot -1
        else: #nums[pivot] < target
            left = pivot +1
    return -1
nums= [1,3,5,7,9]
print(bs(nums,3))

