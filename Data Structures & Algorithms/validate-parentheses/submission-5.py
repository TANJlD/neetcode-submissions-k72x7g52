class Solution:
    def isValid(self, s: str) -> bool:
        prths = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for c in s:
            if c in prths and stack:
                p = stack.pop()
                if p != prths[c]:
                    return False
            else:
                stack.append(c)

        return not stack


        