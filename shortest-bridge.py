class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def markFirstIsland(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                return
            grid[row][col] = 2
            for dx, dy in directions:
                markFirstIsland(row + dx, col + dy)

        def expandFirstIsland():
            queue = deque()
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        queue.append((i, j, 0))

            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] == 2:
                        continue
                    if grid[nx][ny] == 1:
                        return dist
                    grid[nx][ny] = 2
                    queue.append((nx, ny, dist + 1))

        marked = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    markFirstIsland(i, j)
                    marked = True
                    break
            if marked:
                break

        return expandFirstIsland()