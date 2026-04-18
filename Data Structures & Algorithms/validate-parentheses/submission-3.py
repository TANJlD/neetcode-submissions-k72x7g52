class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in dic:
                if not stack or stack.pop() != dic[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack
                 

        