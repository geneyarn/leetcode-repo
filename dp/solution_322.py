from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):

            for c in coins:
                if i - c < 0:
                    continue

                dp[i] = min(dp[i - c] + 1, dp[i])

        return -1 if dp[-1] == amount + 1 else dp[-1]


# result = Solution().coinChange([1, 2, 5], 11)
result = Solution().coinChange([2], 3)
print(result)
