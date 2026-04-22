class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = zip(position, speed)
        ps = sorted(ps, reverse=True)

        fleet = 0
        max_time = 0
        for p, s in ps:
            time = (target-p) / s
            if time > max_time:
                fleet += 1
                max_time = time
        
        return fleet
