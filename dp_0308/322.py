from cmath import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)

        dp = [[inf] * (amount + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            v = coins[i - 1]
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= v:
                    dp[i][j] = min(dp[i][j], dp[i][j - v] + 1)

        return dp[-1][-1] if dp[-1][-1] != inf else -1


result = Solution().coinChange([1, 2, 5], 11)
# result = Solution().coinChange([2], 3)
print(result)
