class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def is_magic_square(subgrid):
            unique_elements = set()
            for row in subgrid:
                for element in row:
                    if element < 1 or element > 9 or element in unique_elements:
                        return False
                    unique_elements.add(element)

            row_sums = [sum(row) for row in subgrid]
            col_sums = [sum(col) for col in zip(*subgrid)]
            diag_sum1 = subgrid[0][0] + subgrid[1][1] + subgrid[2][2]
            diag_sum2 = subgrid[0][2] + subgrid[1][1] + subgrid[2][0]
            sums = row_sums + col_sums + [diag_sum1, diag_sum2]
            if len(set(sums)) != 1:
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [[grid[i+r][j+c] for c in range(3)] for r in range(3)]
                if is_magic_square(subgrid):
                    count += 1

        return count