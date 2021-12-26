# 접미사 접두사 알아보는 법 

string = "abacaaba"

# 미스매치되었을 때 어떤 인덱스는 어디로 가야할 지 알려주는 게 KMP알고리즘이다. 
def makeTable(pattern):
        table = [0]
        j = 0
        print(len(pattern))
        for i in range(1,len(pattern)):
            print(i,j)
            print(pattern[i],pattern[j])
            if pattern[i] == pattern[j] : 
                table.append(j+1)
                j +=1
            elif pattern[i] == pattern[0]:
                table.append(1)
                j = 1
            else:
                table.append(0)
                j=0
                # print(table)
                # print("not same")
        return table

print(makeTable(string))
