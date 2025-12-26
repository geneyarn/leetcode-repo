from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        m = len(prices)
        if m <= 1:
            return 0

        dp = [[0] * 2 for _ in range(m)]
        dp[0][1] = -prices[0]

        for i in range(1, m):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]


result = Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
print(result)
