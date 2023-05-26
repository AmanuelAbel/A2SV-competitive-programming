class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first , second = 2**32,2**32
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False