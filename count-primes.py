class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False  

        p = 2
        while p**2 <= n:
            if prime[p]:
                for i in range(p**2, n + 1, p):
                    prime[i] = False
            p += 1

        primes = [p for p in range(2, n + 1) if prime[p]]
        
        return len(primes) if primes[-1] != n else len(primes) - 1