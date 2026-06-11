class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c in t:
            freq1[c] += 1

        have, need = 0, len(freq1)
        start, end = 0, float("infinity")
        l, r = 0, 0
        while r < len(s):
            c = s[r]

            if c in freq1:
                freq2[c] += 1
                if freq2[c] == freq1[c]:
                    have += 1

            while have == need:
                if (r - l) < (end - start):
                    start = l
                    end = r

                if s[l] in freq1:
                    freq2[s[l]] -= 1
                    if freq2[s[l]] < freq1[s[l]]:
                        have -= 1           
                l += 1
            
            r += 1

        if end != float("infinity"):
            return s[start:end+1]
        else:
            return ""
    
                

        
        