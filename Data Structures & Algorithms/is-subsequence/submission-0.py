class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = len(t)
        found = 0
        for c in s:
            while l < r:
                if t[l] == c:
                    found += 1
                    l += 1
                    break
                l += 1
                    
        return found == len(s)
    