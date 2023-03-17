class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        L,R = 0,len(s) -1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True