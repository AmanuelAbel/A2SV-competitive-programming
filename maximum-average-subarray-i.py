class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r = 0,0 
        counter = 0
        res = float(-inf)
        if k == 1:
            return max(nums)
        if k == 0:
            return 0
        while r < len(nums):
            while r < len(nums)and (r - l + 1) <= k :
                counter += nums[r] 
                r+=1
                print(counter)
            res = max(res,counter/k) 
            counter -= nums[l]
            l += 1 
            print(res)
        return res