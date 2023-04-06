class Solution:
    def prime(self,n,factorization):
        d = 2
        while d * d <= n:
            while n % d == 0:
                factorization.append(d)
                n //= d
            d += 1
        if n > 1:
            factorization.append(n)
        
        return factorization
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1
        ans = set()
        for i in nums:
            z = self.prime(i,[])
            for x in z:
                ans.add(x)
        print(ans)
        return len(ans)