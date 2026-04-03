class Solution:
    def maxScore(self, s: str) -> int:
        preArray = [0] * (len(s)-1)

        prefix = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                prefix += 1
            preArray[i] = prefix

        postfix = 0
        max = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == "1":
                postfix += 1
            if max < postfix + preArray[i-1]:
                max = postfix + preArray[i-1]

        return max 
