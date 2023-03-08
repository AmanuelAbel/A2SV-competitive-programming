class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = []
        rem = 0
        res = 0
        for num in nums:
            rem += num % 2
            arr.append(rem)
        prefix = {0: 1}
        for remainder in arr:
            if remainder - k in prefix:
                res += prefix[remainder - k]
            if remainder not in prefix:
                prefix[remainder] =1
            else:
                prefix[remainder] += 1
        return res