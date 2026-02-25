class Solution:

    def __init__(self):
        self.mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

    def isValid(self, s: str) -> bool:
        stk = []
        m = len(s)

        for c in s:
            if c not in self.mp:
                stk.append(c)
            else:
                need = self.mp[c]
                if not stk or stk[-1] != need:
                    return False
                stk.pop()

        return len(stk) == 0


result = Solution().isValid("([])")
print(result)
