class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        n = len(self.stack)
        mn = self.stack[0]

        for i in range(1, n):
            if self.stack[i] < mn:
                mn = self.stack[i]

        return mn
        
