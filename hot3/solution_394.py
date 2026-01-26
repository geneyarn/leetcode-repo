class Solution:

    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ']':
                tmp = ''
                while stk[-1] != '[':
                    tmp = stk.pop() + tmp

                stk.pop()
                n = ''
                while stk and stk[-1].isdigit():
                    n = stk.pop() + n

                result = ''
                for _ in range(int(n)):
                    result += tmp
                stk.append(result)
            else:
                stk.append(c)
        return ''.join(stk)


# result = Solution().decodeString('3[a]2[bc]')
result = Solution().decodeString('3[a2[c]]')
print(result)
