class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallest) == 0:
            self.smallest.append(val)
        elif min(self.smallest[-1], val) == val:
                self.smallest.append(val)
    
    def pop(self) -> None:
        lost = self.stack.pop()
        if lost == self.smallest[-1]:
            self.smallest.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]