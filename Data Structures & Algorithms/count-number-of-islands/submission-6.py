class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res



# iterata through every cell in the grid
# when a cell with value "1" is found:
    # res += 1
    # run dfs(r, c)
# in dfs:
    # if cell is out of bounds or is "0", return.
    # mark the current cell as "0" (visited)
    # recursively explore all 4 directions (up, down, left, right)
# continue untill all cells are processed
# return res
