class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = 0
        l2 = 0
        found = 0
        while l2 < len(t) and l1 < len(s):
            if s[l1] == t[l2]:
                found += 1
                l1 += 1
            l2 += 1
        return found == len(s)