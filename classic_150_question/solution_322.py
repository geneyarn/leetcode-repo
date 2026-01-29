from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)

        dp = [[inf] * (amount + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0
        for i in range(1, m + 1):
            n = coins[i - 1]
            for j in range(1, amount + 1):
                if j >= n:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - n] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1] if dp[-1][-1] != inf else -1


result = Solution().coinChange([1, 2, 5], 11)
print(result)
