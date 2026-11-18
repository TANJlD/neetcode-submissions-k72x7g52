class Node:
    def __init__(self):
        self.childs = {}
        self.is_word = False

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = Node()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.childs:
                    curr.childs[c] = Node()
                curr = curr.childs[c]
            curr.is_word = True

        result = set()
        seen = set()
        curr_word = []
        m, n = len(board), len(board[0])

        def find(row, col, node): 
            if node.is_word:
                word = "".join(curr_word)
                if word not in result:
                    result.add(word)     
            if (
                (row, col) in seen or
                not 0 <= row < m or 
                not 0 <= col < n or 
                board[row][col] not in node.childs
            ): return

            c = board[row][col]
            curr_word.append(c)
            seen.add((row, col))

            
            
            find(row+1, col, node.childs[c])
            find(row-1, col, node.childs[c])
            find(row, col+1, node.childs[c])
            find(row, col-1, node.childs[c])

            curr_word.pop()
            seen.remove((row, col))


        for r in range(m):
            for c in range(n):
                char = board[r][c]
                if char in root.childs:
                    find(r, c, root)

        return list(result) 