class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [0]*n
        if n == 1:
            return True
        for i in range(n):
            parent[i] = i
        rank = [1]*n
        def Find(n):
            if parent[n] != n:
                parent[n] = Find(parent[n])
            return parent[n]
        def Union(a, b):
            x = Find(a)
            y = Find(b)
            if x == y:
                return 
            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[x] = y
                rank[y] = rank[y] + 1
            return 
        res = n
        for i in range(len(edges)):
            Union(edges[i][0],edges[i][1])
        if Find(source) == Find(destination):
            return True