class Solution:
    def isValid(self, s: str) -> bool:
        m = len(s)

        stk = []
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in range(m):
            c = s[i]
            if c not in mp:
                stk.append(c)
            else:
                if not stk:
                    return False
                if mp[c] != stk[-1]:
                    return False
                stk.pop()
        return not stk


result = Solution().isValid('(')
print(result)
