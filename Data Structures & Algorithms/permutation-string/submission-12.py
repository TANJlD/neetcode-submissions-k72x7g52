class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26
        matches = 0

        for i in range(len(s1)):
            indx1 = ord(s1[i]) - ord("a")
            indx2 = ord(s2[i]) - ord("a")

            freq1[indx1] += 1
            freq2[indx2] += 1

        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            indx = ord(s2[r]) - ord("a")
            freq2[indx] += 1
            if freq2[indx] == freq1[indx]:
                matches += 1
            if freq2[indx] - 1 == freq1[indx]:
                matches -= 1

            indx = ord(s2[l]) - ord("a")
            freq2[indx] -= 1
            if freq2[indx] == freq1[indx]:
                matches += 1
            if freq2[indx] + 1 == freq1[indx]:
                matches -= 1
            l += 1
            
        return matches == 26










