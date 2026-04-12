class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        h = num // 2

        l = 0
        r = h
        m = h // 2

        while l <= r:
            m = (l + r) // 2
            if m * m > num:
                r = m - 1
            elif m * m < num:
                l = m + 1
            else:
                return True

        return False
        