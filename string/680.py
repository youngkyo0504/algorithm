def validPalindrome(s):
    equality = True
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            equality = False
            break
    if equality == True:
        return True

    break_points = [i,len(s)-1-i]

    for break_point in break_points : 
        forward = s[0:break_point] + s[break_point+1:]
        backward = s[len(s):break_point:-1] + ('' if break_point == 0 else s[break_point-1 ::-1])
        print(forward,backward)
        if forward == backward:
            return True
    return False


print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abcefgfedcba"))
print(validPalindrome("aba"))
print(validPalindrome("deeee"))

print("ss"[-2::-1])