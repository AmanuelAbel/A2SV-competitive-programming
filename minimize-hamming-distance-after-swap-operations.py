class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        rep = {i: i for i in range(n)}
        rank = [1] * (n)

        def find(x):
            while rep[x] != x:
                x = rep[x]
            return x

        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)

            if x_rep != y_rep:
                if rank[x_rep] >= rank[y_rep]:
                    rep[y_rep] = rep[x_rep]
                    rank[x_rep] += rank[y_rep]
                else:
                    rep[x_rep] = rep[y_rep]
                    rank[y_rep] += rank[x_rep]
                return 
        
        for i, j in allowedSwaps:
            union(i,j)
        
        parent = defaultdict(list)
        for i in range(len(source)):
            parent[find(i)].append(i)

        ans = 0
        for swap in parent.values():
            count = Counter(list(map(lambda i: source[i], swap)))
        
            for i in swap:
                if target[i] not in count or count[target[i]] < 1:   
                    ans += 1
                else:
                    count[target[i]] -= 1

        return ans