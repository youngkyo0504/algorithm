# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
def minRemoveToMakeValid(s: str):
        parentheses = []
        remove_index_list = []
        for i in range(len(s)):
            if s[i] == "(":
                parentheses.append(i)
            elif s[i] == ")":
                if parentheses == []: # 비어있다면..? 
                    remove_index_list.append(i)
                else:
                    parentheses.pop()
        for remove_index in parentheses:
            remove_index_list.append(remove_index)
        print ("".join([char for idx, char in enumerate(s) if idx not in remove_index_list])        ) # 뭔가 이부분이 별로인거 같다. 너무 비효율적??? 


minRemoveToMakeValid("))((")
minRemoveToMakeValid("a)b(c)d")




                
        