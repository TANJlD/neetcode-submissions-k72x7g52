class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)-1, -1, -1):
                if j == 0:
                    nums[j] = temp
                else:
                    nums[j] = nums[j-1]
                