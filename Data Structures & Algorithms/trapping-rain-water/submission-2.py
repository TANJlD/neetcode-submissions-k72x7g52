class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        mx = max(height)

        for i, num in enumerate(height):
            if num == mx:
                mid = i
                break

        i = 0
        while i < mid - 1:
            j = i
            junk = 0
            while j < mid:
                j += 1
                if height[j] >= height[i]:
                    cav = min(height[i], height[j]) * (j - i - 1)
                    cav -= junk
                    area += cav
                    break
                else:
                    junk += height[j]
            i = j

        i = len(height) - 1
        while i > mid + 1:
            j = i
            junk = 0
            while j > mid:
                j -= 1
                if height[j] >= height[i]:
                    cav = min(height[i], height[j]) * (i - j - 1)
                    cav -= junk
                    area += cav
                    break
                else:
                    junk += height[j]
            i = j

        return area

