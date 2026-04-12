class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue 
            else:
                prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            else:
                postfix[i] = postfix[i+1] * nums[i+1]

        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]

        return result
        