class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_table1={}
        hash_table2={}
        splited_s=s.split(" ")
        if len(splited_s) != len(pattern) :
            return False
        for i in range(len(pattern)):
            if pattern[i] in hash_table1 or splited_s[i] in hash_table2:
                if pattern[i] not in hash_table1 or splited_s[i] not in hash_table2:
                    return False
                # 이제 둘다 존재하는 상황
                if hash_table1[pattern[i]] != splited_s[i] or hash_table2[splited_s[i]] != pattern[i]:
                    return False
            else:
                hash_table1[pattern[i]] = splited_s[i]
                hash_table2[splited_s[i]] = pattern[i]

        return True

solution= Solution()
print(solution.wordPattern("abba","dog cat cat dog"))
print(solution.wordPattern("abba","dog dog dog dog"))