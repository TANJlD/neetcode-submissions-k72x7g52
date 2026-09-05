class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                ans += 2

        if ans < len(s):
            return ans+1

        return ans