class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def visitIsland(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >=COLS or (r, c) in visited or grid[r][c] == '0':
                return
            visited.add((r, c))

            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for r, c in directions:
                visitIsland(r, c)
            return
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    islands += 1
                    visitIsland(r, c)
        return islands



