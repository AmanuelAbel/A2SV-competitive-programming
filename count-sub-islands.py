class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visit = set()
        counter = 0
        def dfs(r,c):
            if (r,c) in visit or r < 0 or c < 0 or r >= len(grid1) or c >= len(grid1[0]) or grid2[r][c] == 0:
                return True
            visit.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False
            res = dfs(r+1,c) and res
            res = dfs(r-1,c) and res
            res = dfs(r,c+1) and res
            res = dfs(r,c-1) and res
            return res
       
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] and (i,j) not in visit and dfs(i,j):
                    counter += 1
        return counter