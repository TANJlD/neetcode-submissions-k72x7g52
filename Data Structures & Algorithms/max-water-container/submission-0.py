class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            con = 0
            for j in range(i+1, len(height)):
                if height[i] <= height[j]:
                    con = height[i] * (j-i)
                elif height[j] <= height[i]:
                    con = height[j] * (j-i)
                if con > max:
                    max = con
        return max
        