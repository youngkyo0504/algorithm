# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

def decodeString(s):
    alphabets = ['']
    repititions = ['']
    for word in s: 
        print(alphabets,repititions)
        if word.isnumeric():
            repititions[-1] = repititions[-1] + word
        elif word == "[":
            alphabets.append("")
            repititions.append("")
        elif word == "]":
            repitition = repititions.pop()
            if repitition == '':
                repitition = repititions.pop()
            repit_string = alphabets.pop()
            repited_string = ''
            for i in range(int(repitition)):
                repited_string += repit_string
            print(repited_string)
            alphabets[-1] = alphabets[-1] + repited_string
            repititions.append("")
        else: 
            alphabets[-1] = alphabets[-1] + word
    print(alphabets[-1])
    return alphabets[-1]

decodeString("ab2[ab3[bc]]")

            