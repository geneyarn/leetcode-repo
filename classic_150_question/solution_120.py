from cmath import inf
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])

        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + triangle[i][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])

        ans = inf
        for i in range(n):
            ans = min(ans, dp[-1][i])
        return ans


result = Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print(result)
