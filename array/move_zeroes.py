arr = [1,3,4,5,0,4,0,5]

def move_zeroes(arr):
    pivot = 0
    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[pivot], arr[i] = arr[i], arr[pivot]
            pivot +=1
    return arr    
print(move_zeroes(arr) )