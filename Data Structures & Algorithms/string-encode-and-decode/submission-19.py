class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = []

        for s in strs:
            new_strs.append(str((len(s))) + "#" + s)

        encoded = "".join(new_strs)

        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        seen = 0

        while seen != len(s) :
            num = ""
            for c in s[seen:]:
                seen += 1
                if c != "#":
                    num = num + c
                elif c == "#":
                    count = int(num)
                    word = ""
                    for l in s[seen:(seen+count)]:
                        seen += 1
                        word = word + l
                    decoded.append(word)
                    break

        return decoded
