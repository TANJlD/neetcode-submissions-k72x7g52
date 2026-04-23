class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rec = 0

        for i, h in enumerate(heights):
            l = i 
            while l > 0:
                if heights[l-1] < h:
                    break
                l -= 1

            r = i
            while r < len(heights)-1:
                if heights[r+1] < h:
                    break
                r += 1

            max_rec = max(max_rec, h * (r-l+1))

        return max_rec

             
            
        