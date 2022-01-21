import itertools


def counting_sort(arr):
    min_num = min(arr)
    max_num = max(arr)

    range = max_num - min_num +1
    counter_arr = range*[0]

    for num in arr:
        counter_arr[num-min_num]+=1
    accumulate_sum = list(itertools.accumulate(counter_arr))
    for i in accumulate_sum:
        accumulate_sum[i] -=1 #accumulate_sum은 index를 나타내기 때문에 -1 해주어야한다.
    result = [0]*len(arr)

    for num in arr:
        index = num -min_num
        nth_smallest = accumulate_sum[index] #실제 얼마나 작은지
        accumulate_sum[nth_smallest] -=1
        result[nth_smallest] = num

    print(result)
    return result

arr = [2,5,1,2,6,7]
counting_sort(arr)




