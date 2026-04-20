import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opt = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y)
        }
        stack = []

        for elt in tokens:
            if elt not in opt:
                stack.append(int(elt))
            else:        
                opd2 = stack.pop()
                opd1 = stack.pop()

                stack.append(opt[elt](opd1, opd2))

        return stack[-1]
        