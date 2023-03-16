class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        arr = [-1]*len(nums)
        for i in range(2*len(nums)):
            i = i%len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                arr[top] = nums[i]  
            stack.append(i)
        return arr