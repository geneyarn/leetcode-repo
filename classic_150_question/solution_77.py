from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        track = []
        ans = []

        def backTrack(idx: int):
            if len(track) == k:
                ans.append(track.copy())
                return
            if idx > n:
                return

            for i in range(idx, n + 1):
                track.append(i)
                backTrack(i + 1)
                track.pop()

        backTrack(1)
        return ans


result = Solution().combine(4, 2)
print(result)
