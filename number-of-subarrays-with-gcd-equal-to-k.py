class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def GCD(y,x):
            if x == 0:
                return y
            return GCD(x,y%x)
        answer = 0
        for idx in range(len(nums)):
            num = nums[idx]
            for idx2 in range(idx, len(nums)):
                num = GCD(num, nums[idx2])
                if num == k:
                    answer += 1

        return answer