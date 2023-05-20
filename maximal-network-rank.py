class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections = [[0] * n for _ in range(n)]
        degrees = [0] * n

        for a, b in roads:
            connections[a][b] = 1
            connections[b][a] = 1
            degrees[a] += 1
            degrees[b] += 1

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degrees[i] + degrees[j] - connections[i][j]
                max_rank = max(max_rank, rank)

        return max_rank