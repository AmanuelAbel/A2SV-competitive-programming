class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        rank = [1]*len(s)
        graph = defaultdict(list)
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
        for a,b in pairs:
            Union(a,b)
        
        for i in range(len(s)):
            z = Find(i)
            graph[z].append(s[i])
        for i in graph:
            graph[i].sort()
        res =""
        for i in range(len(s)):
            z = Find(i)
            res += graph[z][0]
            graph[z].pop(0)
        return res