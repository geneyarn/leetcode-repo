from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        m = len(s)
        ans = []

        def isPan(l: int, r: int) -> bool:
            if l >= r:
                return True

            return s[l] == s[r] and isPan(l + 1, r - 1)

        def backTrack(idx: int, track: List[str]):
            if idx == m:
                ans.append(track.copy())
                return

            for i in range(idx, m):
                if isPan(idx, i):
                    track.append(s[idx:i + 1])
                    backTrack(i + 1, track)
                    track.pop()

        backTrack(0, [])

        return ans


result = Solution().partition('aab')
print(result)
