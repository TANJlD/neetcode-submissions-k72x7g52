class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        max_freq = 0
        max_sub = 0

        l = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            max_freq = max(max_freq, chars[s[r]])

            if (r-l+1) - max_freq <= k:
                max_sub = max(max_sub, r-l+1)
            else:
                while (r-l+1) - max_freq > k:
                    chars[s[l]] -= 1
                    l += 1

        return max_sub 




        
        