class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = []
        right = []

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(nums[i-1] * left[i-1])
        l = len(nums)
        for i in range(l-1, -1, -1 ):
            if i == l-1:
                right.append(1)
            else:
                right.append(nums[i+1] * right[len(right)-1])

        # print(left,right)

        for i in range(len(nums)):
            res.append(left[i] * right[(l-1)-i])

        return res

        