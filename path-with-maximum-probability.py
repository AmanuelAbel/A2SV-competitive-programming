class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        def shortestPath(edges, n, src):
            adj = defaultdict(list)
            for i in range(1, n + 1):
                adj[i] = []

            for s, d, w in edges:
                adj[s].append([d, w])

            shortest = {}
            predecessor = {}  
            minHeap = [[1, src, None]]  
            while minHeap:
                w1, n1, pred = heapq.heappop(minHeap)
                if n1 in shortest:
                    continue
                shortest[n1] = w1
                predecessor[n1] = pred  
                for n2, w2 in adj[n1]:
                    if n2 not in shortest:
                        if w1*w2 < 0:
                            heapq.heappush(minHeap, [w1 * w2, n2, n1])
                        else:
                            heapq.heappush(minHeap, [-w1 * w2, n2, n1])

            return shortest, predecessor
        for i in range(len(edges)):
            rev = edges[i][::-1]
            edges.append(rev)
        for i in range(len(edges)):
            edges[i].append(-succProb[i%len(succProb)])
        res , ans = shortestPath(edges,len(edges),start_node)
        return -res[end_node] if end_node in res else 0