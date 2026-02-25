from typing import List


class Solution:

    def __init__(self):
        self.track = []
        self.ans = []

        self.k = 0

    def backTrack(self, cur: int, n: int):
        if len(self.track) == self.k:
            self.ans.append(self.track.copy())
            return

        for i in range(cur, n + 1):
            self.track.append(i)
            self.backTrack(i + 1, n)
            self.track.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.backTrack(1, n)
        return self.ans


result = Solution().combine(4, 2)
print(result)
