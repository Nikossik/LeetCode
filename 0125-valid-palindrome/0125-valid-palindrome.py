class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ''
        for i in range(len(s)):
            if s[i].isalpha():
                v += s[i].lower()
            elif s[i].isalnum():
                v += s[i]
        if v.lower() == v[::-1].lower():
            return True
        else: 
            return False