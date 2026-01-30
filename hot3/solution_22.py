from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def traverse(self, left: int, right: int, track: List[str]):
        if left == 0 and right == 0:
            self.ans.append(''.join(track))
            return
        if left > 0:
            track.append('(')
            self.traverse(left - 1, right, track)
            track.pop()
        if right > left:
            track.append(')')
            self.traverse(left, right - 1, track)
            track.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.traverse(n, n, [])
        return self.ans
