from typing import List
from typing import Dict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter ={}
        result =[]
        for word in words:
            if word in counter:
                counter[word] +=1
            else:
                counter[word] = 0
        counter = sorted(counter.items(), key=lambda x: x[0])
        counter = sorted(counter, key=lambda x: x[1], reverse=True)
        # 정렬은 안정적임이 보장됩니다. 즉, 여러 레코드가 같은 키를 가질 때, 원래의 순서가 유지됩니다.
        for i in range(k):
            result.append(counter[i][0])

        return result
solution = Solution()
print(solution.topKFrequent(["i","love","leetcode","i","love","coding"],2))
print(solution.topKFrequent(["i","love","leetcode","i","love","coding"],2))

