from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        m = len(prices)

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(m)]

        for i in range(m):
            for j in range(1, k + 1):
                if i - 1 == -1:
                    dp[i][j][1] = -prices[0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][-1][0]


# result = Solution().maxProfit(2, [2, 4, 1])
result = Solution().maxProfit(2, [3, 2, 6, 5, 0, 3])
print(result)
