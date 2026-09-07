class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.miniStack:
            self.miniStack.append(val)
        elif val <= self.miniStack[-1]:
            self.miniStack.append(val)
            

    def pop(self) -> None:
        if self.stack.pop() == self.miniStack[-1]:
            self.miniStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.miniStack:
            return self.miniStack[-1]
