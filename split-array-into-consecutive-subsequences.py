class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        graph = defaultdict(list)
        for num in nums:
            val =0
            if graph[num - 1]:
                heapify(graph[num - 1])
                val = heappop(graph[num - 1])
            graph[num].append(val + 1)

        for each in graph.values():
            for v in each:
                if v < 3:
                    return False

        return True