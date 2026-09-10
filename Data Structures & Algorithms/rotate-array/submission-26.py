class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        temp = nums[0]
        sindx = 0
        cindx = 0
        dindx = 0
        for i in range(n):
            dindx = (cindx+k) % n
            temp, nums[dindx] = nums[dindx], temp

            if dindx == sindx and k > 0:
                sindx = dindx + 1
                cindx = dindx + 1
                temp = nums[dindx + 1]
            else:
                cindx = dindx

            