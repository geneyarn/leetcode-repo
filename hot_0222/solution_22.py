from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.track = []

    def generate(self, left: int, right: int):
        if left == 0 and right == 0:
            self.ans.append(''.join(self.track))
            return
        if left > 0:
            self.track.append('(')
            self.generate(left - 1, right)
            self.track.pop()
        if right > left:
            self.track.append(')')
            self.generate(left, right - 1)
            self.track.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n, n)
        return self.ans
