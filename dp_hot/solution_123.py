from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        m = len(prices)
        if m <= 1:
            return 0

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(m)]

        for i in range(k + 1):
            dp[0][i][1] = -prices[0]


        for i in range(1, m):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][-1][0]


result = Solution().maxProfit([3,3,5,0,0,3,1,4])
print(result)