class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        var = float("inf")
        for i in range(len(nums)):
            while stack and nums[stack[-1][0]] < nums[i]:
                stack.pop()
            if stack:
                if nums[i] > stack[-1][1] and nums[stack[-1][0]] > nums[i]:
                    return True
            stack.append([i,var])
            var = min(var,nums[i])
        return False    
           
        
        
        