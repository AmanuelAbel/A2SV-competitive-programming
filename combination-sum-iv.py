class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dp(idx,currentSum):
            if idx == len(nums):
                return 0
            if currentSum > target:
                return 0
            if currentSum == target:
                return 1
            if currentSum not in cache:
                ans = 0
                for i in range(len(nums)):
                    ans += dp(idx,currentSum + nums[i])
                cache[currentSum] = ans
            return cache[currentSum]
        cache ={}
        return dp(0,0)