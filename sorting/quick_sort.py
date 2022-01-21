def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    pivot = len(arr)-1
    left_i,right_i = 0,len(arr)-2
    while left_i <= right_i:
        if arr[left_i] > arr[pivot] and arr[right_i] <= arr[pivot]:
            arr[left_i],arr[right_i] = arr[right_i],arr[left_i]
        else:
            if arr[left_i] <= arr[pivot]:
                left_i+=1
            if arr[right_i] > arr[pivot]:
                right_i-=1
    arr[left_i],arr[pivot] = arr[pivot],arr[left_i]
    right_side_arr = []
    if left_i +1 <= len(arr):
        right_side_arr = quick_sort(arr[left_i+1:])

    return quick_sort(arr[:left_i]) + [arr[left_i]] + quick_sort(right_side_arr)
arr1 = [3,2,6,4,7,2,3]
print(quick_sort(arr1))
