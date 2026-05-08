class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr = nums
        l = 0
        r = len(nums) - 2

        while l <= r:
            m = (l+r) // 2

            if arr[m] > arr[m+1]:
                return arr[m+1]

            else:
                if arr[m] >= arr[0]:
                    l = m + 1
                elif arr[m] < arr[0]:
                    r = m - 1 

        return arr[0]
        