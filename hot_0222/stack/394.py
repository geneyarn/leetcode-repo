class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        for c in s:
            if c == ']':
                tmp = ''
                while stk and stk[-1] != '[':
                    tmp = stk.pop() + tmp

                stk.pop()

                number = ''
                while stk and stk[-1].isdigit():
                    number = stk.pop() + number

                n = int(number)
                t = ''
                for i in range(n):
                    t += tmp

                stk.append(t)
            else:
                stk.append(c)

        return ''.join(stk)


# result = Solution().decodeString('3[a]2[bc]')
result = Solution().decodeString('3[a2[c]]')
print(result)
