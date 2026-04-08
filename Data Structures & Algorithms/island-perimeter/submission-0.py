class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0
        in_edge = 0 # internal_edge

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island += 1
                    if r >= 1 and grid[r-1][c] == 1:
                        in_edge += 1
                    if c >= 1 and grid[r][c-1] == 1:
                        in_edge += 1
        return 4 * island - 2 * in_edge