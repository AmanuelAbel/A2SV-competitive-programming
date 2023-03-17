class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            m = len(ans)
            for j in range(m):
                res = ans[j] + [nums[i]]
                ans.append(res)
        return ans