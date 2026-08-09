class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        head, tail = 0, 0
        longest = 0

        for tail in range(len(s)):
            while s[tail] in sub and head < tail:
                sub.remove(s[head])
                head += 1
            sub.add(s[tail])
            longest = max(longest, (tail - head + 1))

        return longest 


