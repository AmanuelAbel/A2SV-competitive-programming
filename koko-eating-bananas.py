class Solution:
    def loooop(self,piles: List[int],k):
        totalTime = 0
        for p in piles:
                totalTime += math.ceil(p / k)
        return totalTime

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            totalTime = self.loooop(piles,k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res