class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        while k > length:
            k -= length
        l = 0
        r = len(nums) - k 
        numbers = []
        
        
        if len(nums) > 1 and k < length:
            for i in range(r,len(nums)):
                numbers.append(nums[i])
                
            for i in range(l,r):
                numbers.append(nums[i])
                
            nums.clear()
            for i in range(length):
             if i <= length:
                nums.append(numbers[i])