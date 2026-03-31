
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 1. Read the number (length)
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            # 2. Extract the word
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # 3. Move pointer forward
            i = j + 1 + length

        return res