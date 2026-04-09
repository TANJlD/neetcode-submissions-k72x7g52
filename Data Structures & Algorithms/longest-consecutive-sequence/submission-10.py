class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)

        count = 1
        cons = 1
        for num in nums:
            if (num-1) not in nums_set:
                n = num
                while True:
                    n += 1
                    if n in nums_set:
                        cons += 1
                        if cons > count:
                            count = cons                   
                    else:
                        cons = 1
                        break                

        return count
        
            
            
        