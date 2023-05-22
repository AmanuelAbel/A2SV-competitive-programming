class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        result = [-1] * n  

        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)

        def dfs(node):
            if result[node] >= 0:
                return result[node] 

            result[node] = node

            for neighbor in graph[node]:
                if quiet[result[node]] > quiet[dfs(neighbor)]:
                    result[node] = result[neighbor]  

            return result[node]

        for i in range(n):
            dfs(i)

        return result