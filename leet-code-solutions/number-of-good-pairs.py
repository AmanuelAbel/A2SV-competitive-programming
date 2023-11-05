class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for c in count:
            if count[c] > 1:
                for i in range(count[c]-1,-1,-1):
                    res += i
        return res
