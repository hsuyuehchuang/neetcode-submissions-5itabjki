class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # bfs, check four directions
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            perimeter = 0
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
                
        return 0
