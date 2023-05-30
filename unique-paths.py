class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def isvalid(x,y):
            if x > m or x < 1 or y < 1 or y > n:
                return False
            return True
        def dp(x,y,cache):
            nonlocal m,n
            if not isvalid(x,y):
                return 0
            if not cache[(x,y)]:
                cache[(x,y)] = dp(x+1,y,cache) + dp(x,y+1,cache)
            return cache[(x,y)]
        cache = defaultdict(int)
        cache[(m,n)] = 1
        dp(1,1,cache)
        return cache[(1,1)]