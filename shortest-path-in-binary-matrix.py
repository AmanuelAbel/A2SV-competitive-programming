class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        queue = [(0,0)]
        path = 0
        z = len(grid) - 1
        if grid[z][z-1] == grid[z-1][z-1] == grid[z-1][z] == 1:
            return -1
        while queue:
            for i in range(len(queue)):
                (r,c) = queue.pop(0)
                if r == c == len(grid)-1:
                    return path + 1
                grid[r][c] = 1
                if r+1 < len(grid) and grid[r+1][c] == 0 and (r+1,c) not in queue:
                    queue.append((r+1,c))
                if r-1 >= 0 and grid[r-1][c] == 0 and (r-1,c) not in queue:
                    queue.append((r-1,c))
                if c+1 < len(grid[0]) and grid[r][c+1] == 0 and (r,c+1) not in queue:
                    queue.append((r,c+1))
                if c-1 >= 0 and grid[r][c-1] == 0 and (r,c-1) not in queue:
                    queue.append((r,c-1))
                if r+1 < len(grid) and c+1 < len(grid[0]) and grid[r+1][c+1] == 0 and (r+1,c+1) not in queue:
                    queue.append((r+1,c+1))
                if r+1 < len(grid) and c-1 >= 0 and grid[r+1][c-1] == 0 and (r+1,c-1) not in queue:
                    queue.append((r+1,c-1))
                if r-1 >= 0 and c+1 < len(grid[0]) and grid[r-1][c+1] == 0 and (r-1,c+1) not in queue:
                    queue.append((r-1,c+1))
                if r-1 >= 0 and c-1 >= 0 and grid[r-1][c-1] == 0 and (r-1,c-1) not in queue:
                    queue.append((r-1,c-1))
            path += 1
        return -1