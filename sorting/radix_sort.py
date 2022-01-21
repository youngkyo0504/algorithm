import itertools


def radix_sort(arr):
    max_num = max(arr)
    max_digit= len(str(max_num))

    for nth in range(max_digit):
        print(arr)
        remainder_arr = [0]*len(arr)
        for i,number in enumerate(arr):
            str_num =str(number)
            target_digit =len(str_num) - (nth+1)  # 5자릿수인데 2번째 자리를 구하고 싶다.
            if target_digit >= 0:
                remainder_arr[i] = int(str_num[target_digit])
        counting_arr = [0]*10
        for num in remainder_arr:
            counting_arr[num]+=1
        accumulate_sum = list(itertools.accumulate(counting_arr))
        for i in range(len(accumulate_sum)):
            accumulate_sum[i] -=1
        tmp_arr = [0]*len(arr)
        for i in range(len(arr)-1,0,-1):
            remainder = remainder_arr[i]
            nth_smallest = accumulate_sum[remainder]
            tmp_arr[nth_smallest] = arr[i] #순서대로 정렬
            accumulate_sum[remainder] -=1
        arr = tmp_arr
    return arr

print(radix_sort([111,220,210,2,3,44]))













