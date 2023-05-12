class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(x):
            return x[::-1]
        res = set()
        for i in range(len(nums)):
            res.add(nums[i])
            res.add(int(reverse(str(nums[i]))))
        return len(res)