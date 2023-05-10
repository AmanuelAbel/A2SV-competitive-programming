class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0]* numCourses
        res = []
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0]) 
            indegrees[prerequisites[i][0]] += 1
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            top = queue.popleft()
            res.append(top)
            for i in graph[top]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        print(res)
        return len(res) == numCourses