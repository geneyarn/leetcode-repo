from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for c in tokens:
            if c in '+-*/':
                last = int(stk.pop())
                ll = int(stk.pop())
                if c == '+':
                    stk.append(last + ll)
                elif c == '*':
                    stk.append(last * ll)
                elif c == '/':
                    stk.append(int(ll / last))
                else:
                    stk.append(ll - last)
            else:
                stk.append(c)
        return stk[0]


# reuslt = Solution().evalRPN(["2", "1", "+", "3", "*"])
reuslt = Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(reuslt)
