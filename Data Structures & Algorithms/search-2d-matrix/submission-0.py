class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = []
        while l <= r:
            m = (l+r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = matrix[m]
                break

        l = 0 
        r = len(row) - 1
        while l <= r:
            m = (l+r) // 2
            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True
        return False
                
        
                
        
        