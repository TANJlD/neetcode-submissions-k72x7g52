class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                p = stack.pop()
                if s[i] == ")":
                    if p != "(":
                        return False
                elif s[i] == "}":
                    if p != "{":
                        return False
                else:
                    if p != "[":
                        return False

        if stack:
            return False


        return True
        