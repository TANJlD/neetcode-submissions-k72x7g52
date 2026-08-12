class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        max_len = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            max_freq = max(max_freq, chars[s[r]])

            while (r - l + 1) - max_freq > k:
                chars[s[l]] -= 1
                l += 1

            max_len = max(max_len, (r - l + 1))

        return max_len 

        