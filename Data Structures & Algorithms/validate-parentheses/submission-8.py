class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for par in s:
            if stack and par in map:
                if stack.pop() != map[par]:
                    return False
            else:
                stack.append(par)

        return not stack
