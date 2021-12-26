
def lengthOfLongestSubstring(s):
    start = 0
    dic = {}
    max = 0

    for i in range(len(s)): 
        print(s[i])
        if s[i] in dic and dic[s[i]] != -1: 
            start = dic[s[i]]+1
            for key, value in dic.items():
                if value < start:
                    dic[key] = -1
            dic[s[i]] = i
        else: 
            dic[s[i]] = i
        substring = s[start:i+1] 
        print(substring)
        max = max if max > len(substring) else len(substring )
    return max
print(lengthOfLongestSubstring("abba"))