class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        prifix = 0
        for i, num in enumerate(nums):
            if (total-num) / 2 == prifix:
                return i
            prifix += num
            
        return -1






        