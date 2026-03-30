class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxs = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r]:
                    return False
                rows[r].append(board[r][c])

                if board[r][c] in cols[c]:
                    return False
                cols[c].append(board[r][c])

                grid_pos = (r//3, c//3)
                if board[r][c] in boxs[grid_pos]:
                    return False
                boxs[grid_pos].append(board[r][c])

        return True
        
    
        