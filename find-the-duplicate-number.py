class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        for c in count:
            if count[c] > 1:
                res = c
        return res