from math import inf
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        dp[0][0] = triangle[0][0]

        for i in range(1, m):
            for j in range(i + 1):
                dp[i][j] = min(dp[i - 1][j] if j < i else inf,
                               dp[i - 1][j - 1] if j - 1 >= 0 else inf) + triangle[i][j]

        return min(dp[-1])


result = Solution().minimumTotal([[2],
                                  [3, 4],
                                  [6, 5, 7],
                                  [4, 1, 8, 3]])
print(result)
