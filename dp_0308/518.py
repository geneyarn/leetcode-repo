from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)

        dp = [[0] * (amount + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            v = coins[i - 1]
            for j in range(amount + 1):
                if j >= v:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - v]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


# result = Solution().change(5, [1, 2, 5])
result = Solution().change(3, [2])
print(result)
