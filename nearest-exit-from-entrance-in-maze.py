class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque([(entrance[0], entrance[1], 0)]) 
        maze[entrance[0]][entrance[1]] = '+' 

        while queue:
            x, y, steps = queue.popleft()

            if (x != entrance[0] or y != entrance[1]) and (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
                return steps  

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'  
                    queue.append((nx, ny, steps + 1))

        return -1