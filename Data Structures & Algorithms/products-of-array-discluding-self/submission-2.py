class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        zero = 0
        for num in nums:
            if num != 0:
                total = total * num
            if num == 0:
                zero += 1 

        for self in nums:
            if zero > 1:
                res.append(0)
            elif zero == 1:
                if self == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // self)
            
        return res

        