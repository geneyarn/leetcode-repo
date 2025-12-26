class MinStack:

    def __init__(self):
        self.minStk = []
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minStk or val <= self.minStk[-1]:
            self.minStk.append(val)

    def pop(self) -> None:
        # 注意 Java 的语言特性，比较 Integer 相等要用 equals 方法
        if self.stk[-1] == self.minStk[-1]:
            # 弹出的元素是全栈最小的
            self.minStk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
