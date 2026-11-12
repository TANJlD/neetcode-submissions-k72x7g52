class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def find(r, c, seen, i):
            nonlocal row
            nonlocal col
            if i == len(word):
                return True

            if 0 <= r+1 < row and 0 <= c < col and board[r+1][c] == word[i] and (r+1, c) not in seen:
                seen.append((r+1, c))
                if find(r+1, c, seen, i+1):
                    return True
                seen.pop()
            if 0 <= r-1 < row and 0 <= c < col and board[r-1][c] == word[i] and (r-1, c) not in seen:
                seen.append((r-1, c))
                if find(r-1, c, seen, i+1):
                    return True
                seen.pop()
            if 0 <= r < row and 0 <= c+1 < col and board[r][c+1] == word[i] and (r, c+1) not in seen:
                seen.append((r, c+1))
                if find(r, c+1, seen, i+1):
                    return True
                seen.pop()
            if 0 <= r < row and 0 <= c-1 < col and board[r][c-1] == word[i] and (r, c-1) not in seen:
                seen.append((r, c-1))
                if find(r, c-1, seen, i+1):
                    return True 
                seen.pop()

            return False


        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and find(r, c, [(r, c)],  1):
                     return True
        return False