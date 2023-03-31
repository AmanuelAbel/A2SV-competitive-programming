class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [[] for _ in range(len(nums))]
        for num in nums:
            arr[num - 1].append(num)
        res = [0] * 2
        for i in range(len(arr)):
            if len(arr[i]) > 1:
                res[0] = arr[i][0]
            if len(arr[i]) == 0:
                res[1] = i + 1
        return res