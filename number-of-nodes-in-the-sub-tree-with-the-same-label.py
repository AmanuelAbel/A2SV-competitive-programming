class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        result = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            counts = [0] * 26  
            label = ord(labels[node]) - ord('a') 

            for child in graph[node]:
                graph[child].remove(node)
                child_counts = dfs(child) 
                for i in range(26):
                    counts[i] += child_counts[i]

            counts[label] += 1  
            result[node] = counts[label]

            return counts

        dfs(0)

        return result