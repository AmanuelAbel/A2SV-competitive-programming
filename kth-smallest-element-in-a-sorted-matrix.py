class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
            
        rows, cols = len(matrix), len(matrix[0])
        heap = []

        for row in range(rows):
            heapq.heappush(heap, (matrix[row][0], row, 0))

        for _ in range(k - 1):
            _, row, col = heapq.heappop(heap)

            if col + 1 < cols:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return heap[0][0]