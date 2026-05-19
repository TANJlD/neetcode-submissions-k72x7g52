class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)

        first_half = nums[:len(nums)-k]
        sec_half = nums[len(nums)-k:]
        print(first_half, sec_half, k)
        new_arr = sec_half + first_half
        print(new_arr)
        nums[:] = new_arr[:]