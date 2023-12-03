class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        res = 0
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
                return 0
            if (i, j) in visit:
                return 0
            visit.add((i, j))
    
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
            return 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) and (i,j) not in visit:
                    dfs(i,j)
                    res += 1 
        return res 