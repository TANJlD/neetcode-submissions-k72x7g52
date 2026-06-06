class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c in s1:
            freq1[c] += 1

        for c in s2[:len(s1)]:
            freq2[c] += 1

        if freq1 == freq2:
            return True


        l = 0
        r = len(s1)

        while r < len(s2):
            freq2[s2[r]] += 1
            freq2[s2[l]] -= 1
            
            if freq2[s2[l]] == 0:
                del freq2[s2[l]]

            if freq1 == freq2:
                return True

            r += 1
            l += 1

            print(freq2)

        return False
        