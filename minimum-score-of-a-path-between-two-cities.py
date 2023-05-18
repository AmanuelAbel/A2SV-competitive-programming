class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        minpath = 10**4
        parent = {i:i for i in range(1,n+1)}
        rank = {i:1 for i in range(1,n+1)}
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
        for a,b,res in roads:
            Union(a,b)
        for a,b,res in roads:
            if res < minpath:
                if Find(1) == Find(a) == Find(b):
                    minpath = res
        return minpath