from cmath import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)

        dp = [[inf] * (amount + 1) for _ in range(m)]

        for i in range(m):
            dp[i][0] = 0

        for i in range(m):
            c = coins[i]
            for j in range(1, amount + 1):
                if j >= c:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - c] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1] if dp[-1][-1] < amount + 1 else -1


result = Solution().coinChange([1, 2, 5], 11)
print(result)
