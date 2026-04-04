class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(board):
            for row in board:
                if not check(row):
                    return False
            return True


        def checkColumn(board):
            for i in range(9):
                column = []
                for row in board:
                    column.append(row[i])
                if not check(column):
                    return False
            return True


        def checkGrid(board):
            m, n = 0, 3
            while n < 10:
                i, j = 0, 3
                while j < 10:
                    grid = []
                    for chunk in board[m:n]:
                        for e in chunk[i:j]:
                            grid.append(e)
                    print(grid)
                    if not check(grid):
                        return False
                    i += 3
                    j += 3
                m += 3
                n += 3
            return True


        def check(chunk):
            for e in chunk:
                if e == ".":
                    pass
                else:
                    c = chunk.count(e)
                    if c > 1:
                        return False
            return True     


        if not checkRow(board):
            return False
        elif not checkColumn(board):
            return False
        elif not checkGrid(board):
            return False
        else:
            return True  