from math import inf
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        m = len(prices)
        dp = [[[-inf] * 3 for _ in range(k + 1)] for _ in range(m)]

        for i in range(m):
            for j in range(k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                    dp[i][j][0] = prices[0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i], dp[i - 1][j][2] - prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                    dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j - 1][0] + prices[i])

        return dp[-1][-1][0]


result = Solution().maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3)
print(result)
