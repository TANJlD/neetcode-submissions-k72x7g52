class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0
        anomaly = 0

        for c in s:
            count[c] += 1

        for v in count.values():
            if (v % 2) == 0:
                ans += v
            else:
                ans += (v-1)
        
        if ans < len(s):
            return (ans+1)

        return ans
        