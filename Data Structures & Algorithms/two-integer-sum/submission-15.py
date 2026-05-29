class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            deff = target-num
            if deff in map:
                return sorted([i, map[deff]])

            map[num] = i
        