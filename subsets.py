class Solution:
    def helper(self,i,subsets,combs,nums):
        if i >= len(nums):
            subsets.append(combs.copy())
            return 
        combs.append(nums[i])
        self.helper(i+1,subsets,combs,nums)
        combs.pop()
        self.helper(i+1,subsets,combs,nums)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets =[]
        combs  =[]
        self.helper(0,subsets,combs,nums)
        return subsets