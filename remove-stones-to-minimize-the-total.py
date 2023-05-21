class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap = [-pile for pile in piles]
        heapq.heapify(maxheap)

        while k:
            top = heappop(maxheap)
            top = -top
            if top % 2 == 0:
                top = top // 2
            else:
                top = (top//2) + 1
            heappush(maxheap,-top)
            k-=1
        return -sum(maxheap)