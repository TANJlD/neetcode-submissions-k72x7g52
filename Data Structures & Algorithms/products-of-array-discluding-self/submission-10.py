class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        s = 1
        for i in range(n-1):
            s *= nums[i]
            prefix[i+1] = s
            
        s = 1
        for i in range(n-1, 0, -1):
            s *= nums[i]
            suffix[i-1] = s

        ans = []
        for i in range(n):
            ans.append(prefix[i] * suffix[i])

        return ans