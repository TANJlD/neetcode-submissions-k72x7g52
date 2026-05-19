class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        first_half = nums[:len(nums)-k]
        sec_half = nums[len(nums)-k:]

        nums[:] = sec_half + first_half
        