class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mydict = Counter(nums)
        res = 0
        for i in mydict:
            res = max(res,mydict[i])
        arr = []
        for i in mydict:
            if mydict[i] == res:
                arr.append(i)
        res = float("inf")
        for c in arr:
            i = 0
            j = len(nums)-1
            while i < len(nums):
                if c == nums[i]:
                    break
                i += 1
            while j >= 0:
                if c == nums[j]:
                    break
                j -= 1
            res = min(res,j - i + 1)
        return res
