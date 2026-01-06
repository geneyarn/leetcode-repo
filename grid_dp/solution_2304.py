from cmath import inf
from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j],
                                   dp[i - 1][k] + grid[i][j] + moveCost[grid[i - 1][k]][j])

        return min(dp[-1])


result = Solution().minPathCost([[5, 3], [4, 0], [2, 1]],
                                [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]])
print(result)
