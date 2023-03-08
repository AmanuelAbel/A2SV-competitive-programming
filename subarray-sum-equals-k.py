class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        summ = 0
        res = 0
        for i in nums:
            summ += i
            z = summ - k
            if z in prefix:
                res += prefix.get(z,0)
            prefix[summ] = 1 + prefix.get(summ,0)
        return res