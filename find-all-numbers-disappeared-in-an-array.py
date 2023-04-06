class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        arr = [0]*len(nums)
        for i in nums:
            arr[i-1] = i
        for i in range(len(arr)):
            if arr[i] == 0:
                res.append(i+1)
        return res