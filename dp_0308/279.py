import math
from cmath import inf


class Solution:
    def numSquares(self, n: int) -> int:
        big = math.ceil(math.pow(n, 0.5)) + 1

        dp = [[inf] * (n + 1) for _ in range(big + 1)]
        dp[0][0] = 0

        for i in range(1, big + 1):
            v = i ** 2
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j - v >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - v] + 1)

        return dp[-1][-1]

result = Solution().numSquares(12)
print(result)
