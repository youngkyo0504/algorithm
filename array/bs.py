a = [1,2,4,6,7,10,16]
rp = len(a)-1
lp = 0


# rpoint lpoint
def bs(arr,target):
    lp = 0 
    rp = len(arr)-1

    while lp <= rp : 
        pivot = int((lp+rp)/2) 
        if arr[pivot] == target:
            return pivot
        elif arr[pivot] < target: 
            lp = pivot+1
        else:  # arr[pivot] > target:
            rp = pivot-1
    return -1


print(bs(a,4))
