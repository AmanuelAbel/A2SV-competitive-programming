class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        var1 = bisect_left(nums, target)
        var2 = bisect_right(nums, target)
        arr = []
        if target in nums:
            arr.append(var1)
            arr.append(var2 - 1)
            return arr
        return [-1,-1]