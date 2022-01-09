

# def strStr(haystack, needle):
#     if needle == "":
#         return 0
#     for i in range(len(haystack)):
#         if i+len(needle)-1 < len(haystack) and haystack[i:i+len(needle)] == needle:
#            처음 조건문은 range 조절임 
#             return i
#     return -1        

# print(strStr("aaab","ab"))

class Solution:
    def strStr(self, s: str, goal: str) -> int:
        double_s = s+s
        for i in range(len(double_s)-len(s)+1):
            if double_s[i:i+len(s)]==goal:
                return True
        
        return False

for i in range(1):
    if ""[0:1] == "":
        print("hj")
    print(""[0:1])