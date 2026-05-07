class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_speed = max(piles)
        while l <= r:
            speed = (l + r) // 2
            hours = calHours(piles, speed)

            if hours > h:
                l = speed + 1
            else:
                min_speed = min(min_speed, speed)
                r = speed - 1

        return min_speed



def calHours(piles, k):
    hours = 0

    for pile in piles:
        if (pile % k):
            h = (pile // k) + 1
        else:
            h = pile // k
        hours += h

    return hours



        
    