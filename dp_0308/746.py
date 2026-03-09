from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m = len(cost)

        def dp(n: int) -> int:
            if n <= 1:
                return 0

            return min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])

        return dp(m)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        m = len(cost)
        if m <= 2:
            return min(cost)
        dp = [0] * (m + 1)

        for i in range(2, m + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]


result = Solution().minCostClimbingStairs([10, 15, 20])
print(result)
