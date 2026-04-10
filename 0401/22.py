from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backTrack(left: int, right: int, track: List[str]):
            if left == 0 and right == 0:
                ans.append(''.join(track))
                return

            if left > 0:
                track.append('(')
                backTrack(left - 1, right, track)
                track.pop()

            if right > left:
                track.append(')')
                backTrack(left, right - 1, track)
                track.pop()

        backTrack(n, n, [])

        return ans


result = Solution().generateParenthesis(3)
print(result)
