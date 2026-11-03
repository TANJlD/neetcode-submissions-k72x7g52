class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            c = 0
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                subset.append(nums[i])
                c += 1
                i += 1

            subset.append(nums[i])
            dfs(i+1)
            
            while c:
                subset.pop()
                c -= 1
                i -= 1
                
            subset.pop()
            dfs(i+1)

        dfs(0)
        return result