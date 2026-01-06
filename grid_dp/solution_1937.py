from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = points[0][i]

        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = max(points[i][j] + dp[i - 1][k] - abs(k - j), dp[i][j])

        return max(dp[-1])


result = Solution().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]])
print(result)
