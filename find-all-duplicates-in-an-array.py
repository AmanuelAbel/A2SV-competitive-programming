class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for c in count:
            if count[c] > 1:
                res.append(c)
        return res