def quick_selection(arr,k):
    if(len(arr) == 1): #길이가 1이라면
        return arr[0]
    pivot = len(arr)-1
    left_i,right_i = 0,len(arr)-2
    while left_i <= right_i :
        print(arr)
        if arr[right_i] <= arr[pivot] and arr[left_i] > arr[pivot]:
            print("swap")
            arr[right_i],arr[left_i] = arr[left_i],arr[right_i]
            continue
        if arr[left_i] <= arr[pivot]:
            left_i +=1
        if arr[right_i] > arr[pivot]:
            right_i -=1

    arr[left_i],arr[pivot]= arr[pivot],arr[left_i]
    print(arr)
    nth_largest = pivot -left_i + 1
    if nth_largest == k:
        return arr[left_i]
    elif nth_largest > k:
        return quick_selection(arr[left_i+1:],k)
    else:
        return quick_selection(arr[:left_i],k-nth_largest)

print(quick_selection([3,5,9,9,1,2,7,4],1))
print(quick_selection([3,5,9,9,1,2,7,4],2))
print(quick_selection([3,5,9,9,1,2,7,4],3))
print(quick_selection([3,5,9,9,1,2,7,4],4))
print(quick_selection([3,5,9,9,1,2,7,4],5))
print(quick_selection([3,5,9,9,1,2,7,4],6))
print(quick_selection([3,5,9,9,1,2,7,4],7))












