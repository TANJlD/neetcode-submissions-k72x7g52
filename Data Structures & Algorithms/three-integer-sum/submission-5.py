class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):

            l = i+1
            r = len(nums) - 1
        
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in result:

                        result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
              
        return result  