class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        stack2 = []
        x = float("inf")
        for i in range(len(nums)):
            x = min(x,nums[i])
            stack2.append(x)
        for i in range(len(nums)-1,-1,-1):
            var = stack2[i]
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                if nums[top] > var:
                    return True
            stack.append(i)
        
        return False    
           
        
        
        