from typing import List


class Solution:

    def __init__(self):
        self.track = []
        self.ans = []

    def valid(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def backTrack(self, s: str, idx: int):
        if idx == len(s):
            self.ans.append(self.track.copy())
            return

        for i in range(idx, len(s)):
            if self.valid(s, idx, i):
                self.track.append(s[idx:i + 1])
                self.backTrack(s, i + 1)
                self.track.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backTrack(s, 0)
        return self.ans


result = Solution().partition('aab')
print(result)
