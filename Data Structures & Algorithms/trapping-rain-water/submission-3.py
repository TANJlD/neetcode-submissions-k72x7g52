class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                prefix[i] = height[i]
            else:
                prefix[i] = max(height[i], prefix[i-1])
        
        suffix = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(height[i], suffix[i+1])

        print(prefix)
        print(suffix)

        water = 0
        for i, h in enumerate(height):
            count = min(prefix[i], suffix[i]) - h
            if count > 0:
                water += count

        return water

            
            
            
        