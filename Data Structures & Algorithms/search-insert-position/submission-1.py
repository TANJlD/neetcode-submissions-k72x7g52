class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                if m != len(nums)-1 and target < nums[m+1]:
                    return m+1
                l = m + 1
            elif target < nums[m]:
                if m != 0 and target > nums[m-1]:
                    return m
                r = m - 1
            else:
                return m

        
        