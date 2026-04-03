class Solution:
    def maxScore(self, s: str) -> int:
        max = 0
        for i in range(len(s)-1):
            score = s[:i+1].count("0") + s[i+1:].count("1")
            if score > max:
                max = score
        return max