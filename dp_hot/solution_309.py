from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        if m <= 1:
            return 0
        dp = [[0] * 2 for _ in range(m)]
        dp[0][1] = -prices[0]
        dp[1][0] = max(0, prices[1] - prices[0])
        dp[1][1] = max(-prices[0], -prices[1])

        for i in range(2, m):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[-1][0]

result = Solution().maxProfit([1,2,3,0,2])
print(result)

