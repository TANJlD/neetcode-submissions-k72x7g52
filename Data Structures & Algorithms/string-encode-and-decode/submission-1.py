class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ""
        for w in strs:
            en_str = en_str + w + "~+~"

        return en_str


    def decode(self, s: str) -> List[str]:
        de_str = s.split("~+~")
        de_str.pop()
        return de_str
