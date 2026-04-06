class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = [0] * 26
        countT = [0] * 26

        for c in s:
            countS[ord(c)-ord("a")] += 1
        for c in t:
            countT[ord(c)-ord("a")] += 1

        return countS == countT
        