class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postArray = [0] * len(nums)

        postfix = 0
        for i in range(len(nums)-1, -1, -1):
            postArray[i] = postfix
            postfix += nums[i]

        print(postArray)

        prefix = 0
        
        for i in range(len(nums)):
            if prefix == postArray[i]:
                return i
            prefix += nums[i]

        return -1





        