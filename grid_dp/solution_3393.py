from functools import cache
from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007

        @cache
        def dfs(i: int, j: int, x: int) -> int:
            if i < 0 or j < 0:
                return 0

            val = grid[i][j]
            if i == 0 and j == 0:
                return 1 if x == val else 0

            return (dfs(i - 1, j, val ^ x) + dfs(i, j - 1, val ^ x)) % MOD

        return dfs(len(grid) - 1, len(grid[-1]) - 1, k)


result = Solution().countPathsWithXorValue([[2, 1, 5], [7, 10, 0], [12, 6, 4]], 11)
print(result)
