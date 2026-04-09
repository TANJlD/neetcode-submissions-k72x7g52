class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()

        print(nums)

        count = 1
        c = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                c += 1
                if c > count:
                    count = c
            else: 
                c = 1

        return count
        