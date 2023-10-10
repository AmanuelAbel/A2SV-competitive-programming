class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i1,i2):
            if i1 >= len(nums1) or i2 >= len(nums2):
                return 0
            if nums1[i1] == nums2[i2]:
                return 1 + dp(i1+1,i2+1)
            else:
                return max(dp(i1+1,i2),dp(i1,i2+1))
        return dp(0,0)