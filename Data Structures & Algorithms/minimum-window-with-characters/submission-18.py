class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for i in range(len(t)):
            freq1[t[i]] += 1

        for i in range(len(t)):
            if s[i] in freq1:
                freq2[s[i]] += 1

        matches = 0

        for c in freq1.keys():
            if freq2[c] >= freq1[c]:
                matches += 1

        if matches == len(freq1):
            return s[:len(t)]
        
        start = 0
        end = float("infinity")

        

        l = 0
        for r in range(len(t), len(s)):
            
            if s[r] in freq1:
                freq2[s[r]] += 1
                if freq2[s[r]] == freq1[s[r]]:
                    matches += 1

            while matches == len(freq1):
                if (r - l) < (end - start):
                    start = l
                    end = r
                if s[l] in freq1:
                    freq2[s[l]] -= 1
                    if freq2[s[l]] < freq1[s[l]]:
                        matches -= 1
                l += 1
                

        return s[start:end+1] if end != float("infinity") else ""