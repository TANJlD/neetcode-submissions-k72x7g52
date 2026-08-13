class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        matches = 0
        found = False

        for c in t:
            freq1[c] += 1

        l = 0
        start, end = 0, len(s) - 1
        for r in range(len(s)):
            if s[r] in freq1:
                freq2[s[r]] += 1
                if freq2[s[r]] == freq1[s[r]]:
                    matches += 1

            while matches == len(freq1):
                found = True
                if (r - l) < (end - start):
                    start = l
                    end = r
                if s[l] in freq1:
                    freq2[s[l]] -= 1
                    if freq2[s[l]] < freq1[s[l]]:
                        matches -= 1
                l += 1

        if not found:
            return ""
        return s[start:end+1]