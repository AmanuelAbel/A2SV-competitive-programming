class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent = [0]*n
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
                return True
            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[x] = y
                rank[y] = rank[y] + 1
            return False
        for i in range(n-1):
            res = Union(edges[i][0],edges[i][1])
            if res:
                return [edges[i][0],edges[i][1]]