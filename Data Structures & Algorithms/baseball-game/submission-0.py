class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op not in "+CD":
                stack.append(int(op))
            elif stack and op == "+":
                sum = int(stack[-1]) + int(stack[-2])
                stack.append(sum)
            elif stack and op == "D":
                pro = int(stack[-1]) * 2
                stack.append(pro)
            elif stack and op == "C":
                stack.pop()

        print(stack)

        res = 0    
        for n in stack:
            res += n

        return res

        