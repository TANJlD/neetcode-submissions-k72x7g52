class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0

        l = 0
        r = len(people) - 1

        while l <= r:
            if l == r:
                count += 1
                break
            pair = people[l] + people[r]

            if pair > limit:
                r -= 1
                count +=1 
            else:
                count += 1
                l += 1
                r -= 1

        return count