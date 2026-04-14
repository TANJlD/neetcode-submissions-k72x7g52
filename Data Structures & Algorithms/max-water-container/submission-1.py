class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def findMax(heights):
            max = 0
            for i in range(len(heights)-1):
                far = len(heights) - 1
                con1 = calCon(heights[i], heights[far], (far-i))
                far -= 1
                con2 = 0
                while far > i:
                    con = calCon(heights[i], heights[far], (far-i))
                    far -= 1
                    if con > con2:
                        con2 = con
                
                lar = 0
                if con1 > con2:
                    lar = con1
                else:
                    lar = con2
                
                if lar > max:
                    max = lar 
            
            return max

        

        def calCon(right, left, distance):
            if left <= right:
                return left * distance
            else:
                return right * distance 

        return findMax(heights)
            



        