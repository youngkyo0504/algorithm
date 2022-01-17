# 반씩 쪼개어서 정렬한다.
def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    half = int(len(numbers)/2)
    left_side = merge_sort(numbers[:half])
    right_side = merge_sort(numbers[half:])
    print(left_side,right_side)

    sorted_array = []
    left,right = 0,0
    while left < len(left_side) and right < len(right_side):
        if left_side[left] >= right_side[right] :
            sorted_array.append(right_side[right])
            right+=1
        else:
            sorted_array.append(left_side[left])
            left+=1

    if left < len(left_side): # left가 남아있으면
        sorted_array += left_side[left:]
    elif right < len(right_side):
        sorted_array += right_side[right:]

    return sorted_array


print(merge_sort([2,3,5,1,2]))
