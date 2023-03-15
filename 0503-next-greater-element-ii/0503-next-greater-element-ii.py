class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        arr = [-1]*len(nums)
        arr2 = []
        for i in range(2):
            for z in nums:
                arr2.append(z)
        for i in range(len(arr2)):
            while stack and nums[stack[-1]] < arr2[i]:
                top = stack.pop()
                arr[top%len(nums)] = arr2[i]  
            stack.append(i%len(nums))
        return arr     
                
        