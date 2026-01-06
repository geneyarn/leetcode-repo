from functools import cache
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i: int, j: int, mod: int) -> int:
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1 if mod == 0 else 0

            nxtMod = (mod - grid[i][j]) % k

            return dp(i - 1, j, nxtMod) + dp(i, j + 1, nxtMod)

        return dp(m - 1, n - 1, 0)
