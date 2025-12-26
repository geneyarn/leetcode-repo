class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []

        for n in range(len(num)):
            while stk and k > 0 and stk[-1] > num[n]:
                k -= 1
                stk.pop()

            if not stk and num[n] == '0':
                continue
            stk.append(num[n])

        finalStack = stk[:-k] if k > 0 else stk

        return ''.join(finalStack)


result = Solution().removeKdigits('1432219', 3)
print(result)
