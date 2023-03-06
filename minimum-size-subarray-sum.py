class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0 , 0
        res = len(nums)
        counter = 0
        num = 0
        while r <= len(nums):
            while counter >= target:
                res = min(res,r-l)
                num += 1
                counter -= nums[l]
                print(counter)
                l += 1
            if r < len(nums):
                counter += nums[r]
                print(counter)
            r += 1
        return res if num != 0 else 0