class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs, check one direction until the end
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= c < cols and 0 <= r < rows) or grid[r][c] == 0:
                # If out of bounds or water, add one to the perimeter.
                return 1
            if grid[r][c] == -1:
                # Return 0 if the block has been visited.
                return 0
            grid[r][c] = -1

            return (dfs(r-1, c) + dfs(r+1, c) +
                    dfs(r, c-1) + dfs(r, c+1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        # If the entire grid is water, return 0 for the perimeter
        return 0