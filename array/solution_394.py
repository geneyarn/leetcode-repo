from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        stk: List[str] = []

        for c in s:
            if c == ']':
                tmp = ''
                while stk[-1] != '[':
                    tmp = stk.pop() + tmp

                # pop [
                stk.pop()
                n = ''
                while len(stk) > 0 and stk[-1].isdigit():
                    n = stk.pop() + n

                result = ''
                for i in range(int(n)):
                    result += tmp
                stk.append(result)
            else:
                stk.append(c)
        return ''.join(stk)


result = Solution().decodeString('3[a]2[bc]')
print(result)
