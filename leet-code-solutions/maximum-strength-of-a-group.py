class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        negative = 0
        res = 1
        if len(nums) == 1:
            return nums[-1]
        for i in nums:
            if i < 0:
                negative += 1
        
        if negative > 1 and negative % 2 == 0:
            for i in nums:
                if i == 0:
                    continue
                res *= i
        if negative <= 1:
            if nums[-1] == 0:
                return 0
            for i in nums:
                if i == 0 or i < 0:
                    continue
                res *= i
            return res
        if negative % 2 == 1:
            for i in nums:
                if i == 0:
                    continue
                if i < 0:
                    neg = i
                res *= i  
            res //= neg 
        return res