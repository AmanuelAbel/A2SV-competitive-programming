class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapify(stones)
        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            if stone1 != stone2:
                heappush(stones,stone1-stone2)
        return 0 if len(stones)==0 else -stones[-1]