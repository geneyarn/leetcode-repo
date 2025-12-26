from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def backTrack(self, n: int, idx: int, k: int, track: List[int]):
        if len(track) == k:
            self.ans.append(track.copy())
            return

        for i in range(idx, n + 1):
            track.append(i)
            self.backTrack(n, i + 1, k, track)
            track.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backTrack(n, 1, k, [])
        return self.ans


result = Solution().combine(4, 2)
print(result)