class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = []
        right = []

        l = len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                left.append(num)
            else:
                left.append(num * left[i-1])

        for i, num in enumerate(reversed(nums)):
            if i == 0:
                right.append(num)
            else:
                right.append(num * right[i-1])

        right.reverse()

        for i, num in enumerate(nums):
            if i == 0:
                res.append(right[i+1])
            elif i == (l-1):
                res.append(left[-2])
            else:
                res.append(left[i-1] * right[i+1])

        # print(left, right)
        return res


        