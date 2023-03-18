class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        i = 0
        x = 1
        while x <= n:
            if x == n:
                return True
            x = 3**i
            i += 1