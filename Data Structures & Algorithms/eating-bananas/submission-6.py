class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slow = 1
        fast = max(piles)
        min_speed = fast

        while slow <= fast:
            m = (slow + fast) // 2
            hours = self.countHours(piles, m)
            if hours > h:
                slow = m + 1
            elif hours <= h:
                fast = m - 1
                min_speed = min(min_speed, m)
        
        return min_speed



    def countHours(self, piles, speed):
        hours = 0

        for bananas in piles:
            if (bananas % speed) != 0:
                hours += (bananas // speed) + 1
            else:
                hours += bananas // speed

        return hours
