def dailyTemperatures(temperatures):
    stack = []
    result = []
    for i in range(len(temperatures)-1,-1,-1):
        print(stack,"\n",result)
        if not stack :
            stack.append((i,temperatures[i]))
            result.append(0)
        else:
            while stack:
               if temperatures[i] < stack[-1][1]: # 클 가능성이 있는 아이
                   break
               else:
                   stack.pop() # 자신보다 작으면 제거
            if not stack:
                result.append(0)
            else:
                result.append(stack[-1][0] - i)

            stack.append((i, temperatures[i]))

    return(list(reversed(result)))


dailyTemperatures([89,62,70,58,47,47,46,76,100,70])




