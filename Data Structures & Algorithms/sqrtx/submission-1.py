class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            m = (l + r) // 2
            s = m * m
            if x < s:
                r = m - 1
            elif x > s:
                l = m + 1
                res = m
            else:
                return m

        return res
                