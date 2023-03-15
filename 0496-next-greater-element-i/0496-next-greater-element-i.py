class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        count = {}
        res = [-1]*len(nums1)
        for i, n in enumerate (nums1):
            count[n] = i
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                if nums2[top] in count:
                    res[count[nums2[top]]] = nums2[i]    
                
            stack.append(i)
            
      
        return res
                
                
        