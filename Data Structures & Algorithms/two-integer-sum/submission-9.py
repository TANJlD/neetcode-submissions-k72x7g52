class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            num = target - nums[i]
            if num in map and i != map[num]:
                return sorted([i, map[num]])

                    
                    
            
        