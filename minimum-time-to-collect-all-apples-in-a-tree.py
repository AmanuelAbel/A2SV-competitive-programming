class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            total_time = 0

            for neighbor in graph[node]:
                if neighbor not in visited:
                    sub_time = dfs(neighbor)
                    if sub_time > 0 or hasApple[neighbor]:
                        total_time += sub_time + 2

            return total_time

        return dfs(0)