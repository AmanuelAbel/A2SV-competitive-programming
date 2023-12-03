class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add = 0
        arr = []
        for i in nums:
            add += i
            arr.append(add)
        return arr