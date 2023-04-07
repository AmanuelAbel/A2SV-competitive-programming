class Solution:
    def minSteps(self, n: int) -> int:
        res = []
        def prime(n,factorization):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)
        prime(n,res)
        return sum(res)