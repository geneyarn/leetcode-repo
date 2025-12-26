from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def backTrack(self, track: List[str], left: int, right: int):
        if left < 0 and right < 0:
            return
        if left == 0 and right == 0:
            self.ans.append(''.join(track))
            return

        if left > 0:
            track.append('(')
            self.backTrack(track, left - 1, right)
            track.pop()

        if right > 0 and right > left:
            track.append(')')
            self.backTrack(track, left, right - 1)
            track.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.backTrack([], n, n)

        return self.ans


result = Solution().generateParenthesis(3)
print(result)
