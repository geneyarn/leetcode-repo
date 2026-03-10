from functools import cache
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i: int, j: int, mod: int) -> int:
            if i < 0 or j < 0:
                return 0

            newMode = (mod - grid[i][j]) % k
            if i == 0 and j == 0:
                return 1 if newMode == 0 else 0

            return (dp(i - 1, j, newMode) + dp(i, j - 1, newMode)) % 1_000_000_007

        ans = dp(m - 1, n - 1, 0)
        dp.cache_clear()
        return ans


result = Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3)
print(result)
