# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
def removeDuplicates(s):
        result = [] # stack structure
        for word in s:
            if result == []:
                result.append(word)
            elif word == result[-1]:
                result.pop()
            else: #word != result[-1] 
                result.append(word)
        return("".join(result))

        
print(removeDuplicates("abbaca"))
            
            