class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        max_sub = 0

        l = 0
        r = 0

        while r < len(s):
            if r == 0:
                chars[s[r]] += 1

            valid = self.findValid(chars, l, r, k)

            if valid:
                max_sub = max(max_sub, r-l+1)
                if r == len(s)-1:
                    return max_sub
                r += 1
                chars[s[r]] += 1
            else:
                chars[s[l]] -= 1
                l += 1

        return max_sub


    def findValid(self, chars, l, r, k):
        freq = [x for x in chars.values()]

        if (r-l+1) - max(freq) <= k:
            return True
        else:
            return False


        
        