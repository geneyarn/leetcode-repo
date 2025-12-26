from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                up = dp[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0
                left = dp[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0
                dp[i][j] = up + left
        return dp[-1][-1]


# result = Solution().uniquePathsWithObstacles([[0, 0, 0],
#                                               [0, 1, 0],
#                                               [0, 0, 0]])
result = Solution().uniquePathsWithObstacles([[0, 1],
                                              [0, 0]])
print(result)
