class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            con = min(heights[l], heights[r]) * (r-l)
            if con > max:
                max = con

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max
            
        