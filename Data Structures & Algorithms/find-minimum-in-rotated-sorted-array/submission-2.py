class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 2
        while l <= r:
            m = (l+r) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            else:
                if nums[m] >= nums[0]:
                    l = m + 1
                else:
                    r = m - 1 

        return nums[0]
        