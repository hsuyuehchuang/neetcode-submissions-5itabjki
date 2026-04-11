class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res
                
                
        

# start from [0,0]
# if start cell == 0, find next until cell equals to one
# searching four direction
# dfs(r, c) or ...
# if next number == 0 or out of boundary return True
# if all false: res += 1
# 
# mark 走過的 cell = -1
