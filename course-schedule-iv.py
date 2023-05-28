class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
       

        graph = [[] for _ in range(numCourses)]
        coursess = [0] * numCourses
        visited = defaultdict(set)
        for dep,cou in prerequisites:
            graph[cou].append(dep)
            coursess[dep] += 1
        
        queue = deque()

        ans = []
        for i in range(numCourses):
            if coursess[i] == 0:
                queue.append(i)

        while queue:
            x = queue.popleft()
            for i in graph[x]:
                coursess[i] -= 1
                for j in visited[x]:
                    visited[i].add(j)
                visited[i].add(x)
                if coursess[i] == 0:
                     queue.append(i)
        for i, j in queries:
            if j in visited[i]:
                ans.append(True)
            else:
                ans.append(False)
                    
                    
        return ans