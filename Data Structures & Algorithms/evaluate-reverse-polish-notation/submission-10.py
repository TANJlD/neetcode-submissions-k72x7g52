class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y, 
            "/" : lambda x, y: int(x / y)
        }
        stack = []

        for token in tokens:
            if token in op:
                y = stack.pop()
                x = stack.pop()

                stack.append(op[token](x, y))

            else:
                stack.append(int(token))

        return stack[-1]


        