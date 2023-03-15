class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        var = float("inf")
        for i in range(len(nums)):
            var = min(var,nums[i])
            while stack and nums[stack[-1][0]] <= nums[i]:
                stack.pop()
            if stack:
                if nums[i] > stack[-1][1]:
                    return True
            stack.append([i,var])
        return False    
           
        
        
        