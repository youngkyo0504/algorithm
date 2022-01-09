# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.



def isValid(s):
        valid_parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        checks = []
        for word in s: 
            if word in ["(","{","["] :
                checks.append(word)
            else:
                if checks == []: 
                    return False
                if valid_parentheses[word] != checks.pop(): 
                    return False
        if checks != []: 
                return False
        return True

            
print(isValid("()"))