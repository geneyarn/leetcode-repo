class Solution:
    def isValid(self, s: str) -> bool:

        mp = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stk = []
        for c in s:
            if c in mp.keys():
                stk.append(c)
            else:
                if len(stk) == 0:
                    return False
                last = stk[-1]
                if c != mp.get(last):
                    return False
                stk.pop()
        return len(stk) == 0


# result = Solution().isValid('()')
result = Solution().isValid('(]')
print(result)
