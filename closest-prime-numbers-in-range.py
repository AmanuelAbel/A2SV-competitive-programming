class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1]*2
        nums = []
        def SieveOfEratosthenes(left,num,res):
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            for p in range(left, num+1):
                if prime[p] and p != 1:
                    res.append(p)
        SieveOfEratosthenes(left,right,nums)
        if len(nums) >= 2:
            ans[0] = nums[0]
            ans[1] = nums[1]
            curr = nums[1] - nums[0]
            for i in range(1,len(nums)):
                z = nums[i] - nums[i-1]
                if z < curr:
                    ans[0] = nums[i-1]
                    ans[1] = nums[i]
                    curr = z 
        return ans