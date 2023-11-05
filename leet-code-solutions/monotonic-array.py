class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True 
        operation = 0  
        n = 0 
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 0:
                if nums[i] > nums[i-1]:
                    operation = 1
                else:
                    operation = -1
                n = i 
                break
        if operation == 1:
            for i in range(n,len(nums)):
                if nums[i] < nums[i-1]:
                    return False
        else:
            for i in range(n,len(nums)):
                if nums[i] > nums[i-1]:
                    return False
        return True 
                        
