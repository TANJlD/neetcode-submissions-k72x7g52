class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m 
            elif target > nums[m]:
                if nums[m] >= nums[l]:
                    l = m + 1
                elif nums[m] < nums[l]:
                    if nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1

            elif target < nums[m]:
                if nums[m] <= nums[r]:
                    r = m - 1
                elif nums[m] > nums[r]:
                    if nums[l] <= target:
                        r = m - 1
                    else:
                        l = m + 1

        return -1