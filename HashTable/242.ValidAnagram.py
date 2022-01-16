def isAnagram(s: str, t: str):
    counter1= {}
    counter2= {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in counter1:
            counter1[s[i]] += 1
        else:
            counter1[s[i]] = 0
        if t[i] in counter2:
            counter2[t[i]] += 1
        else:
            counter2[t[i]] = 0
    if counter2 == counter1:
        return True
    else:
        return False


print(isAnagram("anagram", "nagaram"))
