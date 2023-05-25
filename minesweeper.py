class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (-1, 1), (1, -1)]

        def count_adjacent_mines(row, col):
            count = 0
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == 'M':
                    count += 1
            return count

        def dfs(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            elif board[row][col] == 'E':
                count = count_adjacent_mines(row, col)
                if count > 0:
                    board[row][col] = str(count)
                    return
                board[row][col] = 'B'
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        dfs(new_row, new_col)

        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            dfs(row, col)
        return board