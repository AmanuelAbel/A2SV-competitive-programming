class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf') 

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] > mat[x][y] + 1:
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append((nx, ny))

        return mat