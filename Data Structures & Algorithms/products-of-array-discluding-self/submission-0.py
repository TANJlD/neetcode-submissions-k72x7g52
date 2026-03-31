class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for self in nums:
            exSelf = nums.copy()
            exSelf.remove(self)
            pro = 1
            for i in exSelf:
                pro = pro * i
            res.append(pro)
        return res
        