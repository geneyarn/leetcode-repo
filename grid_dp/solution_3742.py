from functools import cache
from math import inf
from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return -inf
            if i == 0 and j == 0:
                return 0
            v = grid[i][j]
            if v == 0:
                return max(dp(i - 1, j, k), dp(i, j - 1, k))
            else:
                if k == 0:
                    return -inf
                return grid[i][j] + max(dp(i - 1, j, k - 1), dp(i, j - 1, k - 1))

        result = dp(m - 1, n - 1, k)
        return -1 if result == -inf else result


result = Solution().maxPathScore([[0, 1], [2, 0]], 1)
# result = Solution().maxPathScore([[0, 1],
#                                   [1, 2]], 1)
print(result)
