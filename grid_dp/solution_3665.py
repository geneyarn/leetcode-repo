from functools import cache
from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1

            result = 0
            if grid[i][j] == 0:
                result = dp(i, j - 1, 0) + dp(i - 1, j, 1)
            else:
                if k == 0:
                    result = dp(i - 1, j, 1)
                else:
                    result = dp(i, j - 1, 0)

            return result

        return dp(m - 1, n - 1, 1)


# result = Solution().uniquePaths([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
# result = Solution().uniquePaths([[0, 0], [0, 0]])
result = Solution().uniquePaths([[0, 1, 1],
                                 [1, 1, 0]])
print(result)
