class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        arr = []
        add = 0
        res = 0
        for i in nums:
            add += i
            arr.append(add)
        for i in arr:
            remainder = i % k
            if remainder in count:
                res += count[remainder]
            count[remainder] += 1
        return res
