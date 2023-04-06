class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for c in count:
            if count[c] == 1:
                return c