class MinStack:

    def __init__(self):
        self.stack = []
        self.mStack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mStack.append(val)
        else:
            self.stack.append(val)
            top = self.mStack[-1]
            if val < top:
                self.mStack.append(val)
            else:
                self.mStack.append(top)
            
    
    def pop(self) -> None:
        self.stack.pop()
        self.mStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mStack[-1]
        
