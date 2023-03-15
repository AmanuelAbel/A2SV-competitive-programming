class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        arr = [0]*len(nums)
        for i in range(len(nums)):
            counter = 0
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                arr[top] = i - top
            stack.append(i)
        return arr 