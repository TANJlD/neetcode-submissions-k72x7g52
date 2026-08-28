class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rown = len(matrix)
        coln = len(matrix[0])
        l = 0
        r = (rown * coln) - 1

        while l <= r:
            m = (l + r) // 2
            row = m // coln
            col = m % coln 

            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True

        return False
