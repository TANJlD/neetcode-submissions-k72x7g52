class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = []
        for s in strs:
            new_strs.append(s + "~+~")

        en_str = "".join(new_strs)

        return en_str


    def decode(self, s: str) -> List[str]:
        de_str = s.split("~+~")
        de_str.pop()

        return de_str
