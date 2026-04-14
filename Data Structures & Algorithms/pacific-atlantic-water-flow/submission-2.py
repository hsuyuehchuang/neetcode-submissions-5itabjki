class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # up and left is pac,
        # down and right is atl
        # process first row, first col as pac
        # process last row, last col as atl
        # 這題水要逆流而上 (curr height >= prev height) 才可以繼續往下走
        # not (curr height >= prev height) = (curr height < prev height) = (heights[r][c] < prev height)
        # condition denied: visited, out of bound
        # dfs, search four directions
        # get the position are in pac set and atl set.
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or (r < 0 or c < 0 or r >= ROWS or c >= COLS) or (heights[r][c] < prevHeight):
                return 0
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

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