array = [5,2,4,8,2,3,4,2,1]

def build_max_heap(array):
    for i in range(int(len(array) / 2), -1,-1):#1/2의 위치부터 해주는데 왜냐하면 바로 1단계는 힙화 할것이 없기 때문에 2단계인 반 이상부터 제 1노드까지 실행
        max_heapify(array, i)
    return array

def max_heapify(array, parent):
    if parent * 2 >= len(array):  #만약 패런트의 자식노드의 인덱스가 존재하지 않을 때 
        return
    child_L = 1 if parent==0  else parent * 2+1
    child_R = 2 if parent==0  else parent * 2+2
    if child_L < len(array) and child_R < len(array): 
        if array[parent] < max(array[child_L], array[child_R]):  #만약 자식노드중 부모노드보다 작은게 있으면 스왑해준다. 
            if array[child_L] <= array[child_R]:
                array[parent], array[child_R] = array[child_R], array[parent]  #R이 더크면 R과 스왑한다. 
            else:
                array[parent], array[child_L] = array[child_L], array[parent]  #L이 더크면 L과 스왑한다. 
        max_heapify(array, child_L)
        max_heapify(array, child_R)
    elif child_L < len(array):#자식노드가 한개만 존재할 때가 있다.   
        if array[parent]  < array[child_L]: #만약 자식노드가 크면  
            array[parent], array[child_L] = array[child_L], array[parent]  #L이 더크면 L과 스왑한다. 

def heap_sort(array):
    result=[]
    for i in range(len(array)): #어레이의 길이만큼 해야한다. 정렬이기 때문이다.
        array[0], array[len(array) - 1] = array[len(array) - 1], array[0] #제일 끝 인덱스와 처음 인덱스를 바꾸어준다. 
        result.append(array.pop()) #마지막 인덱스를 없애준다. 
        max_heapify(array,0)
    print(result)
heap_sort(build_max_heap(array))


    