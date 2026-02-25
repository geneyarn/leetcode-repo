class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []

        for c in num:

            while stk and k > 0 and stk[-1] > c:
                stk.pop()
                k -= 1

            if not stk and c == '0':
                continue
            stk.append(c)

        finalStk = stk[:-k] if k > 0 else stk

        result = ''.join(finalStk).lstrip('0')

        return result if result else '0'
