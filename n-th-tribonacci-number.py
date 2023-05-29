class Solution:
    def tribonacci(self, n: int) -> int:
        def tri(n,memo):
            if n < 2:
                return n
            if n == 2:
                return 1
            if not memo[n]:
                memo[n] = tri(n-1,memo) + tri(n-2,memo) + tri(n-3,memo)
            return memo[n]
        memo = defaultdict(int)
        return tri(n,memo)