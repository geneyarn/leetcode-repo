from typing import List


class Solution:

    def __init__(self):
        self.ans = []

    def valid(self, s: str, start: int, end: int) -> bool:
        i, j = start, end

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def backTrack(self, s: str, track: List[str], idx: int):
        if idx == len(s):
            self.ans.append(track.copy())
            return

        for i in range(idx, len(s)):
            sub = s[idx: i + 1]
            if not self.valid(s, idx, i):
                continue
            track.append(sub)
            self.backTrack(s, track, i + 1)
            track.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backTrack(s, [], 0)
        return self.ans


result = Solution().partition('aab')
print(result)
