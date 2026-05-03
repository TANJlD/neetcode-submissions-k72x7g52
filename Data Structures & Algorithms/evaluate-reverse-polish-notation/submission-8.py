class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opts = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y)
        }
        
        stack = []

        for token in tokens:
            if token in opts:
                y = stack.pop()
                x = stack.pop()

                stack.append(opts[token](x, y))
            else:
                stack.append(int(token))

        return stack[-1]

