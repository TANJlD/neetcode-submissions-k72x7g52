class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if (
                    board[i][j] in row[i] or
                    board[i][j] in col[j] or
                    board[i][j] in grid[((i//3)*3) + (j//3)]
                ):
                    return False
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    grid[((i//3)*3) + (j//3)].add(board[i][j])

        return True