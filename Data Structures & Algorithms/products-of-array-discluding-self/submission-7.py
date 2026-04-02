class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # left pass
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]

        # right pass
        r = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= r
            r *= nums[i]

        return result


        