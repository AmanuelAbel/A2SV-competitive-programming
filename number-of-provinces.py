class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        counter = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
        visited = set()
        def dfs(node):
            nonlocal visited
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr)
        for node in range(1,len(isConnected)+1):
            if node not in visited:
                dfs(node)
                counter += 1 
        return counter