class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            tem = ord(s[i+1]) - ord(s[i])
            if tem >= 0:
                sum += tem
            else:
                sum += tem * -1

        return sum

        