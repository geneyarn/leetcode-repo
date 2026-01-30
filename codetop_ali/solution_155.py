class MinStack:

    def __init__(self):
        self.stk = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.stk or val <= self.stk[-1]:
            self.stk.append(val)
        else:
            self.stk.append(self.stk[-1])

    def pop(self) -> None:
        d = self.arr.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.stk[-1]


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin());  # --> 返回 -3.
minStack.pop();
print(minStack.top());  # --> 返回 0.
print(minStack.getMin());  # --> 返回 -2.
