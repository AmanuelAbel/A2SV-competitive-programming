class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        def GCD(y,x):
            if x == 0:
                return y
            return GCD(x ,y%x)
        z = GCD(y,x)
        return z