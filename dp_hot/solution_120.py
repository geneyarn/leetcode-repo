from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])

        dp = [[10001] * m for _ in range(m)]
        dp[0][0] = triangle[0][0]

        for i in range(1, m):
            for j in range(i + 1):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])
                if j < i:
                    dp[i][j] = min(dp[i - 1][j] + triangle[i][j], dp[i][j])

        return min(dp[-1])


result = Solution().minimumTotal([[2],
                                  [3, 4],
                                  [6, 5, 7],
                                  [4, 1, 8, 3]])
print(result)
