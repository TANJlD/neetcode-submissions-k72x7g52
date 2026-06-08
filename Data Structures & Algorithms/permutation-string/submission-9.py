class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1
        
        matches = 0

        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1


        l = 0
        r = len(s1)

        while r < len(s2):
            if matches == 26:
                return True

            l_indx = ord(s2[l]) - ord("a")
            r_indx = ord(s2[r]) - ord("a")

            freq2[l_indx] -= 1
            if freq2[l_indx] == freq1[l_indx]:
                matches += 1
            elif freq2[l_indx]+1 == freq1[l_indx]:
                matches -= 1

            freq2[r_indx] += 1
            if freq2[r_indx] == freq1[r_indx]:
                matches += 1
            elif freq2[r_indx]-1 == freq1[r_indx]:
                matches -= 1
            
            print(f"Window: {s2[l:r]}, Matches: {matches}, Freq2: {freq2}")
            l += 1
            r += 1
        
        return matches == 26



