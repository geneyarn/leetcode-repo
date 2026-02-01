from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        track = []

        def generate(left: int, right: int):
            if left == 0 and right == 0:
                ans.append(''.join(track))
                return
            if left > 0:
                track.append('(')
                generate(left - 1, right)
                track.pop()
            if right > left:
                track.append(')')
                generate(left, right - 1)
                track.pop()

        generate(n, n)
        return ans


result = Solution().generateParenthesis(3)
print(result)
