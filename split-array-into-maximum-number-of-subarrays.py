class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res = res & nums[i]
        if res != 0:
            return 1
        else:
            ans = 0
            res = nums[0]
            for i in range(1,len(nums)):
                if res == 0:
                    ans += 1
                    res = nums[i]
                res = res & nums[i]
        if res == 0:
            ans += 1
        return ans