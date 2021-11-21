arr = [1,4,1,1,1]

def find_pivot_index(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i in range(len(arr)):
        right_sum -= arr[i]
        if(i>0):
            left_sum += arr[i-1]
        if left_sum == right_sum:
            return i 
    return -1
print(find_pivot_index(arr))