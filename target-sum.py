class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i,val):
            if i == len(nums):
                if val == target:
                    return 1
                else:
                    return 0
            if (i,val) not in cache:
                cache[(i,val)] = dp(i+1,val+nums[i]) + dp(i+1,val-nums[i])
            return cache[(i,val)]
        cache = {}
        return dp(0,0)