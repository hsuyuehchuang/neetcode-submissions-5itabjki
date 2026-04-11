class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque() # for the efficiency of popleft()
            q.append((r, c)) 
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()
                for dr, dc in directions: # find adjacent cell
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        
        return res

