class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        visited = set()
        fresh = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
        if not fresh:
            return 0
        while queue:
            z = len(queue)
            for i in range(z):
                (r,c) = queue.pop(0)
                if grid[r][c] == 1:
                    fresh -= 1
                grid[r][c] = 2
                if r+1 < len(grid) and grid[r+1][c] == 1 and (r+1,c) not in queue:
                    queue.append((r+1,c))
                if r-1 >= 0 and grid[r-1][c] == 1 and (r-1,c) not in queue:
                    queue.append((r-1,c))
                if c+1 < len(grid[0]) and grid[r][c+1] == 1 and (r,c+1) not in queue:
                    queue.append((r,c+1))
                if c-1 >= 0 and grid[r][c-1] == 1 and (r,c-1) not in queue:
                    queue.append((r,c-1))
                
            time += 1
        return time-1 if fresh == 0 else -1