class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")" : "(",
               "}" : "{",
               "]" : "["}

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                p = stack.pop()
                if p != dic[s[i]]:
                    return False

        if stack:
            return False


        return True
        