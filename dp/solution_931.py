from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])

        m = len(matrix)

        dp = [[0] * m for _ in range(m)]

        for i in range(m):
            dp[0][i] = matrix[0][i]

        for i in range(1, m):
            for j in range(m):
                dp[i][j] = matrix[i][j] + dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + matrix[i][j])
                if j + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + matrix[i][j])

        return min([dp[m - 1][i] for i in range(m)])


result = Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
print(result)
