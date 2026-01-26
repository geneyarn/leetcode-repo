from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        m = len(s)
        ans = []
        track = []

        def isPan(i: int, j: int) -> bool:
            if i >= j:
                return True
            return s[i] == s[j] and isPan(i + 1, j - 1)

        def backTrack(idx: int):
            if idx == m:
                ans.append(track.copy())
                return

            for i in range(idx, m):
                if isPan(idx, i):
                    track.append(s[idx: i + 1])
                    backTrack(i + 1)
                    track.pop()

        backTrack(0)
        return ans


result = Solution().partition('aab')
print(result)
