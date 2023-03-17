class Solution:
    def backtrack(self,i,subsets,combs,nums):
        if i >= len(nums):
            if combs not in subsets:
                subsets.append(combs.copy())
            return 
        combs.append(nums[i])
        self.backtrack(i+1,subsets,combs,nums)
        combs.pop()
        self.backtrack(i+1,subsets,combs,nums)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets =[]
        combs  =[]
        nums.sort()
        self.backtrack(0,subsets,combs,nums)
        return subsets