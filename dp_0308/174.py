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

            return max(
                1,
                min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j]
            )

        ans = dp(0, 0)
        dp.cache_clear()
        return ans

    def calculateMinimumHP2(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue

                dp[i][j] = max(1,
                               min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                               )

        return dp[0][0]


result = Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
print(result)
