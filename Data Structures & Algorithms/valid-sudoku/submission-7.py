class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        grid = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                if board[r][c] in grid[tuple([r//3,c//3])]:
                    return False

                row[r].append(board[r][c])
                col[c].append(board[r][c])
                grid[tuple([r//3,c//3])].append(board[r][c])

        print(row)
        print(col)
        print(grid)
        
        return True
        