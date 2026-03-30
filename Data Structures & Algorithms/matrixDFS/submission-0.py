class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set() #(r, c)
        start_r = 0
        start_c = 0
        def dfs(grid, r, c, visted):
            ROWS = len(grid)
            COLS = len(grid[0])
            if (r < 0 or c < 0) or (r == ROWS) or (c == COLS) or ((r,c) in visited) or (grid[r][c] == 1):
               return 0
            
            if (r == ROWS - 1) and (c == COLS - 1):
                return 1
            
            visited.add((r,c))

            count = 0
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r, c - 1, visited)
            count += dfs(grid, r, c + 1, visited)

            visited.remove((r,c))
            return count

        return dfs(grid, start_r, start_c, visited)