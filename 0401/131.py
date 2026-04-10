from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        m = len(s)

        ans = []

        def valid(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backTrack(idx: int, track: list[str]):
            if idx == m:
                ans.append(track.copy())
                return

            for i in range(idx, m):
                if valid(idx, i):
                    sub = s[idx: i + 1]
                    track.append(sub)
                    backTrack(i + 1, track)
                    track.pop()

        backTrack(0, [])

        return ans


result = Solution().partition('aab')
print(result)
