class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = set(s1)
        freq = [0] * 26

        for c in s1:
            indx = ord(c) - ord("a")
            freq[indx] += 1
        l = 0
        for r in range(len(s2)):
            indx = ord(s2[r]) - ord("a")
            if s2[r] in chars:
                freq[indx] -= 1
            else:
                freq[indx] += 1
            
            if r >= len(s1):
                indx = ord(s2[l]) - ord("a")
                if s2[l] in chars:
                    freq[indx] += 1
                else:
                    freq[indx] -= 1
                l += 1
            
            count = 0
            for n in freq:
                if n == 0:
                    count += 1
                if count == 26:
                    return True
        
        return False
