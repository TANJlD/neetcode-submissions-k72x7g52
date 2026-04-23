class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lLimit = [i for i in range(len(heights))]
        rLimit = [i for i in range(len(heights)-1, -1, -1)]

        stack = []
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                idx = stack.pop()
                rLimit[idx] = i - idx - 1
            stack.append(i)
        
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                lLimit[idx] = idx - i - 1
            stack.append(i)

        print(lLimit, rLimit)

        result = 0
        for i, h in enumerate(heights):
            result = max(result, (lLimit[i]+rLimit[i]+1) * h)

        return result 
        