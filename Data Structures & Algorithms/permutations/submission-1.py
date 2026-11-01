class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [nums]
       
        result = []
        permutations = self.permute(nums[1:])

        for per in permutations:
            for i in range(len(per) + 1):
                copy = per.copy()
                copy.insert(i, nums[0])
                result.append(copy)

        return result
            