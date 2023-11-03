class Solution:
    def soupServings(self, n: int) -> float:
        memo = {}
        def dp(a,b):
            if a <= 0 and b > 0:
                return 1
            if a <= 0 and b <= 0:
                return 0.5
            if a > 0 and b <= 0:
                return 0
            if (a,b) in memo:
                return memo[(a,b)]

            val = dp(a-100,b) + dp(a-75,b-25) + dp(a-50,b-50) + dp(a-25,b-75)
            memo[(a,b)] = val*0.25
            return val*0.25
        if n >= 4800:
            return 1
        return dp(n,n)
