from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dp(i,j) = min(dp[i + 1][j], dp[i][j+1]) - dungeon[i][j]
        m, n = len(dungeon), len(dungeon[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = float('inf')

        for j in range(n + 1):
            dp[m][j] = float('inf')

        dp[m - 1][n - 1] = -dungeon[m - 1][n - 1] + 1 if dungeon[m - 1][n - 1] < 0 else 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                minValue = min(
                    dp[i + 1][j],
                    dp[i][j + 1]
                ) - dungeon[i][j]
                dp[i][j] = 1 if minValue <= 0 else minValue
        return dp[0][0]


# result = Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
result = Solution().calculateMinimumHP([[0]])
result = Solution().calculateMinimumHP([[2], [1]])
print(result)
