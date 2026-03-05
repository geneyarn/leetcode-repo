from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.track = []

    def valid(self, s: str) -> bool:
        i, j = 0, len(s) - 1
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

        for i in range(idx + 1, len(s) + 1):
            sub = s[idx:i]
            if self.valid(sub):
                self.track.append(sub)
                self.backTrack(s, i)
                self.track.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backTrack(s, 0)
        return self.ans


result = Solution().partition('aab')
print(result)
