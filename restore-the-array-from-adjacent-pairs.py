class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for pair in adjacentPairs:
            u, v = pair
            graph[u].append(v)
            graph[v].append(u)

        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break

        queue = deque([(start, None)])  
        visited = set([start]) 
        array = []

        while queue:
            node, parent = queue.popleft()
            array.append(node)

            for neighbor in graph[node]:
                if neighbor != parent and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))

        return array