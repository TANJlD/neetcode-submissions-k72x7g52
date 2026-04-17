class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPro = [1] * len(nums)
        rightPro = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            leftPro[i] = leftPro[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            rightPro[i] = rightPro[i+1] * nums[i+1]

        result = []

        for i in range(len(nums)):
            result.append(leftPro[i] * rightPro[i])

        return result
