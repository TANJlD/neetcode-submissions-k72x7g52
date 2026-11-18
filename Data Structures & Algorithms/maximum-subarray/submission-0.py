class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sub = 0

        for n in nums:
            if n > cur_sub+n:
                cur_sub = n
            else:
                cur_sub += n

            max_sum = max(max_sum, cur_sub)

        return max_sum