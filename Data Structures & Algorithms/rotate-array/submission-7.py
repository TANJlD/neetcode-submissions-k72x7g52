class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = start = 0

        while count < n:
            prev = nums[start]
            curr_indx = start
            while True:
                next_indx = (curr_indx + k) % n

                temp = nums[next_indx]
                nums[next_indx] = prev
                prev = temp

                curr_indx = next_indx

                count += 1

                if curr_indx == start:
                    break

            start += 1

