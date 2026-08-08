class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            if s[i] not in mapST:
                if t[i] in mapTS:
                    return False
                mapST[s[i]] = t[i]
                mapTS[t[i]] = s[i]
            else:
                if mapST[s[i]] != t[i]:
                    return False

        return True