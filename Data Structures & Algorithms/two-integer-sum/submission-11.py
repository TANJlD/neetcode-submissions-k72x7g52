class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i, num in enumerate(nums):
            dif = target - num
            if dif in map and i != map[dif]:
                return sorted([i, map[dif]])

                    
                    
            
        