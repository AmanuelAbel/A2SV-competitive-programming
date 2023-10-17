class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        val = nums[-1] - nums[0]
        if val == 0:
            return 0
        if val >= 2*k:
            return val - 2*k
        return 0