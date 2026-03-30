class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_info = {}
        row_info = {}
        col_info = {}
        for row in range(len(board)):
            row_info[row] = []
            for col in range(len(board[0])):
                if col not in col_info:
                    col_info[col] = []

                #checking row
                if board[row][col] in row_info[row] and board[row][col] != '.':
                    return False
                else:
                    row_info[row].append(board[row][col])

                #checking cols
                if board[col][row] in col_info[row] and board[col][row] != '.':
                    return False
                else:
                    col_info[row].append(board[col][row])
                
                #check boxes
                box_row = row//3
                box_col = col//3
                box = box_row * 3 + box_col
                if box not in box_info:
                    box_info[box] = []
                if board[row][col] in box_info[box] and board[row][col] != '.':
                    return False
                else:
                    box_info[box].append(board[row][col])

        return True