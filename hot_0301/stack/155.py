class MinStack:

    def __init__(self):
        self.q = []
        self.stk = []

    def push(self, val: int) -> None:
        self.q.append(val)
        if self.stk and self.stk[-1] < val:
            self.stk.append(self.stk[-1])
        else:
            self.stk.append(val)

    def pop(self) -> None:
        v = self.q.pop()
        if v == self.stk[-1]:
            self.stk.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.stk[-1]


minStack = MinStack();
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
