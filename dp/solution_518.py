from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)

        dp = [[0] * (amount + 1) for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1

        for i in range(m):
            for j in range(1, amount + 1):
                if j - coins[i] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]

        return dp[-1][-1]


result = Solution().change(5, [1, 2, 5])
print(result)
