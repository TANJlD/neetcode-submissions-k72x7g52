class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for num in nums:
            count = 1
            if (num - 1) not in nums_set:
                while True:
                    num += 1
                    if num not in nums_set:
                        break
                    count += 1
                if count > result:
                    result = count

        return result
                    

        