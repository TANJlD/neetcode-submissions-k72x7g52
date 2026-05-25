class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            t, b = l, r

            for i in range(r-l):
                top_left = matrix[t][l+i]

                # top left <--- bottom left
                matrix[t][l+i] = matrix[b-i][l]

                # bottom left <--- bottom right
                matrix[b-i][l] = matrix[b][r-i]

                # bottom right <--- top right
                matrix[b][r-i] = matrix[t+i][r]

                # top right <--- top left
                matrix[t+i][r] = top_left
            
            l += 1
            r -= 1

