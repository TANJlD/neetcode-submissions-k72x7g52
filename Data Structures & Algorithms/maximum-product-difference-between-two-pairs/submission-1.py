class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a, b = float("-inf"), float("-inf")
        c, d = float("inf"), float("inf")

        for n in nums:
            if n > a:
                b = a
                a = n
            elif n > b:
                b = n

            if n < c:
                d = c
                c = n
            elif n < d:
                d = n

        return (a * b) - (c * d)