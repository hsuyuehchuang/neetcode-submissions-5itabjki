class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # up and left is pac,
        # down and right is atl
        # process first row, first col as pac
        # process last row, last col as atl
        # condition denied: visited, out of bound, val is smaller
        # dfs, search four directions
        # get the position are in pac set and atl set.
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or (r < 0 or c < 0 or r >= ROWS or c >= COLS) or (prevHeight < heights[r][c]):
                return 0
            visit.add((r, c))
            dfs(r + 1, c, visit, prevHeight)
            dfs(r - 1, c, visit, prevHeight)
            dfs(r, c + 1, visit, prevHeight)
            dfs(r, c - 1, visit, prevHeight)

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # process first row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # last row
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res