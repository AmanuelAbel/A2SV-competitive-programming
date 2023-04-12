class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        z = image[sr][sc]
        def dfs(r,c):
            if r<0 or c < 0 or r >= len(image) or c >= len(image[0]) or (r,c) in visit or image[r][c] != z:
                return 
            visit.add((r,c))
            image[r][c] = color
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
            return 
        dfs(sr,sc)
        return image