from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[200 * m] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + matrix[i][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + matrix[i][j])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + matrix[i][j])

        return min(dp[-1])


result = Solution().minFallingPathSum([[2, 1, 3],
                                       [6, 5, 4],
                                       [7, 8, 9]])
print(result)
