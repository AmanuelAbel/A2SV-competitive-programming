class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        count = set()
        count.add(0)
        target = sum(nums)
        if target % 2 != 0:
            return False
        else:
            target = target // 2
        for i in range(len(nums)-1,-1,-1):
            temp = set()
            for c in count:
                temp.add(nums[i]+c)
                temp.add(c)
                
            count = temp
        return target in count