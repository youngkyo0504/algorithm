from collections import Counter
def firstUniqChar(s):
    counter = {}
    for i in range(len(s)):
        if s[i] in counter :
            counter[s[i]].append(i)
        else: #존재하지 않으면
            counter[s[i]] = [i]

    for key,value in counter.items():
        if len(value) == 1:
            return value[0]
    return -1

print(firstUniqChar("loveleetcode"))

