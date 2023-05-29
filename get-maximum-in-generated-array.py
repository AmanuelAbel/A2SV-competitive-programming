class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def dp(n,memo):
            if n <= 1:
                memo[n] = n 
                return n
            if not memo[n]:
                if n%2 == 0:
                    memo[n] = dp(n//2,memo)
                else:
                    memo[n] = dp(n//2,memo) + dp((n//2)+1,memo)
            return memo[n]
        memo = [0]*(n+1)
        dp(n,memo)
        for i in range(1,len(memo)):
            if memo[i] == 0:
                dp(i,memo)

        return max(memo)