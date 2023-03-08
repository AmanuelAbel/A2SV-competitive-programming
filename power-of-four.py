class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==4 or n== 1:
            return True
        if n==0: return False
        else:
            return self.isPowerOfFour(n/4)