class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        queue = collections.deque()
        seen.add((0,0))
        queue.append((0,0))

        if grid[0][0] != 0:
            return -1

        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length + 1
                
                dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
                for dr, dc in dirs:
                    if (r + dr, c + dc) in seen or min(r+dr, c+dc) < 0  or r + dr == ROWS or c + dc == COLS or grid[r+dr][c+dc] == 1:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    seen.add((r + dr, c + dc))

            length += 1
        
        return -1