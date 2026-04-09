class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1

        s = nums[0]
        for num in nums:
            if num < s:
                s = num
        l = nums[0]
        for num in nums:
            if num > l:
                l = num

        if (s == l):
            return 1
    
        nums_set = set(nums)

        count = 1
        c = 1
        cons = s
        for i in range(s, l):
            cons += 1
            if cons in nums_set:
                c += 1
                if c > count:
                    count = c
            else:
                c = 0
        
        return count

