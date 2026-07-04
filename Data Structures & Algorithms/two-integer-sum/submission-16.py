class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}

        for i, num in enumerate(nums):
            if (target - num) not in match:
                match[num] = i
            else:
                return [match[target - num], i]
