class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 
            countT[t[i]] = countT.get(t[i], 0) + 1

        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
        return True
        









"""
        if len(s) != len(t):
            return False
        for c in s:
            if s.count(c) != t.count(c):
                return False

        return True
"""     