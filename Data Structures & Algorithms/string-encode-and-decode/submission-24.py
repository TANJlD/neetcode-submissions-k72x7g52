class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s = s + str(len(word)) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < (len(s)-1):
            length = ""
            
            while s[i] != "#":
                length += s[i]
                i += 1

            j = i + int(length) + 1
            strs.append(s[i+1:j])

            i = j

        return strs



