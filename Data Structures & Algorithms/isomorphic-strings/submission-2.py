class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        maps = {}
        mapt = {}

        for i in range(len(s)):
            if s[i] not in maps:
                if t[i] in mapt:
                    return False
                maps[s[i]] = t[i]
                mapt[t[i]] = s[i]
            else:
                if maps[s[i]] != t[i]:
                    return False

        return True