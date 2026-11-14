class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        digit_letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        curr = []

        def dfs(i):
            if i == len(digits):
                result.append("".join(curr))
                return

            letters = digit_letters[int(digits[i])-2]
            for j in range(len(letters)):
                curr.append(letters[j])
                dfs(i+1)
                curr.pop()

        dfs(0)
        return result