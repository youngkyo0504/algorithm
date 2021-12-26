
def isPalindrome(s) :
    s = ''.join(ch for ch in s if ch.isalnum())
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False

print(isPalindrome(" "))
