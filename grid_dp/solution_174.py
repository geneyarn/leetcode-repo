from cmath import inf
from functools import cache
from typing import List


class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @cache
        def dp(i: int, j: int) -> int:
            if i >= m or j >= n:
                return inf
            if i == m - 1 and j == n - 1:
                return 1 if dungeon[i][j] >= 0 else -dungeon[i][j] + 1

            result = max(min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j], 1)
            return result

        return dp(0, 0)


result = Solution().calculateMinimumHP([[-2, -3, 3],
                                        [-5, -10, 1],
                                        [10, 30, -5]])
print(result)
