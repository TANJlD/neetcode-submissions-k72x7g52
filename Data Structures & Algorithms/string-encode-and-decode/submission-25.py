class Solution:

    def encode(self, strs: List[str]) -> str:
        encodes = []

        for word in strs:
            encodes.append(str(len(word)))
            encodes.append("#")
            encodes.append(word)

        return "".join(encodes)



    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            
            length = int(s[start:i])

            i += 1

            strs.append(s[i:i+length])

            i += length

        return strs


