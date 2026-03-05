class Solution:
    def decodeString(self, s: str) -> str:
        m = len(s)
        stk = []
        for i in range(m):
            c = s[i]

            if c != ']':
                stk.append(c)

            else:
                tmp = ''

                # ''.isdigit()
                while stk and stk[-1].isalpha():
                    tmp = stk.pop() + tmp
                stk.pop()

                countStr = ''
                while stk and stk[-1].isdigit():
                    countStr = stk.pop() + countStr

                count = int(countStr)
                ans = ''
                for _ in range(count):
                    ans += tmp

                stk.append(ans)

        return ''.join(stk)


# result = Solution().decodeString('3[a]2[bc]')
result = Solution().decodeString('3[a2[c]]')
print(result)
