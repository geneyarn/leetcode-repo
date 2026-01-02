from functools import cache
from math import inf
from typing import List


class Solution:

    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i >= m or j >= n:
                return inf
            if i == m - 1 and j == n - 1:
                return m * n

            return min(dp(i + 1, j), dp(i, j + 1)) + (i + 1) * (j + 1) + waitCost[i][j]

        return dp(0, 0) - waitCost[0][0]

    def minCost2(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return 1

            return min(dp(i - 1, j), dp(i, j - 1)) + (i + 1) * (j + 1) + waitCost[i][j]

        return dp(m - 1, n - 1) - waitCost[-1][-1]


result = Solution().minCost(2, 2,
                            [[3, 5],
                             [2, 4]])

# result = Solution().minCost(2, 3, [[6, 1, 4], [3, 2, 5]])

print(result)
