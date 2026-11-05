class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            nums = matrix[m]

            if nums[0] > target:
                r = m - 1
            elif nums[-1] < target:
                l = m + 1
            else:
                break

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            n = nums[m] 

            if n > target:
                r = m - 1
            elif n < target:
                l = m + 1
            else:
                return True

        return False