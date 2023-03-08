class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l ,r = 0 , len(nums) - 1
        ans = 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return ans