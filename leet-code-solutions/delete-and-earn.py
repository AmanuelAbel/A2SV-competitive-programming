class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        dp = [0,0]
        for i in range(len(nums)):
            res = nums[i] * count[nums[i]]
            if i > 0 and nums[i]  == nums[i-1] + 1:
                temp = dp[1]
                dp[1] = max(dp[1],res+dp[0])
                dp[0] = temp
            else:
                temp = dp[1]
                dp[1] += res 
                dp[0] = temp
        return dp[1]