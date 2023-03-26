class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        positive = [[] for _ in range(10001)]
        negative = [[] for _ in range(10001)]
        for num in nums:
            if num >= 0:
                positive[num].append(num)
            else:
                negative[num].append(num)
        array = []
        for i in negative:
            if len(i) == 0:
                continue
            else:
                array += i
        for i in positive:
            if len(i) == 0:
                continue
            else:
                array += i
        return array[-k]