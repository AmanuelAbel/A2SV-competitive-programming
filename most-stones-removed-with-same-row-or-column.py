class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        stones.sort()
        res = 0
        visit = set()
        for a, b in stones:
            parent[(a, b)] = (a, b)
        
        rank = [1] * len(stones)

        def Find(n):
            if parent[n] != n:
                parent[n] = Find(parent[n])
            return parent[n]

        def Union(a, b):
            x = Find(a)
            y = Find(b)
            if x == y:
                return 
            parent[x] = y
            return 

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                a, b = stones[i]
                c, d = stones[j]
                if a == c or b == d:
                    Union((a, b), (c, d))
        for a,b in stones:
            visit.add(Find((a,b)))
        return len(stones) - len(visit)