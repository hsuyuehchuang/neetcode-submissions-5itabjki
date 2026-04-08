
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r - 1 < 0 or grid [r-1][c] == 0:
                        res += 1
                    if r + 1 >= rows or grid [r+1][c] == 0:
                        res += 1
                    if c - 1 < 0 or grid[r][c-1] == 0:
                        res += 1
                    if c + 1 >= cols or grid [r][c+1] == 0:
                        res += 1
        return res
        