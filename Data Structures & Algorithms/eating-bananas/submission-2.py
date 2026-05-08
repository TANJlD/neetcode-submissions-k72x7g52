class Solution: 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l+r) // 2

            hours = sum((pile+k-1) // k for pile in piles)

            if hours <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1
            
        return ans
        
        